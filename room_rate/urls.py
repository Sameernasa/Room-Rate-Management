from django.urls import path
import room_rate.views as views  

urlpatterns = [
    path('room-rates/', views.RoomRateListView.as_view(), name='room_rate_list'),
    path('room-rates/add/', views.RoomRateCreateView.as_view(), name='add_room_rate'),
    path('room-rates/edit/<int:pk>/', views.RoomRateUpdateView.as_view(), name='update_room_rate'),
    path('room-rates/delete/<int:pk>/', views.RoomRateDeleteView.as_view(), name='delete_room_rate'),
    path('overridden-room-rates/', views.OverriddenRoomRateListView.as_view(), name='overridden_room_rate_list'),
    path('overridden-room-rates/add/', views.OverriddenRoomRateCreateView.as_view(), name='add_overridden_room_rate'),
    path('overridden-room-rates/edit/<int:pk>/', views.OverriddenRoomRateUpdateView.as_view(), name='update_overridden_room_rate'),
    path('overridden-room-rates/delete/<int:pk>/', views.OverriddenRoomRateDeleteView.as_view(), name='delete_overridden_room_rate'),
    path('discounts/', views.DiscountListView.as_view(), name='discount_list'),
    path('discounts/add/', views.DiscountCreateView.as_view(), name='add_discount'),
    path('discounts/edit/<int:pk>/', views.DiscountUpdateView.as_view(), name='update_discount'),
    path('discounts/delete/<int:pk>/', views.DiscountDeleteView.as_view(), name='delete_discount'),
    path('filtered-room-rates/', views.FilteredRoomRateView.as_view(), name='filtered_room_rate_list'),
    path('discount-room-rates/', views.DiscountRoomRateListView.as_view(), name='discount_room_rate_list'),
    path('discount-room-rates/add/', views.DiscountRoomRateCreateView.as_view(), name='add_discount_room_rate'),
    path('discount-room-rates/edit/<int:pk>/', views.DiscountRoomRateUpdateView.as_view(), name='update_discount_room_rate'),
    path('discount-room-rates/delete/<int:pk>/', views.DiscountRoomRateDeleteView.as_view(), name='delete_discount_room_rate'),
]
