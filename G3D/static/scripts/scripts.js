// função do botão load more.
document.querySelectorAll('.js-load-more').forEach(function(element) {
  element.addEventListener('click', function() {
    var el = this;
    el.innerHTML = 'Loading<span>.</span><span>.</span><span>.</span>';
    el.classList.add('load-more');
    setTimeout(onLoaded, 500);

    function onLoaded() {
      el.classList.remove('load-more');
      el.innerHTML = 'Load more';
      el.blur();
    }
  });
});





// função de menu que acompanha o scroll
function updateMenuStyle() {
  const navbar = document.getElementById("nav");
  const banner = document.querySelector("header");

  if (window.scrollY > 200) {
      navbar.classList.add("header-fixed");
      banner.style.height = "108vh"
  } else {
      navbar.classList.remove("header-fixed");
      banner.style.height = "100vh"
  }
}

window.addEventListener('scroll', updateMenuStyle);
window.addEventListener('load', updateMenuStyle);





// Ativação do Menu
const menuItems = document.querySelectorAll('.menu-item');
const logo = document.querySelector('.logo');

// Função para lidar com o clique em um item de menu
function handleMenuItemClick(event) {
    // Remove a classe "active" de todos os itens de menu
    menuItems.forEach(item => {
        item.classList.remove('active');
    });

    // Adiciona a classe "active" ao item de menu clicado
    event.currentTarget.classList.add('active');
}

// Adiciona um event listener de clique a cada item de menu
menuItems.forEach(item => {
    item.addEventListener('click', handleMenuItemClick);
});


logo.addEventListener('click', function(event) {
    menuItems.forEach(item => {
        item.classList.remove('active');
    });
});


