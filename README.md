# test-yagmail
Sample code to test using [yagmail](https://github.com/kootenpv/yagmail) to send an email.
PS: yagmail is a wrapper around [smtplib](https://docs.python.org/3.5/library/smtplib.html)

# Install
Pre-requisite: `sudo pip3 install pew`

Download and install
```
wget https://github.com/minerva22/test-yagmail/archive/master.zip -O test-yagmail.zip
unzip test-yagmail.zip
cd test-yagmail-master
pew new TEST_YAGMAIL
pip install yagmail pyyaml
```

# Usage
Copy `credentials.yml.dist` to `credentials.yml` and write username/password in it

Run
```
python test.py # by default sends to m.moawad@ffaprivatebank.com only
python test.py --emailTo s.akiki@ffaprivatebank.com m.moawad@ffaprivatebank.com
```
