
ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
/etc/init.d/nginx restart

ln -sf /home/box/web/etc/hello.py   /etc/gunicorn.d/hello.py
ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
/etc/init.d/gunicorn restart


