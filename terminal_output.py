from api_client import get_bus_arrivals
import time

if __name__ == "__main__":
    while True:
        arrivals = get_bus_arrivals()
        msg = " | ".join(arrivals) if arrivals else "No data"
        print(msg)
        print("---")
        time.sleep(20)
