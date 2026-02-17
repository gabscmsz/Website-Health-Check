from requests import get

def get_response_code(url):
    response = get(url)
    return response.status_code

if __name__ == '__main__':
    url = input(print("Cole o URL do site: "))
    code = get_response_code(url)
    if code == 200:
        print("Site Ativo!")
    else:
        print("Site Fora do Ar. Erro " + str(code))

