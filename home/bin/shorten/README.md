This is a small program for my dotfiles, its only purpose is to shorten a path to make it more readable. I initially made a python script for that purpose but I thought starting up the python interpreter every time just for that is a bit overkill.

### How to use it
```sh
$ shorten [path/to/shorten] [path/parent]
```
For example
```sh
$ shorten ~/repos/somerepo/somedir ~/repos/

somerepo/somedir
```

This can be used in shell scripts, I use it for my customized oh-my-zh theme.

```sh
SOME=$(shorten $(pwd) ~/repos/)
```
