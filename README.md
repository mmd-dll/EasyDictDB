# PyEasyDB
A simple library to save and load Python dictionaries in SQLite.


## ویژگی‌ها

- ذخیره سازی و بازیابی اسان دیتاها
- اسان کردن کارشما در استفاده از اس کیو ال
- سبک و سریع



## سوالاتی راجب این کتابخونه

#### آیا متغیر هایی جز دیکشنری رو ذخیره میکنه؟

خیر این کتابخونه برای ذخیره دیکشنری طراحی شده

#### آیا میشه چند دیکشنری رو به صورت جدا ذخیره کرد؟

بله وقتی میخواین دیکشنری رو ذخیره کنید میتونین یک شناسه بهش بدید


## نصب

نصب از طریق ترمینال

```bash
  pip install PyEasyDB
```

## نمونه کد
- ذخیره دیتا
```python
from PyEasyDB import save,load

data = {'name':'mohammad','age':18}

save(data,'user1')
#در اینجا یک فایل data.db ساخته میشود و دیتا توش ذخیره میشه

```

- لود کردن دیتا

```python
from PyEasyDB import save,load

data = load('user1')
# اگه دیتا وجود داشته باشه دیتا = {'name':'mohammad','age':18}
```
