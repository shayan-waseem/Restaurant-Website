const menuOpenButton = document.querySelector("#menu-open-button");
const menuCloseButton = document.querySelector("#menu-close-button");

menuOpenButton.addEventListener("click",() =>{
    // toggle mobile menu visibility 
    document.body.classList.toggle("show-mobile-menu");
});

// close menu when the close button is clicked
menuOpenButton.addEventListener("click",() => menuOpenButton.click());

 
// Initialize Swiper 
const swiper = new Swiper('.slider-wrapper', {
    loop: true,
    spaceBetween: 25,
  
    // If we need pagination
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
      dynamicBullets: true,
    },
  
    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },

    // responsive breakpoints 
    breakpoints:{
        0:{
            slidesPerView: 1
        },
        768:{
            slidesPerView: 2
        },
        1024:{
            slidesPerView: 3
        },
    }

  });

  let cart = [];

function addToCart(itemName, itemPrice) {
    const item = { name: itemName, price: itemPrice };
    cart.push(item);
    updateCartDisplay();
}

function updateCartDisplay() {
    const cartItemsList = document.getElementById('cart-items-list');
    const cartTotal = document.getElementById('cart-total');
    
    // Clear current list
    cartItemsList.innerHTML = '';

    let total = 0;
    cart.forEach(item => {
        const listItem = document.createElement('li');
        listItem.textContent = `${item.name} - $${item.price.toFixed(2)}`;
        cartItemsList.appendChild(listItem);
        total += item.price;
    });

    cartTotal.textContent = `Total: $${total.toFixed(2)}`;

    // Show cart modal
    document.getElementById('cart-modal').style.display = 'block';
}

function closeCart() {
    document.getElementById('cart-modal').style.display = 'none';
}

function checkout() {
    alert("Proceeding to checkout...");
    cart = []; // Clear the cart
    updateCartDisplay();
    closeCart();
}
