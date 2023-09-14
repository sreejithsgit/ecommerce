{/* <script>
function addToCart(product_id) {
      $.ajax({
        type: 'POST',
        url: `/shop/add_to_cart/${product_id}/`,
        dataType: 'json',
        success: function(response) {
          if (response.success) {
            $('#cart-count').text(response.cart_count);
          }
        },
        error: function(error) {
          console.error(error);
        }
      });
    }
  
function removeFromCart(cart_item_id) {
      $.ajax({
        type: 'POST',
        url: `/shop/remove_from_cart/${cart_item_id}/`,
        dataType: 'json',
        success: function(response) {
          if (response.success) {
            $('#cart-count').text(response.cart_count);
            $('#cart-item-' + cart_item_id).remove();
          }
        },
        error: function(error) {
          console.error(error);
        }
      });
    }

function addToCart(product_id) {
    $.ajax({
      type: 'POST',
      url: `/shop/add_to_cart/${product_id}/`,
      dataType: 'json',
      success: function(response) {
        if (response.success) {
          $('#cart-count').text(response.cart_count);
        }
      },
      error: function(error) {
        console.error(error);
      }
    });
  }

function removeFromCart(cart_item_id) {
    $.ajax({
      type: 'POST',
      url: `/shop/remove_from_cart/${cart_item_id}/`,
      dataType: 'json',
      success: function(response) {
        if (response.success) {
          $('#cart-count').text(response.cart_count);
          $('#cart-item-' + cart_item_id).remove();
        }
      },
      error: function(error) {
        console.error(error);
      }
    });
  }
</script>

  </script> */}