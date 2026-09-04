![](/assets/header.png)

**Add to path** is a simple and lightweight script enabling you to add things to `$PATH` with just one command. I created this app mostly due to the fact that I always forget how to add things to `$PATH` and end up googling (shame yep yep). Anyway, this very thing made me write this app in like half an hour and felt like sharing it here - maybe some of you have same problem, or just don't enjoy opening your `.rc` file everytime. 💚

> [!CAUTION]
> **Add to path** supports only **[BASH](https://www.gnu.org/software/bash/)** and **[ZSH](https://zsh.sourceforge.io/)** shells.<br>And likely won't ever support any other, since these are only two popular ones.

<br><br>

# 🌿 Installation

To install this script you need to have **[UV](https://github.com/astral-sh/uv)**. If you need help installing it refer to this page: **https://docs.astral.sh/uv/getting-started/installation**.

If you have installed **UV** you can now proceed to installing this very executable. To do this simply run:

```bash
uv tool install git+https://github.com/TaXi0k/add_to_path.git
```

And that's it.

### 🍏 Alternative: manual download

If you for some reason don't feel like installing straight from GitHub you can clone this repository and install it manually. To do this run:

```bash
git clone https://github.com/TaXi0k/add_to_path
cd add_to_path
uv tool install .
```

<br><br>

# 🍃 Usage

To use this app simply run:
```bash
adtp <path>
```
or
```bash
add_to_path <path>
```
both versions are perfectly valid and do the same thing.

> [!NOTE]
> After adding something to `$PATH`, your shell won’t refresh automatically.<br>You need to either restart your terminal or run `source ~/.bashrc` / `source ~/.zshrc`. 🌿
>
> This tool doesn’t do that for you - **on purpose**. Injecting shell functions into your rc file felt a bit too intrusive, so I decided not to touch your config more than absolutely necessary.
>
> If you *want* automatic refresh, you can add this one small function to your rc file:
> ```bash
> adtp() {
>   command adtp "$1"
>   source ~/.bashrc # or ~/.zshrc
> }
> ```
> Now running `adtp <path>` will **automatically** reload your shell config.

<br><br>

# 🍀 How it works and FAQ

* **💚 Does this modify my rc file?**<br>Yes, this script adds literal two lines to your rc file - to be precise it adds the following string to end of your rc file: `"\n# Created by add_to_path\nsource ~/.config/add_to_path/paths"`. If you want to investigate further check `link_in_rc_file(shell)` function in [main.py](/main.py).<br><br>
* **💚 Is this safe?**<br>Well yes, it is - I created this app to use it myself (exacly what creator of malware would say). It can't damage your rc file - it opens it in **append** and **read** modes only, never in **write** mode.<br><br>
* **💚 What if I use fish or any other shell?**<br>Then you can't use this script. I'm not planning to support it soon nor ever.<br><br>
* **💚 Does it work on macOS?**<br>I haven't tried it but it technically should, since it uses **BASH** / **ZSH**.<br><br>
* **💚 How does it work?**
  * **It doesn't modify any crucial system files (well any system files)**<br>Ok I kinda lied. As I said it appends two lines to rc file, but I promise that's it.
  * **All paths are stored in a specific file**<br>All paths added to `$PATH` using this app are stored in `~/.config/add_to_path/paths` file. That file is sourced inside your rc file to avoid cluttering your precious rc.
  * **I think there's nothing more**<br>This app just automates something you otherwise have to do manually and from my experience takes a bit of time - and to me is unpleasant.

<br><br>

# 🦖 Credits

To me, I did this. I don't know why I even wrote this very line xd.

<br><br>

# 📗 License

[to be added after pushing to GitHub]