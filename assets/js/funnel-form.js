(function ($) {
    "use strict";



    $(".next1").click(function () {
      $(".step1").addClass('d-none');
      $(".step2").removeClass('d-none');

    });
    // Binding next button on second step
    $(".next2").click(function () {
      $(".step2").addClass('d-none');
      $(".step3").removeClass('d-none');

    });
    // Binding back button on second step
    $(".next3").click(function () {
      $(".step3").addClass('d-none');
      $(".step4").removeClass('d-none');

    });
    // Binding back button on third step
    $(".back2").click(function () {
      $(".step2").addClass('d-none');
      $(".step1").removeClass('d-none');

    });
    $(".back3").click(function () {
      $(".step3").addClass('d-none')
      $(".step2").removeClass('d-none');

    });
    $(".back4").click(function () {
      $(".step4").addClass('d-none');
      $(".step3").removeClass('d-none');

    });
    $("#prodselect").change(function () {
      $('.product_add').remove()
      if ($(this).val() > 1) {
        var i;
        var prodnum = 2;



        for (i = $(this).val(); i > 1; i--) {
          var div = String.format('<div class="row product_add">\
                <div class="col-xl-6">\
                  <div class="form-group">\
                    <label for="prods">FE Product Option {0}</label>\
                    <input type="text" name="prod{0}" class="form-control" id="text" placeholder="" required>\
                  </div>\
                </div>\
                <div class="col-xl-2">\
                  <div class="form-group">\
                    <label for="prods">Product Price</label>\
                    <input type="number" min="0" step=".01" name="prod_price{0}" class="form-control" id="text" placeholder="" required>\
                  </div>\
                </div>\
                <div class="col-xl-2">\
                  <div class="form-group">\
                    <label for="prods">Product/Freight Cost</label>\
                    <input type="number"step="0.01" min="0" step=".01" name="prod_cost{0}" class="form-control" id="text" placeholder="" required>\
                  </div>\
                </div>\
                <div class="col-xl-2">\
                  <div class="form-group">\
                    <label for="prods">Est. Take Rate %</label>\
                    <input type="number" step="0.01" max="100" min="0" name="prod_tr{0}" class="form-control" id="text" placeholder="" required>\
                  </div>\
                </div>\
              </div>', prodnum);
          $(".feprods").append(div)
          prodnum++;
        }



      }
    });
    $("#bumpselect").change(function () {
      $('.bump_add').remove()
      if ($(this).val() > 1) {
        var i;
        var prodnum = 2;



        for (i = $(this).val(); i > 1; i--) {
          var div = String.format('<div class="row bump_add">\
                <div class="col-xl-6">\
                  <div class="form-group">\
                    <label for="prods">Order Bump Option {0}: Name</label>\
                    <input type="text" name="order_bump{0}" class="form-control" id="text" placeholder="" required>\
                  </div>\
                </div>\
                <div class="col-xl-2">\
                  <div class="form-group">\
                    <label for="prods">Product Price</label>\
                    <input type="number" step="0.01" min="0" name="ob_price{0}" class="form-control" id="text" placeholder="" required>\
                  </div>\
                </div>\
                <div class="col-xl-2">\
                  <div class="form-group">\
                    <label for="prods">Product/Freight Cost</label>\
                    <input type="number" min="0" step="0.01" name="ob_cost{0}" class="form-control" id="text" placeholder="" required>\
                  </div>\
                </div>\
                <div class="col-xl-2">\
                  <div class="form-group">\
                    <label for="prods">Est. Take Rate %</label>\
                    <input type="number" step="0.01" max="100" min="0" name="ob_tr{0}" class="form-control" id="text" placeholder="" required>\
                  </div>\
                </div>\
              </div>', prodnum);
          $(".orderbumps").append(div)
          prodnum++;
        }



      }
    });
    $("#upselect").change(function () {
      $('.up_add').remove()
      if ($(this).val() > 1) {
        var i;
        var prodnum = 2;



        for (i = $(this).val(); i > 1; i--) {
          var div = String.format('<div class="up_add"><div class="border-top my-3"></div><div class="row">          <div class="col-xl-6">            <div class="form-group">              <label for="prods">Upsell Option {0}: Name</label>              <input type="text" name="up_name{0}" class="form-control" id="upsellselect" placeholder="" required>            </div>          </div>          <div class="col-xl-2">            <div class="form-group">              <label for="prods">Total Sales</label>              <input type="number" step="0.01" min="0" name="total_revenue{0}"class="form-control" id="text" placeholder="" required>            </div>          </div>          <div class="col-xl-2">            <div class="form-group">              <label for="prods"># Products Offered</label>              <input type="number"  min="1" name="products_offered{0}" class="form-control" id="text" placeholder="" required>            </div>          </div>        </div>        <div class="row">          <div class="col-xl-3">            <div class="form-group">              <label  class="control-label" for="">Avg Cost of Products Offered:</label>              <input type="number" min="0" class="form-control" name=“up_cost_avg{0}" placeholder=""  required>              <div class="invalid-feedback">Please fill out this field.</div>            </div>          </div>          <div class="col-xl-3">            <div class="form-group">              <label  class="control-label" for="">Number of Sales:</label>              <input type="number" min="0" class="form-control" name=“total_orders{0}" placeholder=""  required>              <div class="invalid-feedback">Please fill out this field.</div>            </div>          </div>          <div class="col-xl-2">            <div class="form-group">              <label for="prods">Est. Take Rate %</label>              <input type="number" step="0.01" max="100" min="0" name="up_tr{0}" class="form-control" id="text" placeholder="" required>            </div>          </div>          <div class="col-xl-3">            <div class="form-group">              <label  class="control-label" for="">Unique Views:</label>              <input type="number" min="0" class="form-control" name=“upsell_traffic{0}" placeholder=""  required>              <div class="invalid-feedback">Please fill out this field.</div>            </div>          </div>        </div>',
            prodnum);
          $(".upsells").append(div)
          prodnum++;
        }



      }
    });
    String.format = function () {
      // The string containing the format items (e.g. "{0}")
      // will and always has to be the first argument.
      var theString = arguments[0];

      // start with the second argument (i = 1)
      for (var i = 1; i < arguments.length; i++) {
        // "gm" = RegEx options for Global search (more than one instance)
        // and for Multiline search
        var regEx = new RegExp("\\{" + (i - 1) + "\\}", "gm");
        theString = theString.replace(regEx, arguments[i]);
      }

      return theString;
    }
    $("#product-cost-form").submit(function (e) {

        e.preventDefault(); // avoid to execute the actual submit of the form.
        if (window.location.pathname == "/funnel/create") {
          var form = $(this);
          var url = '/funnel/create';

          $.ajax({
            type: "POST",
            url: url,
            data: form.serializeArray(), // serializes the form's elements.
            success: function (data) {
              alert(data); // show response from the php script.
              window.location = "/";
            }
          });
        } else {
          var form = $(this);
          var funnel_id = href.substring(this.href.lastIndexOf('/') + 1); 
          var url = '/funnel/update/' + funnel_id

          $.ajax({
            type: "GET",
            url: url,
            data: form.serializeArray(), // serializes the form's elements.
            success: function (data) {
              alert(data); // show response from the php script.
              window.location = "/";
            }

          });
        }
        /*** 
        $("#salespage").click(function () {
          $(this).attr('value', this.checked ? 1 : 0)
        });**/
      });
      
    })(jQuery);