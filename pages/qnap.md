---
layout: default
title: "QNAP笔记"
permalink: /qnap/
---

# Hardware

## CPU

- Model: J3455 
- Apollo Lake
- Q3'16
- 14nm
- 4 Core 4 Threads
- Base 1.5GHz, Boost 2.3GHz

# Links
[为 Container Station 更换镜像](http://einverne.github.io/post/2020/01/qnap-docker-registry-mirror.html)
[替换默认 shell 为 zsh](http://einverne.github.io/post/2019/05/qnap-change-default-login-shell-to-zsh.html)


# Posts
<ul class="post-list">
  {% for post in site.posts | where: 'cateo %}
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

# cd into QPKG package folder
```
cd `getcfg QDK Install_Path -f /etc/config/qpkg.conf` 
```

# Clash config
```bash
#!/bin/sh
curl https://sub.chiba.bar/link/clash -o clash
#sed -i s/127\.0\.0\.1:9090/0\.0\.0\.0:9090/ clash
#sed -i s/allow-lan:\ false/allow-lan:\ true/ clash
#ed -i s/dns\:/external-ui:\ \"\\/yacd\"\\ndns\:/ clash # Add webui


#docker restart clash
#sleep 10

curl localhost:7090/configs -X PUT -d '{"path": "/root/.config/clash/config.yaml"}'

# curl localhost:7090/proxies/Proxy -X PUT -d '{"name":"By Speed"}'
# curl localhost:7090/proxies/Domestic -X PUT -d '{"name":"DIRECT"}'
# curl localhost:7090/proxies/Others -X PUT -d '{"name":"DIRECT"}'
# curl localhost:7090/proxies/AdBlock -X PUT -d '{"name":"REJECT"}'
# curl localhost:7090/proxies/AsianTV -X PUT -d '{"name":"DIRECT"}'
# curl localhost:7090/proxies/GlobalTV -X PUT -d '{"name":"Proxy"}'
# curl localhost:7090/proxies/Telegram -X PUT -d '{"name":"Proxy"}'
# curl localhost:7090/proxies/Speedtest -X PUT -d '{"name":"DIRECT"}'
# curl localhost:7090/proxies/Microsoft -X PUT -d '{"name":"DIRECT"}'
```


