---
layout: blog-main
title: Arşiv
section: Arsiv

---
{% for post in site.posts %}
<div class="section list">
	<h1>{{ post.date | date_to_string }}</h1>
	<p class="line">
		<a class="title" href="{{ site.base_url }}{{ post.url }}">{{ post.title }}</a>
		<a class="comments" href="{{ site.base_url }}{{ post.url }}#disqus_thread" data-disqus-identifier="{{ post.id }}">View Comments</a>
	</p>
	<span class="excerpt">{{ post.excerpt | markdownify }}</span>
</div>
{% endfor %}
