## Hex On 
Command line utility 

prints the hex values of chars below each line of file 

can take input from files passed as arguments or from stdin 


### Make executable 

change permissions  

```chmod +x hexon.py```

remove extension and add to bin (change to system version tested on mac)

``` cp hexon.py hexon /usr/local/bin/hexon```



### file 
``` hexon test.txt othertest.txt```


### stdin 
``` echo Hello World | hexon```


Will print in the format:
```
   Hello World  
  |466662567662x|
  |85ccf07f2c40a|

