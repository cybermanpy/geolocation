<footer class="footer">
		<section class="footer-content">
			<?php rewind_posts(); ?>
			<?php query_posts('cat=1') ?>
			<?php if ( have_posts() ): ?>
				<?php	while ( have_posts() ) : the_post(); ?>
					<?php the_excerpt();  ?>
				<?php endwhile; ?>
			<?php else: ?>

			<?php endif; ?>
		</section>
	</footer>
</body>
</html>