from datetime import datetime, timedelta

import requests


def get_count_of_product(status, page, sincedate, website):
    params = dict(status=status, page=page)
    rsp = requests.get(website, params=params)
    sinseTimeUTC = int((sincedate - datetime(1970, 1, 1)) / timedelta(milliseconds=1))
    count = 0
    for item in rsp.json()['data']:
        intTimesStamp = int(item['timestamp'])
        if intTimesStamp > sinseTimeUTC:
            count += 1

    print("Total products found:", count)


def main():
    website = 'https://jsonmock.hackerrank.com/api/iot_devices/search'
    # get_count_of(input("Status? "), input("Page? "), input("Date? "), website)
    get_count_of_product("stopped", "2", datetime(2000, 10, 10), website)


if __name__ == "__main__":
    main()
