## -

### 部署

- 修改 `./conf/Apis.httpd.conf` 中的必要信息，复制到 `apache` 的配置文件目录下(/etc/apache2/site-available)
- 并启用配置 `a2ensite Apis.httpd.conf`
- 执行 `./genApiDoc.sh` 生成 api 文档
  - 该过程需要使用 `apidoc`，执行 `npm install -g apidoc`
  - 对于 `ubuntu` 系 `nodejs` 版本太老的问题，执行 `npm install -g n && n latest`
- 执行 `./manage.py collectstatic`
- 执行 `./manage.py makemigrate`
- 重启 `apache`

### 一些坑

- ubuntu 需要装 `libapache2-mod-wsgi-py3`，其他系统我忘了
- 注意，配置文件里的是 `wsgi.py` 而不是 `asgi.py`，别一不小心vim自动补全然后打错了（~~说的就是我~~
- 遇到数据库写入问题的时候，可能是目录的所有者不对，此时执行 `chown www-data:www-data -R /path/to/project` 就可

