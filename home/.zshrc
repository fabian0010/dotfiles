# path
PATH=~/bin:$PATH

# oh-my-zsh
export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="agnoster_custom"
plugins=(git)
source $ZSH/oh-my-zsh.sh

# useful aliases
alias q="exit"
alias cls="clear"
alias pacman="sudo pacman"

alias vim="nvim"
alias ls="lsd"
alias la="lsd -a"

# git aliases
alias push="git push"
alias pull="git pull"
alias fetch="git fetch"
alias merge="git merge"

alias pushom="git push origin master"
alias pullom="git pull origin master"
alias pushod="git push origin dev"
alias pullod="git pull origin dev"

# python aliases
alias py="conda activate base && python"
alias py2="conda activate 2.7 && python"
alias py35="conda activate 3.5 && python"
alias pyr="conda activate base"

# misc aliases
alias neofetch="neofetch | lolcat"

# source .bash_profile
if [ ! -f ~/.bash_profile ]; then
	source ~/.bash_profile
fi

# source .bashrc
if [ ! -f ~/.bashrc ]; then
	source ~/.bashrc
fi
