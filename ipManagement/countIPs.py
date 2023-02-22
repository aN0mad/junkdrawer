import ipaddress
import argparse

IPS = []
count = 0

def get_ip_range(cidr):
    return ipaddress.ip_network(cidr)

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
    parser = argparse.ArgumentParser(description="A script to count the number of single IP addresses")
    
    # Add arguments
    parser.add_argument("-f",'--file', type=str, required=True, help="The file to read ranges from")
    
    # Parse the arguments
    args_parser = parser.parse_args()

    args["file"] = args_parser.file
    
    return args

def main():
    global count

    args = arg_parse()

    with open(args["file"]) as handle_infile:
        IPS = handle_infile.readlines()

    for ip in IPS:
        count += get_ip_range(ip.strip()).num_addresses
    
    print("Total addresses for {0}: {1}".format(args["file"],count))

if __name__ == "__main__":
    main()
