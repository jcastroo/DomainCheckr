import whois
from colorama import Fore, init

# Inicializa o colorama
init(autoreset=True)

ascii_art = """
    |__| ____ _____    _______/  |________  ____   ____  
    |  |/ ___\\__  \  /  ___/\   __\_  __ \/  _ \ /  _ \ 
    |  \  \___ / __ \_\___ \  |  |  |  | \(  <_> |  <_> )
/\__|  |\___  >____  /____  > |__|  |__|   \____/ \____/ 
\______|    \/     \/     \/                                
"""

def verificar_disponibilidade(dominio):
    extensoes = ['.com', '.net', '.org', '.info', '.co', '.io', '.pt', '.edu']

    print(Fore.BLUE + ascii_art)  
    
    for ext in extensoes:
        dominio_completo = dominio + ext
        try:
            informacoes = whois.whois(dominio_completo)
            if informacoes.domain_name:
                print(f"{Fore.RED}{dominio_completo} já está registado.")
            else:
                print(f"{Fore.GREEN}{dominio_completo} está disponível.")
        except Exception:
            print(f"{Fore.GREEN}{dominio_completo} está disponível.")

if __name__ == "__main__":
    print(Fore.BLUE + ascii_art)  
    dominio = input("Domínio Pretendido (sem a extensão): ").strip()
    verificar_disponibilidade(dominio)
