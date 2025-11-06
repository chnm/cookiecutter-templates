import os
import shutil

print(f"cookiecutter.database: {{ cookiecutter.database }}")
use_postgres = bool("postgres" == "{{ cookiecutter.database }}")
print(f"use_postgres: {use_postgres}")

print(f"cookiecutter.use_tailwind: {{ cookiecutter.use_tailwind }}")
use_tailwind = bool("True" == "{{ cookiecutter.use_tailwind }}")
print(f"use_tailwind: {use_tailwind}")

cwd = os.getcwd()
print(f"cwd: {cwd}")

os.rename(os.path.join(cwd, 'env_template'), os.path.join(cwd, '.env'))

if use_postgres:
  print(f"using postgres")
  os.rename(os.path.join(cwd, 'if_use_postgres_initdb'), os.path.join(cwd, 'initdb'))
else:
  print(f"not using postgres")
  shutil.rmtree(os.path.join(cwd, 'if_use_postgres_initdb'))

if use_tailwind:
  print(f"using tailwind")
  os.rename(os.path.join(cwd, 'if_use_tailwind_package.json'), os.path.join(cwd, 'package.json'))
  os.rename(os.path.join(cwd, '{{ cookiecutter.initial_app_name }}/if_use_tailwind_theme'), os.path.join(cwd, '{{ cookiecutter.initial_app_name }}/theme'))
else:
  print(f"not using tailwind")
  shutil.rmtree(os.path.join(cwd, 'if_use_tailwind_theme'))
  os.remove(os.path.join(cwd, 'if_use_tailwind_package.json'))
