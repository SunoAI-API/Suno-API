[简体中文](README_ZH.md) | [日本語](README_JA.md)

### FoxAIHub

FoxAIHub focuses on delivering efficient and reliable AI model API services, covering text-to-image, text-to-video, image-to-video, and music generation API, helping you stay ahead at the intersection of creativity and technology.
[FoxAIHUb](https://foxaihub.com)


### Unofficial API

This is an unofficial API based on Python and FastAPI. It currently supports generating songs, lyrics, etc.  
It comes with a built-in token maintenance and keep-alive feature, so you don't have to worry about the token expiring.

### Features

- Automatic token maintenance and keep-alive
- Fully asynchronous, fast, suitable for later expansion
- Simple code, easy to maintain, convenient for secondary development


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
