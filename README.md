# Flask-LINE-notify

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-%3E%3D%203.5-blue.svg)](https://badge.fury.io/py/lotify)

這是一個使用 [Lotify](https://github.com/louis70109/lotify) 以及 Swagger 的範例程式，歡迎大家取用試玩。

# LINE Notify 註冊

可以參考我之前[鐵人賽的文章](https://nijialin.com/2019/09/20/Day5-%E5%81%9A%E4%B8%80%E5%80%8B%E8%88%87-LINE-Notify-%E9%80%A3%E5%8B%95%E7%9A%84%E6%9C%8D%E5%8B%99/)。

設定的 Callback Url 為 `http://YOUR_DOMAIN/callback`，本地端測試網址就為 `http://localhost:5000/callback`

# 一鍵部署

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

按下上面部署按鈕之後需要設定 LINE Notify 基本所需三個 `環境變數`
![heroku-env-settings](https://i.imgur.com/wV5rUyMl.png)

以下則是環境變數所有的詳細介紹

# 環境變數

```
LINE_NOTIFY_CLIENT_ID=
LINE_NOTIFY_CLIENT_SECRET=
LINE_NOTIFY_REDIRECT_URI=
// 三個 LINE Notify 需要的參數
DOMAIN_NAME=  // swagger 相關參數
LOCAL=true  // 預設本地端 true，若是上限則需 false | None 
PORT= // API port
```

# 本地端測試

```
cp .env.sample .env
LOCAL=true python api.py
```

## Docker

```
docker build -t lotify-swagger .
docker run --rm \
-e LOCAL=true -e LINE_NOTIFY_CLIENT_ID= \
-e LINE_NOTIFY_CLIENT_SECRET= -e LINE_NOTIFY_REDIRECT_URI= \
-p 5000:5000 lotify-swagger  
```
# 步驟

### [LINE Notify](https://notify-bot.line.me/zh_TW/) 基本設定

![](https://i.imgur.com/cqmi2x0l.png)

---

### 初始頁面

開啟瀏覽器後輸入 `http://localhost:5000` 後就會看到一個輸入按鈕

![](https://i.imgur.com/u3W3jOil.png)

---

### 綁定通知 - 選擇`1對1聊天接收`

![](https://i.imgur.com/bdGHOqbl.png)

---

### 連動完成

這時候 LINE Notify 就會推播一個綁定成功的通知

![](https://i.imgur.com/veLmsRkl.png)

---

### 網頁範例

同時瀏覽器會被導到`/notify/check` 並帶上 code & state 的資訊
![](https://i.imgur.com/XlkhJwM.png)

---

### 實測內容

## ![](https://i.imgur.com/jf1HUqEl.png)

# 路由

- 配合前端 template
    - GET /
      - 使用者點選綁定的畫面
    - GET /callback
      - LINE Notify 的設定以及認證完後的 callback 路由
  
- 幫忙發送推播的路由(因為有[ CORS 問題](https://developer.mozilla.org/zh-TW/docs/Web/HTTP/CORS)所以需要 api 來幫忙轉發)
    - <mark>取得連結</mark> POST /notify/link 
    - <mark>換取 Token</mark> POST /notify/change
    - <mark>發送文字訊息</mark> POST /notify/send
    - <mark>發送貼圖訊息</mark> POST /notify/sticker
    - <mark>發送圖片 by 網址</mark> POST /notify/url
    - <mark>發送圖片 by 檔案</mark> POST /notify/file
    - <mark>註銷 Token</mark> POST /notify/revoke

# 授權

[MIT](https://github.com/louis70109/flask-line-notify/blob/master/MIT-LICENSE)
