# ipManagement
Manage and manipulate IP ranges

## Scripts
### countIPs.py
A script to count the number of single IP addresses from a list of ranges

#### Help
```
# python countIPs.py -h
usage: countIPs.py [-h] -f FILE

A script to count the number of single IP addresses

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  The file to read ranges from
```

#### Input file
ranges.txt
```
192.168.1.0/24
192.168.5.0/27
172.16.20.0/30
10.0.1.0/29
```

#### Usage
Count all IPs within the range file
```
# python countIPs.py -f ranges.txt 
Total addresses for ranges.txt: 300
```

### singleIPs.py
A script to split ip ranges into single ip addresses from a list of ranges

#### Help
```
# python singleIPs.py -h
usage: singleIPs.py [-h] -f FILE

A script to split ip ranges into single ip addresses

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  The file to read ranges fro
```

#### Input file
ranges.txt
```
192.168.1.0/24
192.168.5.0/27
172.16.20.0/30
10.0.1.0/29
```

#### Usage
Convert all ranges to single IP addresses
```
# python singleIPs.py -f ranges.txt 
Parsing 192.168.1.0/24
Parsing 192.168.5.0/27
Parsing 172.16.20.0/30
Parsing 10.0.1.0/29
Wrote single IP file: ranges_singleIPs.txt
Total addresses for ranges.txt: 300
```

##### Output
File: ranges_singleIPs.txt
```192.168.1.0
192.168.1.1
192.168.1.2
192.168.1.3
192.168.1.4
192.168.1.5
192.168.1.6
...
192.168.5.0
192.168.5.1
192.168.5.2
...
172.16.20.0
172.16.20.1
172.16.20.2
172.16.20.3
10.0.1.0
10.0.1.1
10.0.1.2
10.0.1.3
10.0.1.4
10.0.1.5
```

### splitRanges.py
A script to split ip ranges into blocks of a provided size

#### Help
```
# python splitRanges.py -h
usage: splitRanges.py [-h] -f FILE -s SIZE

A script to split ip ranges into blocks of a provided size

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  The file to read ranges from
  -s SIZE, --size SIZE  The size of each ip block
```

#### Input
File of single IP ranges seperated by newlines

#### Usage
```
# python splitRanges.py -f ranges_singleIPs.txt -s 100
Writing file: ranges_singleIPs_1.txt
Writing file: ranges_singleIPs_2.txt
Writing file: ranges_singleIPs_3.txt
```