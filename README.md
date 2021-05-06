# DBookmark 📚

- modles -> admin -> views -> templates -> urls


- 프로젝트 시작
  - django-admin startproject config .
  - python manage.py migrate
  - python manage.py createsuperuser
  - python manage.py runsever 
  

 - bookapp 앱 시작
    - python manage.py startapp bookmark
    - 'bookmark', in INSTALLED_APPS


 - boolmark/modles Bookmark
    - python manage.py makemigrations bookmark
    - python manage.py migrate 
    - \_\_str\_\_()
    

 - bookmark/admin Bookmark


 - List BookMark
    - bookmark/views BookmarkListView
    - bookmark/templates/bookmark bookmark_list.html
    - urls; bookmark/urls bookmark:list
    

 - Add BookMark
    - bookmark/views BookmarkCreateView
    - bookmark/templates/bookmark bookmark_create.html, bookmark_list.html
    - bookmark/urls bookmark:add
    
 - Detail BookMark
    - bookmark/views BookmarkDetailView
    - bookmark/templates/bookmark bookmark_detail.html, bookmark_list.html
    - bookmark/urls bookmark:detail

 - Update BookMark
    - bookmark/views BookmarkUpdateView