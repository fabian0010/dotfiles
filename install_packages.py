import os, sys, subprocess, shlex, platform
from subprocess import DEVNULL

def run(*cmds, silent=False):
	for cmd in cmds:
		if not silent: print(">>>", cmd)
		try:
			if silent:
				subprocess.check_call(shlex.split(cmd), stdin=DEVNULL, stdout=DEVNULL, stderr=DEVNULL)
			else:
				subprocess.check_call(shlex.split(cmd))
			if len(cmds) == 1: return 0
		except subprocess.CalledProcessError as e:
			if len(cmds) == 1: return e.returncode

if platform.system() == "Darwin":
	# macos stuff
	if run("which brew", silent=True) != 0:
		print("Installing Homebrew")
		run('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')

# TODO find better way to have selective installs
if not "--skip-packages" in sys.argv:
	# install packages
	if run("which pacman", silent=True) == 0:
		packages = [
			"zsh",
			"neovim",
			"git",
			"gcc",
			"curl",

			"i3-gaps",
			"xfce4-terminal",
			"redshift"
		]
		run("sudo pacman --needed --noconfirm -S " + " ".join(packages))
	if run("which brew", silent=True) == 0:
		packages = [
			"neovim",
			"neofetch",
			"lolcat"
		]
		run("brew install " + " ".join(packages))
	else:
		print("No supported package manager found")
	# TODO apt, ..

if not "--skip-more-packages" in sys.argv:
	# install more packages
	if run("which yay", silent=True) == 0:
		packages = [
			"polybar",
			"visual-studio-code-bin",
			"discord",
			"spotify",
			"c-lolcat"
		]
		run("yay --needed --noconfirm -S " + " ".join(packages))
	if run("which brew", silent=True) == 0: # cask
		packages = [
			"visual-studio-code",
			"spotify"
		]
		run("brew cask install " + " ".join(packages))
	else:
		print("No supported alternative package manager found")
	# TODO snap, ...

if not "--skip-omzsh" in sys.argv:
	# oh-my-zsh
	run("sh -c \"$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)\"")

if not "--skip-chsh-zsh" in sys.argv:
	# chsh
	run("sh -c \"chsh -s $(which zsh)\"", "sh -c \"sudo chsh -s $(which zsh)\"")

if not "--skip-vscode" in sys.argv:
	# vscode extensions
	extensions = [
		"MS-vsliveshare.vsliveshare-pack",
		
		"ms-python.python",
		"bungcip.better-toml",

		"ms-vscode.cpptools",
		"vadimcn.vscode-lldb",

		"monokai.theme-monokai-pro-vscode"
	]
	for e in extensions:
		run("code --install-extension " + e)

# python stuff
if run("which conda", silent=True) != 0:
	if platform.system() == "Darwin":
		run("curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh --output miniconda.sh")
	elif platform.system() == "Linux":
		run("curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh --output miniconda.sh")

	run("bash ./miniconda.sh")
run("conda upgrade python")
run("conda create -y -n 2.7 python=2.7")
run("conda create -y -n 3.5 python=3.5")

pip_packages = [
	"better_exceptions",
	"HXMK"
]
run("pip install " + " ".join(pip_packages))