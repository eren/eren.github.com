---
layout: top
title: Home
section: Home
changefreq: always
link:
    - rel: canonical
      href: /

---
<img class='inset right' src='/images/eren_turkay.png' title='Eren Turkay' alt="Eren Turkay'in fotografi" width='150px' />
Merhaba
=======
İstanbul Bilgi Üniversitesi'nde İngilizce Öğretmenliği ve Bilgisayar Bilimleri bölümleri çift anadal öğrencisiyim. Uzun zamandır aktif olarak özgür yazılım geliştiriyorum ve kullanıyorum. Eski bir Pardus geliştiricisiyim. Amatör Telsizciyim, çağrı işaretim _TA1AET_. Gömülü sistemler, linux, bilgi güvenliği, ağ, kablosuz iletişim, programlama dilleri, işletim sistemleri, afet ve acil durum haberleşmesi gibi birçok konu ile ilgileniyorum.


Hakkımda daha detaylı bilgi için aşağıdaki ve yukarıdaki bağlantıları kullanabilirsiniz.


+-- {: .section }
# Academics
The main focus of my work at the moment is the completion of my studies at the
[Rochester Institute of Technology](http://www.rit.edu/) which I attend as a
full-time student. Studying computer science, I hope to complete my studies at
the end of February, 2012.
=--

+-- {: .section }
# Code
The vast majority of my work can be found at my
[GitHub](https://github.com/eatnumber1) page. What you can see below is the five
most recent projects I've worked on at GitHub.
+-- {: #github_{{ site.github_username }} }
Contacting GitHub...
{: #github_loading .loading }
<ul class="compact recent" id="github_list"/>
=--
=--

+-- {: .section }
# Blog
I periodically post to a programming blog entitled
_[Machinae Elegantiam](/machinae)_.

{% for post in site.categories.machinae limit: 3 %}
* [{{ post.title }}]({{ post.url }}){% if post.excerpt %}{: title="{{ post.excerpt }}"}{% endif %}
{: .compact .recent }
{% endfor %}
=--


{% comment %}
vim: ft=jekyll sw=4 ts=4 sts=4 tw=80
{% endcomment %}
