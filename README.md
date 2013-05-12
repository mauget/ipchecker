#ipchecker#

Periodically pings a configured DNS name, checking for an IP address reassignment.
Emails the IP address to an interested party when the target DNS name's IP address changes.

##Example of EMailed Notification##

---

From: IP Checker &lt;ipchecker@hostsite.org&gt;

To: Interested Party &lt;sombody@somesite.org&gt;

Subject: DNS IP Tracking

<table>
<tr><th>DNS name	</th><td> www.somesite.com</td></tr>
<tr><th>IP Change	</th><td> True             </td></tr>
<tr><th>Current IP	</th><td> 207.142.140.32   </td></tr>
<tr><th>Cached IP	</th><td> 207.142.140.107  </td></tr> 
</table>

From DNS IP Checker

---

##MIT License##

Copyright (c) 2013 Louis E. Mauget, mauget@mindspring.com

##Platforms##

Linux, Mac OS, Microsoft Windows, ... any platform where Python 2.7.2 or greater is available

##Installing##

 1. Copy the `*.py` files to your desired installation directory
 2. Rename `props_template.py` to `props.py`
 3. Edit the values of `props.py` for your environment and the desired behavior_
 4. `chmod 755 *.py` (unless installed on Microsoft Windows)

**Important:** the script will cannot operate rationally for you unless you edit the values in step 3.

###Microsoft Windows Notes###

Microsoft Windows has no default Python system installed. Choose and download a  Python for Microsoft Windows from
[http://www.python.org/getit/windows/](http://www.python.org/getit/windows/).

##Execution##

In the installation directory use `.\ipchecker.py`.  If using Microsoft Windows
issue `./ipchecker.py` or invoke `python ipchecker.py`.

If `props.do_run = True`, then the checking process will happen forever at intervals
defined by the number of seconds in `props.interval`. For example `props.interval = 30*60`
will cause the process to carry out its check once per half hour._

##Configuration Notes##

We tried to make the configuration keys/names self-explantory. Don't change the name on 
the left side of the equal sign. Do set the value as desired.

###Target DNS###

`dns_name = 'google.com'`

###Checking interval in seconds###

`interval = 60*30`

###Checking loop enabled: Forever is True###

`do_run = False`

###Notify when IP unchanged###

`always_notify = True`

###SMTP properties###

`smtp_server = 'smtp.embarqmail.com`
`smtp_port = 587`
`smtp_user = 'someUserName'`
`smtp_debug_level = 1;  # 1 or 0 works`
`smtp_password = 'password'`

###Email properties###

`receivers = ['receiver1@somesite.com', 'receiver2@otherplace.org']`

###Email message template###

`message_template = """From: No-Reply<%s>`

`To: Lou Mauget <mauget@mindspring.com>`

`MIME-Version: 1.0`

`Content-type: text/html`

`Subject: DNS IP Tracking`

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

###Tracking file name and location###

`tracker_file = 'tracker_file.txt'`
