---
layout: main
title: From Bitbake Hello World to an Image
section: Anasayfa
---

* Table of Contents
{:toc}

From Bitbake Hello World to an Image
====================================
[OpenEmbedded][openembedded] and [Yocto][yoctoproject] are based on
[bitbake][bitbake] build system. In order to understand the structure of OE, it
is beneficial to have an understanding of bitbake to some degree along with the
tasks and classes defined in OE. This document will, hopefully, present the "big
picture" of creating an image using OpenEmbedded and Yocto. It will start from a
very basic bitbake project, explain the important concepts, delve into OE
classes, and finally show the image creation process at its basics.

Bitbake
=======
BitBake is, at its simplest, a tool for executing tasks and managing metadata
[\[1\]][bitbake-doc]. What bitbake does, basically, is to handle the tasks
defined in bitbake metadata (.bbclass, .bb), resolve their task dependencies,
put them in right order and run them. You can think of a task as a function that
can be set to run before or after another function (or task). A task can also
have additional flag(s) assigned besides the dependency information. Flags are
basically variables assigned to functions (tasks) that tell additional info
about them. Tasks and some of their flags interpreted by bitbake will be
explained shortly. Don't be confused and be patient.

{% comment %}
Explain the following questions in tasks section
- what is a task?
- How tasks are added, dependency resolution happens?
- What is a flag, how flags are defined?
- How these flags are used? E.g: cleandirs, dirs flag used by bitbake. Give
  reference to the code executed (bb/build.py)
{% endcomment %}

Before we begin our hello world example, it is important to note that what
bitbake parses is a bitbake metadata. Hence, it has its own syntax, variable
assignments, function definitions, etc. Do not confuse it with a regular shell
scripts, although bitbake syntax resembles to them. Before proceeding, please
read [metadata section][bitbake-metadata] of [bitbake user
manual][bitbake-user-manual].

Obtaining Bitbake
-----------------
Let's obtain the bitbake source and extract it. As of this date, the latest
bitbake release is 1.16.0.

{% highlight bash linenos %}
wget http://git.openembedded.org/bitbake/snapshot/bitbake-1.16.0.tar.bz2
tar xvf bitbake-1.16.0.tar.bz2
cd bitbake-1.16.0
{% endhighlight %}

Instead of installing bitbake, we will run it in its build directory. Now, build
bitbake:

{% highlight bash linenos %}
# FIXME: how to disable xml doc generation? It takes a little time for this doc.
python setup.py build
export PYTHONPATH=`pwd`/build/lib
{% endhighlight %}

Now that we have built our bitbake, let's run it.

{% highlight bash linenos %}
./bin/bitbake --version
BitBake Build Tool Core version 1.16.0, bitbake version 1.16.0
{% endhighlight %}

We are now ready to create our helloworld bitbake project.

Hello World Project
-------------------
Starting with the fundamentals, we will gradually evolve and see how bitbake
works by playing with it. In this part, we will cover what a task is, how it is
defined, how a task can be overwritten, what is a flag, and how a flag is used
by bitbake. With these informations in mind, we will also see how all of these
can come together to form a useful build system that creates embedded linux
images. After we have covered the concepts written above, we will delve into
OpenEmbedded code and see the ideas implemented.

*NOTE: This part is written with the help of the information in
[emails][bitbake-helloworld-email] sent to yocto project mailing list.*

{% comment %}
- after explaining hello world bitbake and before delving into OE code, give the
  build diagram in getting started. Say it's not enough to understand the code,
  and start explaining.

{% endcomment %}


[openembedded]: http://localhost/
[yoctoproject]: http://localhost/
[bitbake]: http://localhost/
[bitbake-doc]: http://localhost/
[bitbake-metadata]: http://docs.openembedded.org/bitbake/html/ch02.html
[bitbake-user-manual]: http://docs.openembedded.org/bitbake/html/
[bitbake-helloworld-email]: http://www.mail-archive.com/yocto@yoctoproject.org/msg09379.html
