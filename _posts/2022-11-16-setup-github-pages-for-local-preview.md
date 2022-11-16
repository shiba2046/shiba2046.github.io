---
categories: jekyll github
layout: post
---

# Set up enviroment to preview locally

1. Install Ruby & Jekyll

    ```bash
    pacman -Syu ruby base-devel
    ruby update
    ruby install jekyll bundler
    ```

    Add to shell enviroment

    ```bash
    echo '# Install Ruby Gems to ~/gems' >> ~/.zshrc
    echo 'export GEM_HOME="$HOME/gems"' >> ~/.zshrc
    echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.zshrc
    source ~/.zshrc
    ```


2. Navigate to folder

    Create a new `Gemfile`

    ```
    bundle init
    ```

    Edit the `Gemfile` to add `github-pages` as a depenency.

    ```
    gem "github-pages", "~> GITHUB-PAGES-VERSION", group: :jekyll_plugins
    gem "webrick" # Add this to avoid the 'cannot load such file - webrick' error
    ```
    Replace `GITHUB-PAGES-VERSION` with the latest supported version of the github-pages gem. You can find this version here: "[Dependency versions](https://pages.github.com/versions/)."

    Currently `227`

3. Run `bundle install`

4. Serve Jekyll site locally.

    ```bash
    $ bundle exec jekyll serve --baseurl="" --livereload
    ```

5. Preview at `http://localhost:4000`

# Update the Github Pages gem

Run `bundle update github-pages`



# Reference Links

[Getting Started](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)

[Test Locally](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll)

[Jekyll](http://jekyllrb.com/docs/github-pages/)