## 簡介

應用Django的簡易學生成績CRUD系統
___
## 使用方式

若有更改modules,需輸入python manage.py makemigrations來完成修改

再輸入python manage.py migrate來部屬資料庫

用python manage.py createsuperuser來建立登入資料庫的帳號密碼

在manage.py的資料夾下輸入python manage.py runserver來部屬伺服器

到網頁的http://127.0.0.1:8000/admin 來登入並使用資料庫

資料庫的分類及欄位在modules.py中修改
___
## 介紹

網址輸入http://127.0.0.1:8000/ 來訪問首頁，對應index.html
![image](https://github.com/NAre3/djangofinal/assets/62021701/f0deb872-f143-488e-9fde-57b2b6652669)

點擊學生資料按鈕來總覽、編輯或刪除學生的資料
![image](https://github.com/NAre3/djangofinal/assets/62021701/1f13f9a6-7562-4e37-beef-21d286d87302)
![image](https://github.com/NAre3/djangofinal/assets/62021701/bc0c7f04-a28a-4bd6-b3a3-4d26357cfb4d)


點擊所有成績顯示、修改學生的各科分數
![image](https://github.com/NAre3/djangofinal/assets/62021701/52786fff-cc34-4884-9fed-91b1a8fe634f)

點擊新增資料來新增
![image](https://github.com/NAre3/djangofinal/assets/62021701/bdbf4e5b-f047-44a7-93f5-51b82951dcde)
