---
layout: defaults/page
permalink: index.html
narrow: true
title: Home
---

## Hello!

My name is Ella, and I am a computer science Ph.D. graduate from Clemson University's Zucker Family Graduate Center in North Charleston, South Carolina, with specialized expertise in informal learning methodologies, technical writing, digital content creation, and inclusive design. In 2018, I decided it was time to pursue a graduate degree in the evenings while maintaining my full-time industry position, and in 2021, I transitioned to my PhD program full-time. My research focuses on software development communities, live streaming software development, and software engineering education, with particular emphasis on creating accessible learning experiences for diverse learners through my work with the NSF-funded Educating Autistic Software Engineers (EdASE) program and research on developer communities.

I have created original and engaging learning experiences that improved knowledge retention and learner outcomes for undergraduate computer science students, while also developing user-focused documentation across my seven years of technical writing experience in both industry and academia. My published research demonstrates my commitment to understanding how technology can democratize access to computer science education, and my hands-on curriculum development experience shows my ability to translate research insights into real-world educational impact. My goal with my career is to bridge the gap between academic research and practical application in computer science education to create more inclusive and effective learning environments for all, regardless of whether they have access to formal education.

I am currently seeking a post-graduate career where I can apply my problem-solving skills, ability to manage projects, and technical communication expertise to promote education and learning endeavors. Outside of academic and research pursuits, I enjoy playing video games like Stardew Valley and rogue-like games like Slay the Spire and Balatro. I am also an artist who recently had her first solo show this past January 2025 and just received an honorable mention for another piece in my city's yearly arts fest.

### Recent Posts

{% for post in site.posts limit:2 %}
{% include components/post-card.html %}
{% endfor %}


