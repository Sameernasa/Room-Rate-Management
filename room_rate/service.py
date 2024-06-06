from datetime import timedelta
from .models import RoomRate, OverriddenRoomRate, Discount, DiscountRoomRate
from django.db.models import Q



def get_final_rate(room_id, start_date, end_date):
    try:
        # Get the default room rate
        room_rate = RoomRate.objects.get(pk=room_id)
    except RoomRate.DoesNotExist:
        return None

    date_range = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]
    final_rates = []

    for date in date_range:
        # Check for overridden rate for the given date
        overridden_rate = OverriddenRoomRate.objects.filter(room_rate=room_rate, stay_date=date).first()
        room_rate_for_date = overridden_rate.overridden_rate if overridden_rate else room_rate.default_rate

        # Get all applicable discounts
        discounts = DiscountRoomRate.objects.filter(room_rate=room_rate).select_related('discount')

        # Calculate the highest discount
        highest_discount = 0
        for discount_room_rate in discounts:
            discount = discount_room_rate.discount
            if discount.discount_type == 'fixed':
                highest_discount = max(highest_discount, discount.discount_value)
            elif discount.discount_type == 'percentage':
                highest_discount = max(highest_discount, room_rate_for_date * (discount.discount_value / 100))

        # Calculate the final rate
        final_rate = max(0, room_rate_for_date - highest_discount)
        final_rates.append({'date': date, 'rate': final_rate})

    return final_rates