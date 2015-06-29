<?php 

add_theme_support('post-thumbnails');

add_image_size('custom', 150, 150);

function register_my_menus(){
    register_nav_menus( 
        array(
            'menu-header'   => __( 'Menu header'),
            'menu-footer' => __( 'Menu footer')
        ) 
    );
}
add_action('init', 'register_my_menus');

function nav_class_filter( $var ) {
    return is_array($var) ? array_intersect($var, array('menu-item')) : '';
}
add_filter('nav_menu_css_class', 'nav_class_filter', 100, 1);

function search_register_sidebar(){
    register_sidebar(
        array(
            'id' => 'sidebar-search',
            'name' => 'Sidebar para buscar',
            'description' => 'Sidebar donde colocar un buscador',
            'before_widget' => '<div class="sidebar__item">',
            'after_widget' => '</div>',
            'before_title' => '<strong>',
            'after_title' => '</strong>'
            )
    );
}
add_action('widgets_init', 'search_register_sidebar');

/**
 * WooCommerce
 *
 * Unhook sidebar
 */
remove_action( 'woocommerce_sidebar', 'woocommerce_get_sidebar', 10);
add_filter( "woocommerce_catalog_orderby", "my_woocommerce_catalog_orderby", 20 );
remove_action( 'woocommerce_before_shop_loop', 'woocommerce_catalog_ordering', 30 );
// function my_woocommerce_catalog_orderby( $orderby ) {
//     unset($orderby["menu_order"]);  //Remove default sorting option.
//     unset($orderby["popularity"]);  //Remove popularity option.
//     unset($orderby["rating"]);      //Remove rating option.
//     unset($orderby["date"]);        //Remove newness option.
//     unset($orderby["price"]);       //Remove price: low to high option
//     unset($orderby["price-desc"]);  //Remove price: high to low option
//     return $orderby;
// }