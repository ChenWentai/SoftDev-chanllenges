t="a b c d d c a c e f f a"
a=$(echo $t | tr " " "\n" | sort | uniq)
echo $a | tr " " "\n"
