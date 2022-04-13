# NicPWNs' Log Parser

## Usage
```bash
python3 log-parser.py
```

## Behavior
Uses map reduce to analyze counts for key data points in web logs.

## Test
Test this with the included [AWS S3](s3.txt) and [Apache httpd](access.log) datasets.

## To Do
- [ ] Add CLI arguments to specify log file and log format before runtime.
- [ ] Add support for more web server log types. NGINX?
- [ ] Add support for log types other than web logs. Linux Secure?
- [ ] Add automatic recognition of key data fields using regex.
