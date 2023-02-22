import ipaddress
import os
import argparse

IP_Ranges = []
count = 0
IPS = []

def arg_parse():
    '''
    Description:
        argparse creates a commandline and handles argument parsing
    
    Returns:
        dictionary
    '''
    # Vars
    args = {}
    
    # Create the parser
    parser = argparse.ArgumentParser(description="A script to split ip ranges into single ip addresses")
    
    # Add arguments
    parser.add_argument("-f",'--file', type=str, required=True, help="The file to read ranges from")
    
    # Parse the arguments
    args_parser = parser.parse_args()

    args["file"] = args_parser.file
    
    return args

def get_network_v4(cidr):
    return ipaddress.ip_network(cidr)
    
def main():
    global count

    args = arg_parse()

    outFile, outFileExtension = os.path.splitext(args["file"])
    with open(args["file"]) as handle_infile:
        IP_Ranges = handle_infile.readlines()

    for ip in IP_Ranges:
        print("Parsing {0}".format(ip.strip()))
        ip_range = ipaddress.IPv4Network(ip.strip(), False)
        [IPS.append(str(ip_net)+"\n") for ip_net in ip_range]

    outFileHandle = open(outFile+"_"+"singleIPs"+outFileExtension, "w")
    print("Wrote single IP file: {0}".format(outFile+"_"+"singleIPs"+outFileExtension))
    outFileHandle.writelines(IPS)
    outFileHandle.close()
    print("Total addresses for {0}: {1}".format(args["file"], len(IPS)))

if __name__ == "__main__":
    main()
