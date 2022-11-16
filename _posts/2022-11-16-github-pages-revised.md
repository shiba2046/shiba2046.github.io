---
layout: post
tilte: "Trying again at Github Pages"
date: 2022-11-16
categories: jekyll blogging
---

Now in 2022, let's pick up the pages and blog again.

# Date format

```html
<ul class="post-list">
  {% for post in site.posts %}
    <li>
        <div>
            {{ % assign date_format = site.minima.date_format | default: "%b %-d, %Y" % }}
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

```