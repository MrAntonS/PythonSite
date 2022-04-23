    p1 =multiprocessing.Process(target=do_smth)
    p2 = multiprocessing.Process(target=do_smth)

    p1.start()
    p2.start()

    fin = time.perf_counter()

    print(f'Finished in {round(fin - start, 2)} second(s)')