## Automação de Login e Webscraping
Este simples projeto tem como objetivo automatizar o processo de login e raspagem de dados da seção de tutoriais do github

### Dependêcias:
venv
.env
.gitignore
selenium webdriver # Controla o navegador
selenium options
selenium keys
selenium by
selenium service # Gerencia a execução do WebDriver: inicia, mantém e encerra o processo, utilizando o caminho do chromedriver.
dotenv

### Instalação das dependências
pip install selenium
python -m venv <nome_do_ambiente>
nome_do_ambiente\Scripts\activate
pip install python-dotenv (dentro do venv)

### Comandos
Essa linha inicia o navegador Chrome usando o WebDriver, passando o serviço que gerencia o driver (service_system) e as opções de configuração personalizadas (chrome_options).
browser = webdriver.Chrome(service=service_system, options=chrome_options)

### é usado para determinar o caminho absoluto do chromedriver.exe.
driver_path = os.path.abspath('./common/chromedriver.exe')
Aqui, você está criando um objeto chamado service_system da classe Service do Selenium. Esse objeto é responsável por iniciar o chromedriver com o caminho absoluto do arquivo que você obteve na linha anterior.
service_system = Service(executable_path=driver_path)
Resumindo: driver_path transforma o caminho do driver em um caminho absoluto. Já service_system cria o serviço que permite a comunicação entre o Selenium e o WebDriver, utilizando o caminho absoluto onde o driver está localizado.

### Essa função carrega as variáveis de ambiente de um arquivo .env. Isso é útil para manter informações sensíveis, como seu username e password, fora do código-fonte, mantendo a segurança.
load_dotenv() 

`Resgata automaticamente o username e a senha a partir do arquivo .env e os insere nos campos de login no GitHub.`
username = os.getenv('GITHUB_USERNAME')
password = os.getenv('GITHUB_PASSWORD')

`Essa linha localiza o campo de entrada para o nome de usuário`
username_input = browser.find_element(By.ID, 'login_field')

`Essa linha localiza o campo de entrada para a senha do usuário`
password_input = browser.find_element(By.ID, 'password')

`Localiza o botão de login`
login_button = browser.find_element(By.NAME, 'commit')

`Clica no botão de login`
#login_button.click()

Essas duas linhas automatizam a ação de preencher os campos de login com o nome de usuário e a senha.
Lembrando, que essas informações já foram definidas no .env
username_input.send_keys(username)
password_input.send_keys(password)
