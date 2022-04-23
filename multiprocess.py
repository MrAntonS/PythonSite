import time
import multiprocessing as mp
import threading

start = time.perf_counter()

def do_smth(sec):
    print('Sleep')
    time.sleep(sec)
    return "Done"

if __name__ == '__main__':
    with mp.Pool() as pool:
        result = pool.map(do_smth, [1,2,3,4,5,6,7,8,9,10])
        print(result)
    # applications = []
    # for _ in range(10):
    #     p = multiprocessing.Process(target=do_smth, args=[_])
    #     p.start()
    #     applications.append(p)
    # for _ in applications:
    #     _.join()
    
    fin = time.perf_counter()

    print(f'Finished in {round(fin - start, 2)} second(s)')