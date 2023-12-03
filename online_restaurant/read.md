python manage.py runserver 

运行网页版

先在setting文件中修改database

再在database中建立数据库online_restaurant

迁移数据库

python manage.py makemigrations

python manage.py migrate


修改每个app里的views文件和urls文件可实现业务逻辑，tempaltes文件夹负责实现静态内容，models文件负责实行数据库内容修改
