
c = 0

while IFS= read -r f; do
    if [[ -e $2/$f ]]; then
        #printf '%s exists in %s\n' "$f" "$2"
        continue
    else
        printf '%s is missing in %s\n' "$f" "$2"
        #exit 1
        let c++
    fi
echo $c
done < "$1"