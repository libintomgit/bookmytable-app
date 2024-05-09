import os

a = f"this is os.environ ---- {os.environ['POSTGRES_PASSWORD']}"
print(a)


b = os.environ.get('POSTGRES_DB','LIBIN')
print(f"this is os.environ.get ---- {b}")