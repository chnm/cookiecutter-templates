import os
import shutil

print(f"cookiecutter.use_tailwind: {{ cookiecutter.use_tailwind }}")
use_tailwind = bool("True" == "{{ cookiecutter.use_tailwind }}")
print(f"use_tailwind: {use_tailwind}")

cwd = os.getcwd()
print(f"cwd: {cwd}")

if use_tailwind:
  print(f"using tailwind")
  os.rename(os.path.join(cwd, 'if_use_tailwind_theme'), os.path.join(cwd, 'theme'))
  os.rename(os.path.join(cwd, 'if_use_tailwind_package.json'), os.path.join(cwd, 'package.json'))
else:
  print(f"not using tailwind")
  shutil.rmtree(os.path.join(cwd, 'if_use_tailwind_theme'))
  os.remove(os.path.join(cwd, 'if_use_tailwind_package.json'))
