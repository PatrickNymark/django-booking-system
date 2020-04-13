$(document).on('click', '.sidebar-clear', function() {
      min = parseInt($('#hidden-min-price').val())
      max = parseInt($('#hidden-max-price').val())
      // clear price range
      $("#slider-range").slider({ values: [min, max]})
      $("#price-range").val($( "#slider-range" ).slider("values", 0) + ' DKK' + ' - ' + $( "#slider-range" ).slider("values", 1) + ' DKK');
    
      $(".completed-checkbox, .category-checkbox").each(function() {
        $(this).prop("checked", false)
      })

      $("#area-input").val("")
      $('#filter-form').submit()

  })

  // focus search field on load
  $(document).ready(function() {
    $('#id_search_value').focus()
    $('#id_search_value').val("")

    plumbing = $('#hidden-Plumbing').val()
    painting = $('#hidden-Painting').val()
    carpentry = $('#hidden-Carpentry').val()
    cleaning = $('#hidden-Cleaning').val()
    console.log(typeof $('#hidden-is-urgent').val())

    $('#plumbing').prop('checked', plumbing != undefined);
    $('#painting').prop('checked', painting != undefined);
    $('#carpentry').prop('checked', carpentry != undefined);
    $('#cleaning').prop('checked', cleaning != undefined);
    $('#is-urgent').prop('checked', $('#hidden-is-urgent').val() ==  'True');

  })

  $(document).on('submit', '#filter-form', function() {
    const input = $('<input />').attr('type', 'hidden')
      .attr('name', "search_value")
      .attr('value', $('#id_search_value').val())

    $(this).append(input)
  })

  // $(document).on('submit', '#search-form', function() {
    
  //   console.log(inputs)
    
  // })


  $( function() {
    min = parseInt($('#hidden-min-price').val())
    max = parseInt($('#hidden-max-price').val())

    current_min = parseInt($('#hidden-current-min-price').val())
    current_max = parseInt($('#hidden-current-max-price').val())

    $( "#slider-range" ).slider({
      range: true,
      min: min,
      max: max,
      values: [ current_min, current_max],
      slide: function( event, ui ) {
        $( "#price-range" ).val(ui.values[ 0 ] + ' DKK' + " - " + ui.values[ 1 ] + ' DKK' );
      }
    });
    $("#price-range").val($( "#slider-range" ).slider("values", 0) + ' DKK' + ' - ' + $( "#slider-range" ).slider("values", 1) + ' DKK');

  } );


  // // submit search on icon 
  // $(document).on('click', '#search-icon', function() {
  //   $('#search-form').submit()
  // })

  