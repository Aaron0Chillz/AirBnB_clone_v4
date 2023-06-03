$(document).ready(function() {
  var selectedAmenities = {};

  $('.amenities input[type="checkbox"]').change(function() {
    if (this.checked) {
      selectedAmenities[$(this).data('id')] = $(this).data('name');
    } else {
      delete selectedAmenities[$(this).data('id')];
    }

    var amenitiesList = Object.values(selectedAmenities).join(', ');
    $('.amenities h4').text(amenitiesList);
  });
});
