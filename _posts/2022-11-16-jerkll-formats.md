---
# layout: post
# title: Template
categories: jekyll
# date: 2022-11-16
tags:

---


# Reference

[Reference](https://jekyllrb.com/docs/posts/)


#  List posts

```html
{% raw %}
<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">
        {{ post.title }}
      </a>
      - <time datetime="{{ post.date | date: "%Y-%m-%d" }}">{{ post.date | date_to_long_string }}</time>
    </li>
  {% endfor %}
</ul>
{% endraw %}
```

# Page variables

(http://jekyllrb.com/docs/variables/#page-variables)



# Date format

```html
{% raw %}
<ul class="post-list">
  {% for post in site.posts %}
    <li>
        <div>
            {% assign date_format = site.minima.date_format | default: "%b %-d, %Y" %}
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

{% endraw %}
```