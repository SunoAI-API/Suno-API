[简体中文](README_ZH.md) | [日本語](README_JA.md)

### Unofficial API

This is an unofficial API based on Python and FastAPI. It currently supports generating songs, lyrics, etc.  
It comes with a built-in token maintenance and keep-alive feature, so you don't have to worry about the token expiring.

### Features

- Automatic token maintenance and keep-alive
- Fully asynchronous, fast, suitable for later expansion
- Simple code, easy to maintain, convenient for secondary development


### Contact me

[https://t.me/austin2035](https://t.me/austin2035)


### Usage

#### Configuration

Edit the `.env.example` file, rename to `.env` and fill in the session_id and cookie.

These are initially obtained from the browser, and will be automatically kept alive later.

![cookie](./images/cover.png)


#### Run

Install dependencies 

```bash
pip3 install -r requirements.txt
```

For this part, refer to the FastAPI documentation on your own.
```bash
uvicorn main:app 
```

#### Docker

```bash
docker compose build && docker compose up
```

#### Documentation

After setting up the service, visit /docs

![docs](./images/docs.png)

#### 合作交流
备注进群：拉你进入 音乐生成行业交流群
<img src="./images/wechat.jpg" width="382px" height="511px" />

### Useful resources

[chatgpt web, midjourney, gpts,tts, whisper,suno-v3](https://github.com/Dooy/chatgpt-web-midjourney-proxy)

