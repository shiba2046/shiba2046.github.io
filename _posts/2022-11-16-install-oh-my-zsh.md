---
categories: linux
---

# Centos manually install ZSH

Get latest source from [ZSH](https://www.zsh.org/pub/)

```bash
cd /usr/src
wget https://www.zsh.org/pub/zsh-5.9.tar.xz
xz -d zsh-5.9.tar.xz
tar xvf zsh-5.9.tar

./configure && make
sudo make install
```

This will install the new version of zsh to `/usr/local/bin/zsh` so that it does not interfere with the system zsh package.




# Install Oh My Zsh

```bash
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

# Install Powerlevel10k



0. Install nerd font
[Link](https://github.com/romkatv/powerlevel10k#meslo-nerd-font-patched-for-powerlevel10k)


1. Clone the repository

    ```bash
    git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
    ```

2. Set `ZSH_THEME="powerlevel10k/powerlevel10k"` in `~/.zshrc`.

3. Type `p10k configure` to config

[Powerlevel10k Homepage](https://github.com/romkatv/powerlevel10k)