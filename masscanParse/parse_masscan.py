import re

# masscan command
# masscan -p80,443 --rate=1000 -iL ranges.txt | tee -a masscan_output.txt 

infile = "masscan_output.txt" # input filename
reg_ip = r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' # This is a very crappy regex and should be burned on site, but it works /shrug
reg_ports = r'[0-9]{1,2}/' # We extract both the port and the "/" example: '80/'. Thus, we have to strip it later

# Main loop
with open(infile) as intf:
    linenum = 0
    for line in intf:
        linenum += 1
        ips = re.findall(reg_ip,line)
        ports = re.findall(reg_ports,line)
        if len(ips) > 1:
            print("Too many ips on line: {0}".format(linenum))
            continue
        if len(ports) > 1:
            print("Too many port on line: {0}".format(linenum))
            continue
    
        print("{0}:{1}".format(ips[0], ports[0].strip("/")))