---
layout: home
list_title: Read our latest posts
title: ""
---

# Notes 
A collection of my notes while using Linux [Link](notes/linux.md)
Dedicated notes on WSL [Link](notes/wsl.md)

Readme [Link](/README.md)

Working Diary [Link](working-diary.md)

Similarly, a place to put my notes while using Python, for easy reference [Link](notes/python.md)

# Blog Posts
<ul class="post-list">
  {% for post in site.posts %}
    <li>
        <div>
            { % assign date_format = site.minima.date_format | default: "%b %-d, %Y" % }
            
            <span class="post-meta">
                {{ post.date | date: date_format }}
            </span>
            <h3>
                <a class="post-link" href="{{ post.url | relative_url }}">
                    {{ post.title | escape}}
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