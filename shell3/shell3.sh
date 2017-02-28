foo(){
	for i in $@
	do 	echo $i
		s=$(find logs/$i.log)	
		cat $s 
	done	
     }
	for j in ./logs/10.0.3.2.log
	do 	t=$(<$j)
	done

a=$(foo $t)
b=$(foo $a)
c=$(foo $b)
d=$(foo $c)
echo $d | tr " " "\n" | sort | uniq
