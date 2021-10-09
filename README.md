Mock Server
===========

基于Flask的简易mock平台

Key Features
------------

本地开发环境部署
---------------

1. git clone 或者 checkout至本地目录
2. 修改：MockServer/config.py 数据库相关配置
    ```python
    USERNAME = 'root'
    PASSWORD = 'xxxxx'
    HOST = '127.0.0.1'
    DB = 'MockServer'
    ```
3. 安装相应依赖库
    ```bash
    pip install -r requirements.txt
    ```
4. 创建MockServer数据库, 默认DB是MockServer
5. 生成数据库迁移脚本，应用表结构
    ```bash
   flask db init
   flask db migrate
   flask db upgrade
    ```
6. Start Server