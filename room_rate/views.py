from datetime import timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from .models import RoomRate, OverriddenRoomRate, Discount, DiscountRoomRate
from .forms import RoomRateForm, OverriddenRoomRateForm, DiscountForm, FilterForm, DiscountRoomRateForm
from .service import get_final_rate
from django.views import View

class RoomRateListView(ListView):
    """
    Displays a list of all room rates.
    """
    model = RoomRate
    template_name = 'room_rate/room_rate_list.html'
    context_object_name = 'room_rates'

class RoomRateCreateView(CreateView):
    """
    Provides a form to add a new room rate.
    """
    model = RoomRate
    form_class = RoomRateForm
    template_name = 'room_rate/add_room_rate.html'
    success_url = reverse_lazy('room_rate_list')

class RoomRateUpdateView(UpdateView):
    """
    Provides a form to update an existing room rate.
    """
    model = RoomRate
    form_class = RoomRateForm
    template_name = 'room_rate/update_room_rate.html'
    success_url = reverse_lazy('room_rate_list')

class RoomRateDeleteView(DeleteView):
    """
    Confirms deletion of a room rate.
    """
    model = RoomRate
    template_name = 'room_rate/delete_room_rate.html'
    success_url = reverse_lazy('room_rate_list')

class OverriddenRoomRateListView(ListView):
    """
    Displays a list of overridden room rates.
    """
    model = OverriddenRoomRate
    template_name = 'room_rate/overridden_room_rate_list.html'
    context_object_name = 'overridden_room_rates'

class OverriddenRoomRateCreateView(CreateView):
    """
    Provides a form to add a new overridden room rate.
    """
    model = OverriddenRoomRate
    form_class = OverriddenRoomRateForm
    template_name = 'room_rate/add_overridden_room_rate.html'
    success_url = reverse_lazy('overridden_room_rate_list')

class OverriddenRoomRateUpdateView(UpdateView):
    """
    Provides a form to update an existing overridden room rate.
    """
    model = OverriddenRoomRate
    form_class = OverriddenRoomRateForm
    template_name = 'room_rate/update_overridden_room_rate.html'
    success_url = reverse_lazy('overridden_room_rate_list')

class OverriddenRoomRateDeleteView(DeleteView):
    """
    Confirms deletion of an overridden room rate.
    """
    model = OverriddenRoomRate
    template_name = 'room_rate/delete_overridden_room_rate.html'
    success_url = reverse_lazy('overridden_room_rate_list')

class DiscountListView(ListView):
    """
    Displays a list of all discounts.
    """
    model = Discount
    template_name = 'room_rate/discount_list.html'
    context_object_name = 'discounts'

class DiscountCreateView(CreateView):
    """
    Provides a form to add a new discount.
    """
    model = Discount
    form_class = DiscountForm
    template_name = 'room_rate/add_discount.html'
    success_url = reverse_lazy('discount_list')

class DiscountUpdateView(UpdateView):
    """
    Provides a form to update an existing discount.
    """
    model = Discount
    form_class = DiscountForm
    template_name = 'room_rate/update_discount.html'
    success_url = reverse_lazy('discount_list')

class DiscountDeleteView(DeleteView):
    """
    Confirms deletion of a discount.
    """
    model = Discount
    template_name = 'room_rate/delete_discount.html'
    success_url = reverse_lazy('discount_list')

class FilteredRoomRateView(View):
    """
    Filters and displays room rates based on room ID and date range, showing the lowest calculated rates considering discounts and overridden rates.
    """
    template_name = 'room_rate/filtered_room_rate_list.html'

    def get(self, request):
        """
        Handles GET requests and displays the filter form.
        """
        form = FilterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        """
        Handles POST requests, processes the filter form, and displays the filtered room rates.
        """
        form = FilterForm(request.POST)
        if form.is_valid():
            room = form.cleaned_data['room_id']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            room_rate = RoomRate.objects.get(pk=room.id)
            final_rates = get_final_rate(room.id, start_date, end_date)
            return render(request, self.template_name, {'form': form, 'final_rates': final_rates, 'room_name': room_rate.room_name})
        return render(request, self.template_name, {'form': form})

class DiscountRoomRateListView(ListView):
    """
    Displays a list of mappings between room rates and discounts.
    """
    model = DiscountRoomRate
    template_name = 'room_rate/discount_room_rate_list.html'
    context_object_name = 'discount_room_rates'

class DiscountRoomRateCreateView(CreateView):
    """
    Provides a form to map discounts to room rates.
    """
    model = DiscountRoomRate
    form_class = DiscountRoomRateForm
    template_name = 'room_rate/add_discount_room_rate.html'
    success_url = reverse_lazy('discount_room_rate_list')

class DiscountRoomRateUpdateView(UpdateView):
    """
    Provides a form to update a mapping between a room rate and a discount.
    """
    model = DiscountRoomRate
    form_class = DiscountRoomRateForm
    template_name = 'room_rate/update_discount_room_rate.html'
    success_url = reverse_lazy('discount_room_rate_list')

class DiscountRoomRateDeleteView(DeleteView):
    """
    Confirms deletion of a mapping between a room rate and a discount.
    """
    model = DiscountRoomRate
    template_name = 'room_rate/delete_discount_room_rate.html'
    success_url = reverse_lazy('discount_room_rate_list')
