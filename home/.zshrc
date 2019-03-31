PATH=~/bin:~/miniconda3/bin:$PATH

export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="agnoster_custom"
plugins=(git)

source $ZSH/oh-my-zsh.sh

export BETTER_EXCEPTIONS=1
export FORCE_COLOR=1

alias q="exit"
alias pacman="sudo pacman"
alias neofetch="neofetch | lolcat"

alias vim="nvim"
alias ls="lsd"
alias la="lsd -a"

alias py="conda activate base && python"
alias py2="conda activate 2.7 && python"
alias py35="conda activate 3.5 && python"
alias pyr="conda activate base"

alias push="git push"
alias pull="git pull"

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('$HOME/miniconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
	eval "$__conda_setup"
else
	if [ -f "$HOME/miniconda3/etc/profile.d/conda.sh" ]; then
		. "$HOME/miniconda3/etc/profile.d/conda.sh"
	else
		export PATH="$HOME/miniconda3/bin:$PATH"
	fi
fi
unset __conda_setup
# <<< conda initialize <<<
