---
# layout: home
# list_title: Read our latest posts
title: ""
layout: page
# menubar_toc: true
# toc_title: 目录
show_sidebar: true
---

# Notes 


# Blog Posts

<ul class="post-list">
  {% for post in site.posts %}
    <li>
        <div>
            
            {% assign date_format = site.minima.date_format | default: "%b %-d, %Y" %}
            
            
            <h3>
                <a class="post-link" href="{{ post.url | relative_url }}">
                    {{ post.title | escape}}
                
                <span class="post-meta">
                    {{ post.date | date: date_format }}
                </span>
                </a>
            </h3>
        </div>
        {% if post.featured_image %}
            <div class="featured-image">
            <img
                src="{{ '/assets/' | append: post.featured_image | relative_url }}"
            />
            </div>
        {% endif %}

    </li>
  {% endfor %}
</ul>