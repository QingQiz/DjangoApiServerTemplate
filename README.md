## -

### 部署

- 修改 `./conf/Apis.httpd.conf` 中的必要信息，复制到 `apache` 的配置文件目录下，并启用配置
- 执行 `./genApiDoc.sh` 生成 api 文档
  - 该过程需要使用 `apidoc`，执行 `npm install -g apidoc`
  - 对于 `ubuntu` 系 `nodejs` 版本太老的问题，执行 `npm install -g n && n latest`
- 重启 `apache`

