from requests import get
from requests.exceptions import (
    Timeout,
    SSLError,
    ConnectionError,
    TooManyRedirects,
    RequestException
)

def get_response_code(site_url):
    try:
        headers = {'user-agent': 'Mozilla/5.0'}
        response = get(site_url, headers=headers, timeout=5)
    except Timeout:
        print("Erro de Timeout. O site excedeu o tempo de carregamento estipulado.")
    except SSLError:
        print("Erro de Segurança. O certificado SSL é inválido ou expirou.")
    except ConnectionError:
        print("Erro de Conexão. Verifique sua conexão com a Internet.")
    except TooManyRedirects:
        print("Erro. O site excedeu o limite de redirecionamentos.")
    except RequestException:
        print("Um erro não esperado ocorreu.")
    else:
        return response.status_code

if __name__ == '__main__':
    url = ""
    while url != "Fim":
        url = input(print("Cole o URL do site: "))
        if url == "Fim":
            break
        codError = get_response_code(url)
        if codError == 200:
            print("Site Ativo!")
        elif codError is not None:
            print("Site Fora do Ar. Erro " + str(codError))
