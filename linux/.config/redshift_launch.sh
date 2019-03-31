
killall -q redshift

while pgrep -u $UID -x redshift >/dev/null; do sleep 0.33; done

redshift