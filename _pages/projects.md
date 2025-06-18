---
layout: defaults/projects
permalink: /projects/
narrow: true
title: Projects
---

<ul>
  {% for project in site.projects %}
    <li>
      <a href="{{ project.url | relative_url }}">{{ project.title }}</a>
      {% if project.description %}
        <p>{{ project.description }}</p>
      {% endif %}
    </li>
  {% endfor %}
</ul>