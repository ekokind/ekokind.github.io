---
layout: defaults/project
permalink: /projects/
narrow: true
title: Projects
---
<div class="row">
  {% for project in site.projects %}
    <div class="col-md-6 mb-4">
      <div class="card h-100">
        {% if project.image %}
          <img src="{{ project.image | relative_url }}" 
               class="card-img-top" 
               alt="{{ project.image_alt | default: project.title }}"
               style="height: 200px; object-fit: cover;">
        {% endif %}
        <div class="card-body">
          <h5 class="card-title">
            <a href="{{ project.url | relative_url }}">{{ project.title }}</a>
          </h5>
          {% if project.description %}
            <p class="card-text">{{ project.description }}</p>
          {% endif %}
        </div>
      </div>
    </div>
  {% endfor %}
</div>