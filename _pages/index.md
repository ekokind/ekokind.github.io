---
layout: defaults/page
permalink: index.html
narrow: true
title: Home
---

## Hello!

My name is Ella, and I am a computer science Ph.D. graduate from Clemson University's Zucker Family Graduate Center in Charleston, South Carolina. In 2018, I decided it was time to pursue a graduate degree in the evenings while maintaining my full-time industry position. In 2020, the opportunity arose to switch from a master's to PhD program full-time -- so here I am! My research focuses on software development communities, live streaming software development, and software engineering education. My goal is to bridge the gap between academic research and practical application in computer science education to create more inclusive and effective learning environments for all, regardless of whether they have access to formal education. I am currently seeking a post-graduate career where I can apply my problem-solving skills, ability to manage research projects, and use technical communication to promote education and learning endeavors. 

Outside of academic and research pursuits, I enjoy playing video games with a tight-knit group of individuals who have stayed together since my undergraduate days. When not playing a multiplayer game, I love Stardew Valley and any and all rogue-like deck builders (Slay the Spire, Balatro) and general rogue-like games (Death Must Die, Deep Rock Galactic Survivors). I am also an artist who owns a small laser-etching and rug tufting business that I run out of a spare room; it has been an absolute joy to share my art with others and motivate others to create. 


### Recent Posts

{% for post in site.posts limit:2 %}
{% include components/post-card.html %}
{% endfor %}


