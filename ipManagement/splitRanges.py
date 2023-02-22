import ipaddress
import os
import argparse



IPS = []
file_counter = 1
count = 0

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
    parser = argparse.ArgumentParser(description="A script to split ip ranges into blocks of a provided size")
    
    # Add arguments
    parser.add_argument("-f",'--file', type=str, required=True, help="The file to read ranges from")
    parser.add_argument("-s",'--size', type=int, required=True, help="The size of each ip block")
    
    # Parse the arguments
    args_parser = parser.parse_args()

    args["file"] = args_parser.file
    args["size"] = args_parser.size
    
    return args


def get_ip_range(cidr):
    return ipaddress.ip_network(cidr, False)
    
def main():
    global count
    global file_counter

    args = arg_parse()

    IPLimit = args["size"]
    outFile, outFileExtension = os.path.splitext(args["file"])

    localIPs = []
    with open(args["file"]) as handle_infile:
        IPS = handle_infile.readlines()

    for ip in IPS:
        localIPs.append(ip)
        count += get_ip_range(ip.strip()).num_addresses
        if count >= IPLimit:
            outFileHandle = open(outFile+"_"+str(file_counter)+outFileExtension, "w")
            print("Writing file: {0}".format(outFile+"_"+str(file_counter)+outFileExtension))
            outFileHandle.writelines(localIPs)
            outFileHandle.close()
            file_counter += 1
            localIPs = []
            count = 0

if __name__ == "__main__":
    main()
