# syntax=docker/dockerfile:1
FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

EXPOSE 8000
ENV BASE_URL=https://studio-api.suno.ai
ENV SESSION_ID=sess_2fpxj0Fbk7b7czZxbu7u2Up2Ron
ENV COOKIE=__client=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImNsaWVudF8yZXZQNzNCSTNkZWkwZDk3WkJCTWFPSEZuMzkiLCJyb3RhdGluZ190b2tlbiI6ImVwdjR3djRzNGp0ZXZtcWxvajIwa2JrcmVub3A1amQ0aGdiOG0yYTgifQ.sspHveYOZ9zQ53IZCmSZtx6UNchMYFPikulavV0udaUoNC77u3e_CASroYlQKQ-myK6yebyu4BBpxLaovGsGgNGdun3pOeYAiQs2SUSF6F1GFt44g-Wpy8G7ViXpLUx6silpR-2kpvNsKICYYzu21octLGrSEEVf9fxALTw4_kV1DKHI35gNb2KrJxn0BGyl2zcilFyJ9pNGB8WXCnui-N2Vh8CfTIwDd4p0vmTZZNFOGlkIctuygveX4IuploCIRpUSQk0lku6wIioii49kyWeJsk7OiSimUd1RvFA1JUMC6edVpn--kKiDF-NAF9-kLRmYW6Xjac5eMZMtIvqN_Q; __client_uat=1714511951; __cf_bm=t_7B.UdrL_zoIpDcOj6TqNrKM3tCMy2TtBaVuqZQu2M-1714569058-1.0.1.1-OsVpBoNPGIBLjVWPCjRVfZCBg7sJLCfLUn2qwLeCgQZvDNpw4Yl8iYJjanCGc7VbImnvSJimpAGKbay21GB4RQ; __cf_bm=AB3uYhRYU7BG.CDU9M0Ll51fYxI_4ClZ_lUCb9AvqbE-1714569708-1.0.1.1-i.Nih125eobc0FOYwNBAlB2SQS_VSH7DCGI7ueXIP1h9bL8I3qx8Uj.OfV4xp5x8FUR_DQxKyRVitM5jvYPnUw; _cfuvid=QUmLN_OOvwoyvqoaN7fyYJ1_cJ3bLT_6rXbdWJBwfIo-1714569709283-0.0.1.1-604800000; mp_26ced217328f4737497bd6ba6641ca1c_mixpanel=%7B%22distinct_id%22%3A%20%22ce25f3b7-571d-4178-9536-425f6ca7e4ba%22%2C%22%24device_id%22%3A%20%2218ec9c0c55c313-03c626da4d21d8-26001a51-384000-18ec9c0c55c313%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22%24user_id%22%3A%20%22ce25f3b7-571d-4178-9536-425f6ca7e4ba%22%7D

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]
