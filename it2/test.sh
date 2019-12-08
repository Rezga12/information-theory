
# !/bin/bash

if [ "$#" -ne 10 ] && [ "$#" -ne 8 ] && [ "$#" -ne 6 ] ; then
    echo "Invalid Arguments"
    echo "Usage: script requires 3-5 Arguments: "
    echo "       -s Path to folder which contains following scripts with exact names:"
    echo "                   LZcompress.xxx and LZdecompress.xxx"
    echo "       -t Path to folder which contains public tests(where A,B,C,D folders are located)"
    echo "       -r Path to folder where we should put output for each test"
    echo "       -e Extension of your file (pass with dot exaple: .py)"
    echo "       -i Your Interpreter (no need if using executable)"
    echo "Example: ./check.sh -s src -t public_tests -r result -i python3 -e .py"
    
    exit
fi

# Read Command Line Arguments
POSITIONAL=()
while [[ $# -gt 0 ]]
do
    key="$1"
    case $key in
        -s)
            SCRIPT_FOLDER_PATH="$2"
            shift # past argument
            shift # past value
        ;;
        -t)
            TEST_FOLDER_PATH="$2"
            shift # past argument
            shift # past value
        ;;
        -r)
            RESULT_DIR_NAME="$2"
            shift # past argument
            shift # past value
        ;;
        -e)
            EXTENSION="$2"
            shift # past argument
            shift # past value
        ;;
        -i)
            INTERPRETER="$2"
            shift # past argument
            shift # past value
        ;;
        *)    # unknown option
            POSITIONAL+=("$1") # save it in an array for later
            shift # past argument
        ;;
    esac
done
set -- "${POSITIONAL[@]}" # restore positional parameters


[ -z "$SCRIPT_FOLDER_PATH" ] && printf "Script Folder path shouldn't be empty (use -s) \nexiting...\n" && exit
echo "Script Folder path:    $(pwd)/${SCRIPT_FOLDER_PATH}"

[ -z "$TEST_FOLDER_PATH" ] && printf "Test Folders path shouldn't be empty (use -t) \nexiting...\n" && exit
echo "Test Folders path:     $(pwd)/${
        pass
passTEST_FOLDER_PATH}"

[ -z "$RESULT_DIR_NAME" ] && printf "Result Directory Path shouldn't be empty (use -s) \nexiting...\n" && exit
echo "Result Directory Path: $(pwd)/${RESULT_DIR_NAME}"

echo "Extension:           ${EXTENSION}"
echo "Interpreter:           ${INTERPRETER}"

# delete Result Dir if exists
if [ ! -d "${RESULT_DIR_NAME}" ]; then
    mkdir ${RESULT_DIR_NAME}
fi

echo
echo "Starting Tests..."

compare_files(){
    SCRIPT_PATH=$1
    PTEST_DIR_NAME=$2
    RES_DIR_NAME=$3
    TNUM=$4
    
    FNAME=${SCRIPT_PATH%.*}
    FNAME=${FNAME##*/}
    
    for i in $(seq 1 $TNUM);
    do
        while [ ${#i} -lt 3 ]; do
            i=0$i
        done
        
        CURRENT_TEST=${PTEST_DIR_NAME}${i}.dat
        CURRENT_TEST_ANS=${PTEST_DIR_NAME}${i}.ans
        DEST_FILE_NAME=${RES_DIR_NAME}/${FNAME}_${i}.txt
        
        # launch your python script and calculate time
        START=$(date +%s.%N)
        eval ${INTERPRETER} ${SCRIPT_PATH} \"$CURRENT_TEST\" "${DEST_FILE_NAME}"
        END=$(date +%s.%N)
        DIFF=$(echo "$END - $START" | bc)
        
        # check if correct
        echo "Test ${i}: $(eval cmp --silent \"$CURRENT_TEST_ANS\" \"$DEST_FILE_NAME\" && echo "Success: files are same!" || echo "Failed: files are different")"
        echo "Compress Time: $DIFF seconds"
        echo
    done
}

run_test(){
    TNAME="$1"
    PROG_NAME="$2"
    TEST_SUB_FOLD="$3"
    TNUM="$4"
    
    echo
    echo "### Checking ${TNAME}"
    
    SCRIPT=${SCRIPT_FOLDER_PATH}/${PROG_NAME}
    TESTS=${TEST_FOLDER_PATH}/${TEST_SUB_FOLD}/
    RES_DIR=${RESULT_DIR_NAME}/${TEST_SUB_FOLD}/
    
    if [ ! -f "${SCRIPT}" ]; then
        echo "Script not found (Try using -e flag)"
        return
    fi
    
    if [ -d "${RES_DIR}" ]; then
        rm -rf ${RES_DIR}
    fi
    mkdir $RES_DIR
    eval compare_files \"${SCRIPT}\" \"${TESTS}\" \"${RES_DIR}\" "${TNUM}"
}
run_test "Compress" "LZcompress${EXTENSION}" "A" 5
run_test "Decompress" "LZdecompress${EXTENSION}" "B" 5