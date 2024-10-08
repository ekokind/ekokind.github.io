---
layout: defaults/page
permalink: index.html
narrow: true
title: Home
---

## Hello!

My name is Ella, and I am a PhD candidate at Clemson University's Zucker Family Graduate Center in Charleston, South Carolina, under Dr. Paige Rodeghero. In 2018, I decided it was time to pursue a graduate degree in the evenings while maintaining my full-time industry position. In 2020, the opportunity arose to switch from a master's to PhD program full-time -- so here I am! My research focuses on software development communities, live streaming software development, and software engineering education. My goal is to bridge the gap between academic research and practical application in software engineering education to create more inclusive and effective learning environments for all students, regardless if they have access to formal education. 

When not studying, writing, or attending class, I enjoy playing video games with a tight-knit group of individuals who have stayed together since my undergraduate days. When not playing a multiplayer game, I love Stardew Valley and any and all rogue-like deck builders (Slay the Spire, Balatro) and general rogue-like games (Death Must Die, Deep Rock Galactic Survivors). I also own a small laser-etching and rug tufting business that I run out of a spare room; it has been an absolute joy to share my art with others and motivate others to create. 


### Recent Posts

{% for post in site.posts limit:2 %}
{% include components/post-card.html %}
{% endfor %}


