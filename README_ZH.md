# 非官方 Suno API

这一个基于 Python和 FastAPI 的非官方 Suno API，目前支持生成歌曲，歌词等功能。  
自带维护 token 与保活功能，无需担心 token 过期问题。

### 特点

- token 自动维护与保活
- 全异步，速度快，适合后期扩展
- 代码简单，易于维护，方便二次开发

### 对应的套壳

[https://github.com/Dooy/chatgpt-web-midjourney-proxy](https://github.com/Dooy/chatgpt-web-midjourney-proxy)

### 使用

#### 配置

编辑 `.env.example` 文件，重命名为 `.env`，填写 session_id 和 cookie

这些先从浏览器中获取，后期会自动保活。

![cookie](./images/cover.png)

#### 运行

安装依赖

```bash
pip3 install -r requirements.txt
```

这一部分，自行参考 FastAPI 文档

```bash
uvicorn main:app 
```

#### Docker

```bash
docker compose build && docker compose up
```

#### 文档

搭建服务后访问 /docs

![docs](./images/docs.png)


#### 合作交流

<img src="./images/wechat.jpg" width="382px" height="511px" />
