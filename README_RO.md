[简体中文](README_ZH.md) | [日本語](README_JA.md)

# API Suno Neoficial

Acesta este un API Suno neoficial bazat pe Python și FastAPI. În prezent, suportă generarea de cântece, versuri, etc.
Vine cu o funcționalitate integrată de menținere a tokenului și de menținere a conexiunii, astfel încât să nu trebuie să vă faceți griji în legătură cu expirarea tokenului.

### Caracteristici

- Menținerea automată a tokenului și a conexiunii
- Complet asincron, rapid, potrivit pentru o extindere ulterioară
- Cod simplu, ușor de întreținut, convenabil pentru dezvoltarea secundară

### Utilizare

#### Configurare

Editați fișierul `.env.example`, redenumiți-l în `.env` și completați cu session_id și cookie.

Acestea sunt obținute inițial din browser și vor fi menținute automat în viitor.

![cookie](./images/cover.png)

#### Rulare

Instalați dependențele

```bash
pip3 install -r requirements.txt
```
Pentru această parte, consultați documentația FastAPI pe cont propriu.

```bash
uvicorn main:app 
```

#### Docker

```bash
docker compose build && docker compose up
```

#### Documentație

După configurarea serviciului, vizitați /docs

![docs](./images/docs.png)

#### Contactați-mă
<img src="./images/wechat.jpg" width="382px" height="511px" />
