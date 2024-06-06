1) Room Rates Management
   
  1.1) List Room Rates
  
        URL: /api/room-rates/
        
        View: RoomRateListView
        
        Description: Displays a list of all existing room rates.
        
        Template: room_rate_list.html
        
  1.2) Add Room Rate
  
        URL: /api/room-rates/add/
        
        View: RoomRateCreateView
        
        Description: Provides a form to add a new room rate, including the room ID, room name, and default rate.
        
        Template: add_room_rate.html
        
  1.3) Edit Room Rate
        
        URL: /api/room-rates/edit/<int:pk>/
        
        View: RoomRateUpdateView
        
        Description: Provides a form to edit an existing room rate.
        
        Template: update_room_rate.html
        
  1.4) Delete Room Rate
        
        URL: /api/room-rates/delete/<int:pk>/
        
        View: RoomRateDeleteView
        
        Description: Confirms deletion of a room rate.
        
        Template: delete_room_rate.html
   
2) Overridden Room Rates Management
   
  2.1) List Overridden Room Rates
        
        URL: /api/overridden-room-rates/
        
        View: OverriddenRoomRateListView
        
        Description: Displays a list of overridden rates for each room rate.
        
        Template: overridden_room_rate_list.html
        
  2.2) Add Overridden Room Rate
        
        URL: /api/overridden-room-rates/add/
        
        View: OverriddenRoomRateCreateView
        
        Description: Provides a form to add overridden rates for specific dates.
        
        Template: add_overridden_room_rate.html
        
  2.3) Edit Overridden Room Rate
        
        URL: /api/overridden-room-rates/edit/<int:pk>/
        
        View: OverriddenRoomRateUpdateView
        
        Description: Provides a form to edit an overridden room rate.
        
        Template: update_overridden_room_rate.html
        
  2.4) Delete Overridden Room Rate
        
        URL: /api/overridden-room-rates/delete/<int:pk>/
        
        View: OverriddenRoomRateDeleteView
        
        Description: Confirms deletion of an overridden room rate.
        
        Template: delete_overridden_room_rate.html
   
3) Discounts Management

  3.1) List Discounts
        
        URL: /api/discounts/
        
        View: DiscountListView
        
        Description: Displays a list of all existing discounts.
        
        Template: discount_list.html
        
  3.2) Add Discount
        
        URL: /api/discounts/add/
        
        View: DiscountCreateView
        
        Description: Provides a form to add a new discount.
        
        Template: add_discount.html
        
  3.3) Edit Discount
        
        URL: /api/discounts/edit/<int:pk>/
        
        View: DiscountUpdateView
        
        Description: Provides a form to edit an existing discount.
        
        Template: update_discount.html
        
  3.4) Delete Discount
        
        URL: /api/discounts/delete/<int:pk>/
        
        View: DiscountDeleteView
        
        Description: Confirms deletion of a discount.
        
        Template: delete_discount.html
   
4) Filtered Room Rates
   
  4.1) Filtered Room Rates
        
        URL: /api/filtered-room-rates/
        
        View: FilteredRoomRateView
        
        Description: Filters and displays room rates based on room ID and date range, showing the lowest calculated rates considering discounts and overridden rates.
        
        Template: filtered_room_rate_list.html
   
5) Discount Room Rates Management
   
  5.1) List Discount Room Rates
        
        URL: /api/discount-room-rates/
        
        View: DiscountRoomRateListView
        
        Description: Displays a list of mappings between room rates and discounts.
        
        Template: discount_room_rate_list.html
        
  5.2) Add Discount Room Rate
        
        URL: /api/discount-room-rates/add/
        
        View: DiscountRoomRateCreateView
        
        Description: Provides a form to map discounts to room rates.
        
        Template: add_discount_room_rate.html
        
  5.3) Edit Discount Room Rate
        
        URL: /api/discount-room-rates/edit/<int:pk>/
        
        View: DiscountRoomRateUpdateView
        
        Description: Provides a form to edit a mapping between a room rate and a discount.
        
        Template: update_discount_room_rate.html
        
  5.4) Delete Discount Room Rate
        
        URL: /api/discount-room-rates/delete/<int:pk>/
        
        View: DiscountRoomRateDeleteView
        
        Description: Confirms deletion of a mapping between a room rate and a discount.
        
        Template: delete_discount_room_rate.html
