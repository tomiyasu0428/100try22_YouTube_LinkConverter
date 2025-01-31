# YouTube Shorts Link Converter
YouTube Shorts のURLを通常のYouTube動画URLに変換するツールです。

ファイル構造

Shorts_Link_Converter/
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html
├── static/
│   ├── style.css
├── README.md

環境構築の流れ

1. 仮想環境の作成

python -m venv venv

2. 仮想環境の有効化

Windows:

venv\Scripts\activate

macOS/Linux:

source venv/bin/activate

3. 必要なライブラリのインストール

pip install -r requirements.txt

4. アプリの起動

python app.py

使い方

ブラウザで http://127.0.0.1:5000/ を開きます。

https://www.youtube.com/shorts/XXXX の形式のURLを入力し、「変換」ボタンを押します。

変換されたURLが表示され、クリックすると通常のYouTube動画ページが開きます。

デプロイ方法

Cloudflare Pages, Render, Heroku などに対応

GitHubリポジトリを作成し、コードをプッシュします。

適切なホスティングサービスでFlaskアプリをデプロイします。

ライセンス

MIT