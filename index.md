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
<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url | prepend: site.baseurl }}">{{ post.date }} - {{ post.title }}</a>
    </li>
  {% endfor %}
</ul>