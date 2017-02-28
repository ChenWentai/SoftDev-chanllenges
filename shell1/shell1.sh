ldd /bin/* | grep so | sed 's/\t//' | sed 's/=.*//' | sed 's/.0x.*//' | sed '/\//d' | sort -d | uniq -c | sort -nr

