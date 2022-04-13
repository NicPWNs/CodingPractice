#!/usr/bin/env python3
# Author: Nic Jones (NicPWNs)
# log-parser.py

print("\n#################################################################")
print("# Welcome to NicPWNs' Log Parser. Map Reduce Common Log Formats #")
print("#################################################################\n")

# Read in log file lines
logPath = str(input("Enter the full or relative log file path to analyze [access.log]: ") or "access.log")
logType = str(input("Enter the type of log file [httpd]: ") or "httpd")
logFile = open(logPath, 'r')
logLines = logFile.readlines()

# List of supported log types
logTypes = ["s3", "httpd"]

# Data model for column/index numbers of key data
logDataModel = {
    "s3_source":4,
    "s3_request":9,
    "s3_status": 12,
    "httpd_source":0,
    "httpd_request":5,
    "httpd_status": 8,
}

# Initialize main lists
source = []
request = []
status = []

# Check for supported log type input
if logType not in logTypes:
    print("Log type not supported! Currently suppored: s3, httpd")
    exit()

# Create lists of key data
for line in logLines:
   source.append(line.split(' ')[logDataModel[logType + "_source"]])
   request.append(line.split(' ')[logDataModel[logType + "_request"]])
   status.append(line.split(' ')[logDataModel[logType + "_status"]])

# Create unique sets of data (MAP)
sourceSet = sorted(set(source))
requestSet = sorted(set(request))
statusSet = sorted(set(status))

# Initialize dictionary from data sets
sourceDict = dict.fromkeys(sourceSet, 0)
requestDict = dict.fromkeys(requestSet, 0)
statusDict = dict.fromkeys(statusSet, 0)

# Count data occurrences and add to dictionaries (REDUCE)
for occurrence in sourceSet:
    sourceDict[occurrence] = source.count(occurrence)
for occurrence in requestSet:
    requestDict[occurrence] = request.count(occurrence)
for occurrence in statusSet:
    statusDict[occurrence] = status.count(occurrence)

# Output map reduced data
print("\n.....Processing.....")
print("\nAnalysis of source IP addresses in log file:")
for key, value in sourceDict.items():
    print(key, ':', value)
print("\nAnalysis of request types in log file:")
for key, value in requestDict.items():
    print(key, ':', value)
print("\nAnalysis of status codes in log file:")
for key, value in statusDict.items():
    print(key, ':', value)