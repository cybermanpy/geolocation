<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="<?php bloginfo('stylesheet_url') ?>">
    <title><?php bloginfo('name') ?></title>
</head>
<body>
    <header class="header">
        <section class="header-content">
            <figure class="img-header">
                <img src="<?php bloginfo('url') ?>/wp-content/themes/american/img/logo.png" alt="">
            </figure>
            <div class="sidebar">
                <?php 
                    dynamic_sidebar('sidebar-search')
                ?>
            </div>
            <?php 
                wp_nav_menu(
                    array(
                        'theme_location' => 'menu-header',
                        'container' => 'nav',
                        'container_class' => 'nav',
                        'menu_class' => 'nav__list'
                    )
                );
            ?>
        </section>
    </header>