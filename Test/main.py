import time
import run

if __name__ in "__main__":
    print("\n\n")
    print(time.strftime("%c", time.localtime(time.time())))
    start_time = time.time()
    run.start()
    end_time = time.time() - start_time
    print(end_time)