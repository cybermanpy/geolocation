<?php get_header(); ?>
    <section class="content">
        <article>
            <?php rewind_posts(); ?>
            <?php query_posts('cat=6') ?>
            <?php if ( have_posts() ): ?>
                <?php   while ( have_posts() ) : the_post(); ?>
                <figure class="slider">
                    <?php the_post_thumbnail(); ?>
                </figure>
            <?php endwhile; ?>
            <?php else: ?>
            <?php endif; ?>
        </article>
         <article>
            <?php rewind_posts(); ?>
            <?php query_posts('cat=16') ?>
            <?php if ( have_posts() ): ?>
                <?php   while ( have_posts() ) : the_post(); ?>
                <figure class="slider">
                    <?php the_post_thumbnail(); ?>
                </figure>
            <?php endwhile; ?>
            <?php else: ?>
            <?php endif; ?>
        </article>
    </section>
<?php get_footer() ?>