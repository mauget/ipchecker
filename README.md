#ipchecker#

Periodically pings a configured DNS name, checking for an IP address reassignment.
Emails the IP address to an interested party when the target DNS name's IP address changes.

##Example of EMailed Notification##

<table>
<tr><th>DNS name	</th><td> www.somesite.com</td></tr>
<tr><th>IP Change	</th><td> True             </td></tr>
<tr><th>Current IP	</th><td> 207.142.140.32   </td></tr>
<tr><th>Cached IP	</th><td> 207.142.140.107  </td></tr> 
</table>

From DNS IP Checker

##MIT License##

Copyright (c) 2013 Louis E. Mauget, mauget@mindspring.com

##Platforms##
Linux, Mac OS, Microsoft Windows, ... any platform where Python 2.7.2 or greater is available

##Installing##

 1. Copy the `*.py` files to your desired installation directory
 2. Rename `props_template.py` to `props.py`
 3. Edit the values of `props.py` for your environment and the desired behavior_
 4. `chmod 755 *.py` (unless installed on Microsoft Windows)

###Microsoft Windows Notes###

Microsoft Windows has no default Python system installed. Choose and download a  Python for Microsoft Windows from
[http://www.python.org/getit/windows/](http://www.python.org/getit/windows/).

##Execution##

In the installation directory use `.\ipchecker.py`.  If using Microsoft Windows
issue `./ipchecker.py` or invoke `python ipchecker.py`.

If `props.do_run = True`, then the checking process will happen forever at intervals
defined by the number of seconds in `props.interval`. For example `props.interval = 30*60`
will cause the process to carry out its check once per half hour._
