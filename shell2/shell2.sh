a=$(sed 's/,/ /g' | grep '172.30.1'| awk '{x=$1;y=$1+$8;z=1364803829.0;if(z<=y&&z>=x&&$4~/172.30.1/) print($5); if (z<=y&&z>=x&&$5~/172.30.1/) print($4)}')
for i in $a;do geoiplookup $i;done | sed 's/GeoIP Country Edition://'|sort -d | uniq -c | sort -nr





