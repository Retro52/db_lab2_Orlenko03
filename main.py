import psycopg2

import config

query_1 = '''
    SELECT launchyear.launchy_year, COUNT(cpu_name) FROM cpu INNER JOIN launchyear
ON launchyear.launchy_id = cpu.launchy_id
GROUP BY launchyear.launchy_year
ORDER BY launchyear.launchy_year DESC
'''

query_2 = '''
    SELECT threads.thread_count, COUNT(cpu_name) FROM cpu INNER JOIN threads
ON threads.thread_id = cpu.thread_id
GROUP BY threads.thread_count
ORDER BY COUNT(cpu_name), threads.thread_count
'''

query_3 = '''
    SELECT launchyear.launchy_year, MIN(lithography.lithography_size)
FROM cpu
JOIN launchyear
ON launchyear.launchy_id = cpu.launchy_id
JOIN lithography
ON lithography.lithography_id = cpu.lithography_id
GROUP BY launchyear.launchy_year
ORDER BY launchyear.launchy_year
'''


def get_query_result(_q: str):
    _connection = psycopg2.connect(user=config.username, password=config.password, dbname=config.database,
                                   host=config.host, port=config.port)

    _res = []

    with _connection:
        _cursor = _connection.cursor()
        _cursor.execute(_q)

        for row in _cursor:
            _res.append(row)

    return _res


def display():
    _connection = psycopg2.connect(user=config.username, password=config.password, dbname=config.database,
                                   host=config.host, port=config.port)

    with _connection:
        _cursor = _connection.cursor()

        print()
        print('1. Total number of CPUs released each year:\n')
        _cursor.execute(query_1)
        for row in _cursor:
            print(row)

        print()
        print('2. Thread number distribution among the CPUs:\n')
        _cursor.execute(query_2)
        for row in _cursor:
            print(row)

        print()
        print('3. Minimum possible lithography resolution per release year (since 2017):\n')
        _cursor.execute(query_3)
        for row in _cursor:
            print(row)


if __name__ == '__main__':
    display()
