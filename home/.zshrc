PATH=~/bin:$PATH

export ZSH="~/.oh-my-zsh"
ZSH_THEME="agnoster_custom"
plugins=(git)

source $ZSH/oh-my-zsh.sh

export BETTER_EXCEPTIONS=1
export FORCE_COLOR=1

alias q="exit"
alias pacman="sudo pacman"
alias vim="nvim"
alias neofetch="neofetch | lolcat"

alias py="conda activate base && python"
alias py2="conda activate 2.7 && python"
alias py35="conda activate 3.5 && python"
alias pyr="conda activate base"