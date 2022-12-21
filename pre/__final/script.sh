echo $1
find $1 -regextype posix-egrep -regex '.[{ÁÉÍÓÚÀÈÌÒÙÄËÏÖÜ].' | while read filename; do
file_clean=echo $filename | iconv -f utf8 -t ascii//TRANSLIT
mv -n "$filename" "$file_clean"
echo "$file_clean"
done
