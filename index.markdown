---
layout: top
title: Anasayfa
section: Anasayfa
changefreq: monthly
---
{% unless site.disqus_shortname == null %}
<script type="text/javascript">
	var disqus_shortname = '{{ site.disqus_shortname }}';

	(function () {
		var s = document.createElement('script'); s.async = true;
		s.type = 'text/javascript';
		s.src = 'http://' + disqus_shortname + '.disqus.com/count.js';
		(document.getElementsByTagName('HEAD')[0] || document.getElementsByTagName('BODY')[0]).appendChild(s);
	}());
</script>
{% endunless %}

<img class='inset right' src='{{ site.base_url }}/images/eren_turkay.png' title='Eren Turkay' alt="Eren Turkay'in fotografi" width='150px' />
Merhaba
=======
Uzun zamandır aktif olarak özgür yazılım geliştiriyorum ve kullanıyorum. Eski
bir Pardus geliştiricisiyim. Amatör Telsizciyim _(DE TA1AET)_. Gömülü sistemler,
linux, bilgi güvenliği, ağ, kablosuz iletişim, programlama dilleri, işletim
sistemleri, afet ve acil durum haberleşmesi gibi konular ile ilgileniyorum.

Teknik konular dışında [salsa](http://en.wikipedia.org/wiki/Salsa_%28dance%29),
[bachata](http://en.wikipedia.org/wiki/Bachata_%28dance%29) ve
[merengue](http://en.wikipedia.org/wiki/Merengue_%28dance%29) gibi latin
dansları ile ilgileniyorum. Zaman buldukça tüplü dalış yapıyorum, 1 yıldız CMAS
lisansına sahibim.

+-- {: .section }
# Akademi
[İstanbul Bilgi Üniversitesi](http://www.bilgi.edu.tr/)'nde [Bilgisayar
Bilimleri](http://cs.bilgi.edu.tri/) ve İngilizce Öğretmenliği bölümlerinde çift
anadal yapmaktayım. 2015 yılında her iki bölümden de mezun olmayı umuyorum.

=--

+-- {: .section }
# Kod
Projeler ve açıklamalarına [projeler][projeler] sayfasından ulaşabilir, yazdığım
kodlara ise [GitHub][my_github] sayfamdan erişebilirsiniz.

[projeler]: {{ site.base_url }}/projeler
[my_github]: http://github.com/eren
=--


+-- {: .section }
# Detay
Hakkımda daha detaylı bilgiye ve şimdiye kadar yaptığım çalışmalara [bu
adresten]({{ site.base_url }}/hakkimda/) ulaşılabilir. Bununla birlikte iletişim
bilgileri için lütfen [bu bağlantıyı]({{ site.base_url }}/iletisim/) ziyaret
ediniz.
=--

{% comment %}
Son Girdiler
============

{% for post in site.posts limit:{{site.num_of_post_in_main}} %}
<div class="section list">
	<h1>{{ post.date | date: "%Y-%d-%m"}}</h1>
	<p class="line">
		<a class="title" href="{{ site.base_url }}{{ post.url }}">{{ post.title }}</a>
		<a class="comments" href="{{ site.base_url }}{{ post.url }}#disqus_thread" data-disqus-identifier="{{ post.id }}">View Comments</a>
	</p>
	<span class="excerpt">{{ post.excerpt | markdownify }}</span>
</div>
{% endfor %}

{% endcomment %}
