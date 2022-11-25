import requests 
import concurrent.futures
import time

def requesting(count):
    count + 1
    print(f'Request {count}...')
    x = requests.get('http://localhost:8080', stream=True)
    return f'Request {count} done'

def run_processes(total: int):
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(requesting, count) for count in range(total)]
    
        for fu in concurrent.futures.as_completed(results):
            print(fu.result())

    finish = time.perf_counter()
    print(f'Finished {total} request(s) in {round(finish-start, 2)} second(s)')

if __name__ == '__main__':
    run_processes(10000)
