import os
import subprocess

def run_command(command, cwd=None):
  result = subprocess.run(command, shell=True, cwd=cwd, text=True, capture_output=True)
  if result.returncode == 0:
    print(f'✅ Başarılı: {command}')
  else:
    print(f'❌ Hata oluştu. Lütfen tekrar deneyiniz. {command}\n{result.stderr}')

def setup_frontend():
  print('🚀 Frontend kurulumu başlatılıyor...')
  frontend_path = os.path.join(os.getcwd(), "frontend")
  run_command("npm install", cwd=frontend_path)
  run_command("npm run build", cwd=frontend_path)

def setup_backend():
  print('🚀 Backend kurulumu başlatılıyor...')
  backend_path = os.path.join(os.getcwd(), "backend")
  run_command("pip install django", cwd=backend_path)

def main():
  print('🔧 Otomatik yapılandırma başlatılıyor...')
  setup_frontend()
  setup_backend()
  print('🎉 Kurulum tamamlandı! Projeyi 127.0.0.1:8000 adresinden görüntüleyebilirsiniz.')

if __name__ == "__main__":
  main()
