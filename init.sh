﻿ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
rm /etc/nginx/sites-enabled/default
/etc/init.d/nginx restart

ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
/etc/init.d/gunicorn restart

