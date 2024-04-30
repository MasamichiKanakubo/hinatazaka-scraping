from bs4 import BeautifulSoup
import requests
import os

url = 'https://www.hinatazaka46.com/s/official/diary/detail/55786?ima=0000&cd=member'
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

images = soup.body.find_all('img')

# 'images' ディレクトリが存在しない場合は作成する
if not os.path.exists('images'):
    os.makedirs('images')

for img in images:
    src = img.get('src')
    if src and src.endswith('.jpg'):  # URLが '.jpg' で終わるか確認
        image_response = requests.get(src)
        if image_response.status_code == 200:
            # URLからファイル名を抽出（URLの最後の部分をファイル名とする）
            filename = src.split('/')[-1]
            # 完全なパスを指定
            file_path = os.path.join('images', filename)
            # 画像をファイルに保存
            with open(file_path, 'wb') as file:
                file.write(image_response.content)
            print(f"Saved {filename} to images directory.")
        else:
            print(f"Failed to download {src}")
