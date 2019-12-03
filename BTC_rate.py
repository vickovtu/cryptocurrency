import threading
from w_r_json import write_rate
from cryptocurrency_exchange import *


def show_results(stock_rates):
    while True:
        print(stock_rates)
        time.sleep(1)


def rate():
    # словарь, куда каждый поток складывает полученную информацию
    stock_rates = {'exmo': 0, 'binance': 0, 'bittrex': 0}

    threads = []

    # Подготавливаем потоки, складываем их в массив
    exmo_thread = threading.Thread(target=get_exmo_rates, args=(stock_rates,))
    binance_thread = threading.Thread(target=get_binance_rates, args=(stock_rates,))
    bittrex_thread = threading.Thread(target=get_bittrex_rates, args=(stock_rates,))
    show_results_thread = threading.Thread(target=show_results, args=(stock_rates,))
    write_to_json = threading.Thread(target=write_rate, args=(stock_rates,))

    threads.append(exmo_thread)
    threads.append(binance_thread)
    threads.append(bittrex_thread)
    threads.append(show_results_thread)
    threads.append(write_to_json)

    # Запускаем каждый поток
    for thread in threads:
        thread.start()

    # Ждем завершения каждого потока
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    rate()
