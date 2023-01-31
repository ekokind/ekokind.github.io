---
layout: defaults/page
permalink: index.html
narrow: true
title: Home
---

## Hello!

My name is Ella and I am a PhD student at Clemson University's Zucker Family Gradute Center in Charleston, South Carolina under Dr. Paidge Rodeghero. In 2018, I decided it was time to pursue a graduate degree in the evenings while maintaining my full-time industry position. In 2020, the opportunity came up to switch from a masters to PhD program full time -- so here I am! 

When not studying, writing, or attending class, I enjoy playing video games with a tight-knit group of individuals that have stayed together since undergraduate days. Shout-out to all my Moira and Orisa mains in Overwatch! I also own a small laser-etching business that I run out of a spare room, it has been an absolute joy to share my work with others and motivate others to create. 


### Recent Posts

{% for post in site.posts limit:1 %}
{% include components/post-card.html %}
{% endfor %}


