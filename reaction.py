import serial
import subprocess
import sys

# run the command and capture its output in real time
with subprocess.Popen(sys.argv[2:], stdout=subprocess.PIPE, bufsize=1,\
     universal_newlines=True) as process:
    for line in process.stdout:
        # check if the keyword is in the current line of output
        print(line, end="")
        line = line.strip()
        if line == "SUCCESS" or line == "FAILED":
            ser = serial.Serial(sys.argv[1], timeout=1)
            ser.write(bytes(line + '\r\n', 'utf-8'))
            ser.close()
