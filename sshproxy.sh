

# Help menu
print_help () {
	echo "loop.sh - SSH proxy automation script with auto looping"
	echo "Arguments:"
	echo ""
	echo "-d    The hostname to connect to with ssh"
	echo "-p    The local port to start the proxy on"
	echo "-u    Username to connect to ssh"
	echo "-i    The key to use with ssh"
	echo "-h    This help menu"
	echo ""
}


# Initialise option flag with a false value
HELP=false

# Argument parsing
while getopts ':d:p:i:u:h' 'flag'
do
    case ${flag} in
        'd') HOST=${OPTARG};;
        'p') PORT=${OPTARG};;
	'u') USERNAME=${OPTARG};;
	'i') IDRSA=${OPTARG};;
        'h') HELP=true;;
    esac
done

if [ "$HELP" = true ]
then
	print_help
	exit
fi

if [ -z "$HOST" ]
then
	echo "Error: Missing -d flag"
	print_help
	exit
fi

if [ -z "$PORT" ]
then
	PORT=8089
else
	re='^[0-9]+$'
	if ! [[ $PORT =~ $re ]] ;
	then
		echo "Error: -p, Port not a number"
		exit
	fi

fi

if [ -z "$USERNAME" ]
then
	USERNAME="root"
fi

if [ -z "$IDRSA" ]
then
	IDRSA="id_rsa"
fi


# Start the proxy
echo "Starting dynamic proxy"
echo "Attempting ssh proxy on port: $PORT"
while $true;
do
	ssh -C -N -D "$PORT" "$USERNAME"@"$HOST" -i "$IDRSA"
	echo "Connection failed..."
	echo "Looping..."
	sleep 2
done


# Help menu
print_help () {
	echo "loop.sh - SSH proxy automation script with auto looping"
	echo "Arguments:"
	echo ""
	echo "-d    The hostname to connect to with ssh"
	echo "-p    The local port to start the proxy on"
	echo "-u    Username to connect to ssh"
	echo "-i    The key to use with ssh"
	echo "-h    This help menu"
	echo ""
}


# Initialise option flag with a false value
HELP=false

# Argument parsing
while getopts ':d:p:i:u:h' 'flag'
do
    case ${flag} in
        'd') HOST=${OPTARG};;
        'p') PORT=${OPTARG};;
	'u') USERNAME=${OPTARG};;
	'i') IDRSA=${OPTARG};;
        'h') HELP=true;;
    esac
done

if [ "$HELP" = true ]
then
	print_help
	exit
fi

if [ -z "$HOST" ]
then
	echo "Error: Missing -d flag"
	print_help
	exit
fi

if [ -z "$PORT" ]
then
	PORT=8089
else
	re='^[0-9]+$'
	if ! [[ $PORT =~ $re ]] ;
	then
		echo "Error: -p, Port not a number"
		exit
	fi

fi

if [ -z "$USERNAME" ]
then
	USERNAME="root"
fi

if [ -z "$IDRSA" ]
then
	IDRSA="id_rsa"
fi


# Start the proxy
echo "Starting dynamic proxy"
echo "Attempting ssh proxy on port: $PORT"
while $true;
do
	ssh -C -N -D "$PORT" "$USERNAME"@"$HOST" -i "$IDRSA"
	echo "Connection failed..."
	echo "Looping..."
	sleep 2
done

