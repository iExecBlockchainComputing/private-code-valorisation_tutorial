import sys
import wget

def read_file(filepath):
    with open(filepath, "r") as f:
        return f.read()

def write_file(path, data):
    with open(path, "w+") as f:
        f.write(data)


def bubbleSort(arr, asc):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if asc:
                if arr[j] > arr[j+1] :
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                if arr[j] < arr[j+1] :
                    arr[j], arr[j+1] = arr[j+1], arr[j]

def main():
    # treat the args
    # /app/app.py https://inputfile_download_link.com asc/desc 
    args = sys.argv
    url = 'https://github.com/GregoireBailly/iExecTests/raw/master/data_cp_tuto.csv'
    if len(args) > 1:
        url = args[1]

    direction_asc = True
    if len(args) > 2 and args[2] == "desc":
        direction_asc = False

    
    # Download the input file
    wget.download(url, '/scone/inputs.csv')
    data = read_file("/scone/inputs.csv").split(",")
    
    #work on data
    sort = [float(i) for i in data]
 
    bubbleSort(sort, direction_asc)
    
    #write result
    result = str(sort)
    write_file("/scone/my-result.txt", result)