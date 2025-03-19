import os
import subprocess

def run_command(command, cwd=None):
  result = subprocess.run(command, shell=True, cwd=cwd, text=True, capture_output=True)
  if result.returncode == 0:
    print(f'✅ Başarılı: {command}')
  else:
    print(f'❌ Hata oluştu. Lütfen tekrar deneyiniz. {command}\n{result.stderr}')

def main():
  backend_path = os.path.join(os.getcwd(), "backend")
  run_command("python manage.py runserver", backend_path)

if __name__ == "__main__":
  main()