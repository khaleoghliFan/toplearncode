# session 3
[source](https://www.youtube.com/watch?v=qDwdMDQ8oX4&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=3>)
### 1. ساخت قالب پایه (`base.html`)
```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html>
<head>
  <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
  <header>...</header>

  {% block content %}
  <!-- محتوای پیش‌فرض -->
  {% endblock %}

  <footer>...</footer>
</body>
</html>
```
2. فایل فرزند (home.html)
```html
Copy
Edit
{% extends "base.html" %}

{% block title %}خانه{% endblock %}

{% block content %}
<h2>خوش آمدید</h2>
<p>این صفحه خانه است.</p>
{% endblock %}
```
