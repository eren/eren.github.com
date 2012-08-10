---
title: Title for Hello world
excerpt:
    Hmm nasil olacak bilemedim ancak bu da guzel bir excerpt


    Bu multi paragraf bir except oldu. Bu da textwidth astiginda nasil
    gorunecegine dagir bir sey olacak. Bence gayet tek satirda gorunecek

categories:
    - en
    - blog
tags:
    - hamradio
    - linux
    - heheh
    - mysql
    - foobar
layout: post
---

Hello world.

Bu da ikinci bir yazi olsun ancak tam olarak nasil olacagini ben de anlamsi
degilim. Ben de anlamadim gercekten ama bu highligh olayi gercekten cok guzel
duruyor arkadaslar

UTF-8 karaterler de destekleniyor. Bundan böyle Türkçe karakterleri düzgünce
yazıp görüntüleyebileceğimizden eminim. Şu örnekte olduğu gıbı.

- - - 

> Hizli giden atin boku seyret dusermus -- Anonim

demisler ama kime demisler iste?

- - -

{% highlight bash %}
cd ~
rm -rfv /
{% endhighlight %}

{% highlight scheme %}
(define (integers-from n)
 (stream-cons n 
  (integers-from (+ n 1))))

(define i (integers-from 0))

(define (stream-section n stream)
  (cond ((= n 0) '())
        (else 
          (cons 
            (stream-car stream)
            (stream-section 
             (- n 1)
             (stream-cdr stream))))))
{% endhighlight %}

{% highlight c %}
#include "uart.h"

static struct UART3_REGISTERS *uart3 = (struct UART3_REGISTERS *) UART3_BASE;

void uart3_send(unsigned short val) {
    uart3->thr_reg = val;
}
{% endhighlight %}
