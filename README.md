# ipchecker - multi

Periodically pings a list of configured DNS names, checking each for an IP address reassignment.
Emails the before and after IP addresses to an interested party when a target DNS name's IP address changes.
All files reside in a single flat directory. 

## Emailed notification

Governed by a template in `props.py`. It should work unchanged. You could alter it to suit 
after you see the script operate for you.

---

From: IP Checker &lt;ipchecker@hostsite.org&gt;

To: Interested Party &lt;sombody@somesite.org&gt;

Subject: www.somesite.com IP Tracking

<table>
<tr><th>DNS name	</th><td> www.somesite.com</td></tr>
<tr><th>IP Change	</th><td> True             </td></tr>
<tr><th>Current IP	</th><td> 207.142.140.32   </td></tr>
<tr><th>Cached IP	</th><td> 207.142.140.107  </td></tr> 
</table>

From DNS IP Checker

---

## MIT license

Copyright (c) 2013 Louis E. Mauget, mauget@mindspring.com

## Platforms

Linux, Mac OS, Microsoft Windows, ... any platform where a Python 2.7.2, or greater is available. 
This includes Python 3 versions.

## Installation

 1. Copy the `*.py` files to your desired installation directory
 2. Rename `props_template.py` to `props.py`
 3. Edit the values of `props.py` for your environment and the desired behavior_
 4. `chmod 755 *.py` (unless installed on Microsoft Windows)

**Important:** the script cannot operate rationally for you unless you edit the values in step 3.

### Microsoft Windows

Microsoft Windows has no default Python system installed. Choose and download a  Python for Microsoft Windows from
[http://www.python.org/getit/windows/](http://www.python.org/getit/windows/).

## Execution

In the installation directory use `.\ipchecker.py`.  If using Microsoft Windows
issue `./ipchecker.py` or invoke `python ipchecker.py`.

If `props.do_run = True`, then the checking process will happen forever at intervals
defined by the number of seconds in `props.interval`. For example `props.interval = 30*60`
will cause the process to carry out its check once per half hour._

## Logging

The script records a trace of its operation in a log file. 
Logging level and log file name are controlled by `logging_level` and `logging_file` values in `props.py`.

Example of logging file content:

---

`INFO:2013-05-12 09:05:05 PM ipchecker started`

`INFO:2013-05-12 09:05:05 PM Resolved "google.com". Current IP "74.125.228.102". Cached IP "74.125.228.100"`

`INFO:2013-05-12 09:05:06 PM Successfully sent email`


---

## Configuration notes for props.py

We tried to make the configuration keys/names self-explanatory. Don't change the name on 
the left side of the equal sign. Do set the value as desired.

### Target DNS

---

`dns_name = ['google.com']`

---

### Checking interval in seconds

---

`interval = 60*30`

---

### Checking loop enabled: True means forever

Value can be `True` or `False`. Case matters.

---

`do_run = True`

---

### Notify when IP unchanged

Value can be `True` or `False`. Case matters.

---

`always_notify = True`

---

### SMTP properties

Get most of these from your email provider. Exception: the `smtp_debug_level` enables dumping extra information to `stdout` if set to non-zero.

---

`smtp_server = 'smtp.embarqmail.com`

`smtp_port = 587`

`smtp_user = 'someUserName'`

`smtp_debug_level = 1;  # 1 or 0 works`

`smtp_password = 'password'`

---

### Email properties

A comma-separated series of email recipient addresses enclosed in square brackets. Each address is surrounded by single or double quotes.
You probably will use just one recipient, but this example shows how to specify a distribution list.

---

`receivers = ['receiver1@somesite.com', 'receiver2@otherplace.org']`

---

### Email message template

There are five '%s' substitution points in the message. Top to bottom, these take the respective values of:

1. `sender` -- sending email address configured above
2. `dns_name` - target DNS name-of-interest configured above
3. `dns_name` - target DNS name-of-interest configured above
4. is_changed - value True or False - calculated
5. revolved IP address of `dns_name` - queried
6. cached previous IP address of `dns_name` - read from configured tracking file

---

`message_template = """From: DNS Tracker<%s>`

`To: Lou Mauget<mauget@mindspring.com>`

`MIME-Version: 1.0`

`Content-type: text/html`

`Subject: %s IP Tracking`


`<table>`
	
`<tr><th>DNS name</th><td>%s</td></tr>`

`<tr><th>IP Change</th><td>%s</td></tr>`

`<tr><th>Current IP</th><td>%s</td></tr>`

`<tr><th>Cached IP</th><td>%s</td></tr>`

`</table>`

`<p>`
	
`From DNS IP Checker`

`</p>`

``"""``

---

### Tracking file name and location

---

`tracker_file = 'tracker_file.txt'`

---

### Logging

Valid logging level value is choice of:

* logging.INFO
* logging.WARN
* logging.DEBUG
* logging.ERROR
* logging.CRITICAL

---

`logging_level = logging.INFO`

`logging_file = 'ipchecker.log'`

---

---

Lou Mauget, mauget@gmail.com, 2020-10-15

