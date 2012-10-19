---
layout: main
title: Projeler
section: Anasayfa
---

Projeler
========
+-- {: .section }
# [SOS](http://github.com/eren/sos/)
**S**imple **O**perating **S**ystem. İşletim sistemi temellerini öğrenmek
amacıyla başlattığım bir proje.

Texas Instruments [OMAP3530][omap3530] SoC'ye sahip ve
içerisinde ARMv7 mimarisi olan [BeagleBoard][beagleboard] üzerinde
geliştirme yapıyorum. Şu anda emekleme aşamasında olmakla birlikte çok temel bir
çekirdeğe sahip olup, UART3 üzerinden veri haberleşmesi yapabilmekte. İlerleyen
zamanlarda kesmeleri *(interrupt)* devreye sokup *memory management unit*'i
aktif hale getirerek *process* ve *thread* implement etmeyi planlıyorum.
Böylelikle temel bir multi-process işletim sistemine sahip olmayı
amaçlamaktayım.

[omap3530]: http://www.ti.com/product/omap3530
[beagleboard]: http://beagleboard.org/ 

=--

+-- {: .section }
# [python-svxlinkconf](http://github.com/eren/python-svxlinkconf/)
Amatör Telsizciler tarafından kullanılan yazılım tabanlı röle kontrol uygulaması
olan [svxlink][svx] için ayar dosyasını kolay bir biçimde düzenlemeye yarayan python
kütüphanesi.

Bu kütüphane ile ayar dosyasındaki biçim ile uğraşılmaksızın python ile soyut bir
biçimde ayar dosyaları yazılabiliyor. Böylelikle, arkaplanda svxlink kullanan
uygulama geliştiricileri kolay bir biçimde ayar dosyalarını yazıp,
güncelleyebiliyorlar.

=--

+-- {: .section }
# [django-svxlinkconf](http://github.com/eren/django-svxlinkconf/)
Django kullanılarak hazırlanmış olan, [svxlink][svx] röle kontrol uygulamasının web arayüzü.

Svxlink'in ayar dosyaları ile alt seviyede uğraşmayı gerektirmeyen, kolay bir
biçimde ayar yapılabilmesini sağlayan bu arayüz ile ses alıcı ve verici
istasyonları rahatlıkla eklenerek svxlink ayarları yapılabiliyor. Böylelikle,
hem son kullanıcı açısından hızlı, hem de güvenilir bir biçimde röle kontrol
edilebiliyor.

[svx]: http://svxlink.sourceforge.net

=--

{% comment %}
vim: ft=jekyll sw=4 ts=4 sts=4 tw=80
{% endcomment %}
