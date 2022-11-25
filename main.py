import requests 

if __name__ == '__main__':
    for _ in range(10):
        x = requests.get('http://localhost:8080')
