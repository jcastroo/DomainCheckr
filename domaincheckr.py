import whois
from colorama import Fore, init
import argparse

init(autoreset=True)

ascii_art = """
    |__| ____ _____    _______/  |________  ____   ____  
    |  |/ ___\\__  \  /  ___/\   __\_  __ \/  _ \ /  _ \ 
    |  \  \___ / __ \_\___ \  |  |  |  | \(  <_> |  <_> )
/\__|  |\___  >____  /____  > |__|  |__|   \____/ \____/ 
\______|    \/     \/     \/                                
"""


init(autoreset=True)

def check(dominio):
    extensoes = ['.com', '.net', '.org', '.info', '.co', '.io', '.pt', '.edu', '.eu']
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

def main():
    print(Fore.BLUE + ascii_art)  

    parser = argparse.ArgumentParser(description="Verifica a disponibilidade de domínios.")
    parser.add_argument('dominio', help="O nome do domínio (sem a extensão).")
    
    args = parser.parse_args()
    
    check(args.dominio)

if __name__ == "__main__":
    main()

