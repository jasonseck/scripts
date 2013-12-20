#!/bin/bash
diff /var/log/auth.log /var/log/auth.tmp | /usr/sbin/sendmail jasonseck@gmail.com
cp /var/log/auth.log /var/log/auth.tmp
