import os
import shutil

use_docker = bool("True" == "{{ cookiecutter.use_docker }}")
print(f"use_docker: {use_docker}")

print(f"cookiecutter.database: {{ cookiecutter.database }}")
use_postgres = bool("postgres" == "{{ cookiecutter.database }}")
print(f"use_postgres: {use_postgres}")

print(f"cookiecutter.use_tailwind: {{ cookiecutter.use_tailwind }}")
use_tailwind = bool("True" == "{{ cookiecutter.use_tailwind }}")
print(f"use_tailwind: {use_tailwind}")

print(f"cookiecutter.include_test_app: {{ cookiecutter.include_test_app }}")
include_test_app = bool("True" == "{{ cookiecutter.include_test_app }}")
print(f"include_test_app: {include_test_app}")

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

if use_docker:
  print(f"using docker")
  os.rename(os.path.join(cwd, 'if_use_docker.github'), os.path.join(cwd, '.github'))
  os.rename(os.path.join(cwd, 'if_use_docker_Dockerfile'), os.path.join(cwd, 'Dockerfile'))
  os.rename(os.path.join(cwd, 'if_use_docker_docker-compose.yml'), os.path.join(cwd, 'docker-compose.yml'))
  os.rename(os.path.join(cwd, 'if_use_docker_docker-compose.yml.j2'), os.path.join(cwd, 'docker-compose.yml.j2'))
else:
  print(f"not using docker")
  shutil.rmtree(os.path.join(cwd, 'if_use_docker.github'))
  os.remove(os.path.join(cwd, 'if_use_docker_Dockerfile'))
  os.remove(os.path.join(cwd, 'if_use_docker_docker-compose.yml'))
  os.remove(os.path.join(cwd, 'if_use_docker_docker-compose.yml.j2'))

if include_test_app:
  print(f"included test app")
  os.rename(os.path.join(cwd, 'if_include_test_app_test_app'), os.path.join(cwd, 'test_app'))
else:
  print(f"excluded test app")
  shutil.rmtree(os.path.join(cwd, 'if_include_test_app_test_app'))
