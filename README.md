# DBookmark π

- modles -> admin -> views -> templates -> urls


- νλ‘μ νΈ μμ
  - django-admin startproject config .
  - python manage.py migrate
  - python manage.py createsuperuser
  - python manage.py runsever 
  

 - bookapp μ± μμ
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
    - bookmark/templates/bookmark bookmark_update.html, bookmark_list.html
    - bookmark/url bookmark:update
    - bookmark/models get_absolute_url() in Bookmark
   

 - Delete Bookmark
   - bookmark/view BookmarkDeleteView
   - bookmark/templates/bookmark bookmark_confirm_delete.html, bookmark_list.html
   - bookmark/url bookmark:delete
   
- κΈ°λ₯μμ± β¨πββοΈ
- config/templates/base.html, extends, block title, block content