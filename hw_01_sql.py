import psycopg2
import psycopg2.extras
from pprint import pprint as pp
from tabulate import tabulate

conn = psycopg2.connect("host=localhost port=5432 dbname=train user=postgres password=1")
cursor = conn.cursor()  # cursor_factory=psycopg2.extras.DictCursor)

query = """
CREATE TABLE IF NOT EXISTS train (
    id INTEGER PRIMARY KEY,
    age INTEGER,
    gender INTEGER,
    height REAL,
    weight REAL,
    ap_hi INTEGER,
    ap_lo INTEGER,
    cholesterol INTEGER,
    gluc INTEGER,
    smoke BOOLEAN,
    alco BOOLEAN,
    active BOOLEAN,
    cardio BOOLEAN
)
"""
cursor.execute(query)
conn.commit()

with open('mlbootcamp5_train.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    # Skip the header row
    next(reader)
   for row in reader:
        cursor.execute(
            "INSERT INTO train VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            row
        )

conn.commit()


def fetch_all(cursor):
    colnames = [desc[0] for desc in cursor.description]
    records = cursor.fetchall()
    return [{colname: value for colname, value in zip(colnames, record)} for record in records]


"""
cursor.execute("")
records = cursor.fetchall()
print(records)
"""

""" 1.Сколько мужчин и женщин представлено в этом наборе данных? """
cursor.execute(
   """
    SELECT gender, AVG(height)
    from mytable
    GROUP BY gender;
   """
   )
print('Задание 1')
print(tabulate(fetch_all(cursor), "keys", "psql"))


""" 2. Кто в среднем реже указывает, что употребляет алкоголь – мужчины или женщины? """

cursor.execute(
    """
    SELECT gender, AVG(alco)
    FROM mytable
    GROUP BY gender;  
    """
)

print('Задание 2')
print(tabulate(fetch_all(cursor), "keys", "psql"))


""" 3.Во сколько раз (округленно, round) процент курящих среди мужчин больше, чем процент
    курящих среди женщин (по крайней мере, по этим анкетным данным)? """

cursor.execute(
    """
    SELECT(
        (
              (SELECT COUNT(smoke)
              FROM mytable
              WHERE gender='2'
              AND
              smoke='1')/
              (SELECT COUNT(gender)
              FROM mytable
              WHERE gender='2')
      )/
     (
              (SELECT COUNT(smoke)
              FROM mytable
              WHERE gender='1'
              AND
              smoke='1')/
              (SELECT COUNT(gender)
              FROM mytable
              WHERE gender='1')
    ));
    """
 )
 print('Задание 3')
print(tabulate(fetch_all(cursor), "keys", "psql"))


""" 4.В чём здесь измеряется возраст? На сколько месяцев (примерно) отличаются медианные значения
    возраста курящих и некурящих? """
    
cursor.execute(
    """
        SELECT DISTINCT abs(
            (SELECT median(age) / 30 from mytable where smoke='1') - \
            (SELECT median(age) / 30 from mytable where smoke='0')
        )::int as difference
        FROM mytable;
    """
) 
print('Задание 4')
print(tabulate(fetch_all(cursor), "keys", "psql"))



""" 5.  1. Создайте новый признак age_years – возраст в годах, округлив до целых (round).
       Для данного примера отберите курящих мужчин от 60 до 64 лет включительно.
        2. Категории уровня холестрина на рисунке и в наших данных отличаются. Отображение значений на картинке
       в значения признака cholesterol следующее: 4 ммоль/л -> 1, 5-7 ммоль/л -> 2, 8 ммоль/л -> 3.
        3. Интересуют 2 подвыборки курящих мужчин возраста от 60 до 64 лет включительно:
       первая с верхним артериальным давлением строго меньше 120 мм рт.ст. и концентрацией холестерина – 4 ммоль/л,
       а вторая – с верхним артериальным давлением от 160 (включительно) до 180 мм рт.ст. (не включительно)
       и концентрацией холестерина – 8 ммоль/л.
       Во сколько раз (округленно, round) отличаются доли больных людей (согласно целевому признаку, cardio)
       в этих двух подвыборках?
       """

cursor.execute(
    """
    """
)
print('Задание 5')
print(tabulate(fetch_all(cursor), "keys", "psql"))


""" 6. Постройте новый признак – BMI (Body Mass Index). Для этого надо вес в килограммах
    поделить на квадрат роста в метрах. Нормальными считаются значения BMI от 18.5 до 25.
    Выбрать верные утверждения:
    1. Медианный BMI по выборке превышает норму.
    2. У женщин в среднем BMI ниже, чем у мужчин.
    3. У здоровых в среднем BMI выше, чем у больных.
    4. В сегменте здоровых и непьющих мужчин в среднем BMI ближе к норме,
       чем в сегменте здоровых и непьющих женщин.
"""
cursor.execute(
    """
    """
)
print('Задание 6.1')
print(tabulate(fetch_all(cursor), "keys", "psql"))

cursor.execute(
    """
    """
)
print('Задание 6.2')
print(tabulate(fetch_all(cursor), "keys", "psql"))  

cursor.execute(
    """
    """
)
print('Задание 6.3')
print(tabulate(fetch_all(cursor), "keys", "psql"))  

cursor.execute(
    """
    """
)
print('Задание 6.4')
print(tabulate(fetch_all(cursor), "keys", "psql"))  

"""" 7. Отфильтруйте следующие сегменты пациентов (считаем это ошибками в данных):
    1. Указанное нижнее значение артериального давления строго выше верхнего.
    2. Рост строго меньше 2.5%-перцентили или строго больше 97.5%-перцентили.
       (используйте pd.Series.quantile, если не знаете, что это такое – прочитайте)
    3. Вес строго меньше 2.5%-перцентили или строго больше 97.5%-перцентили.
    Сколько процентов данных (округленно, round) мы выбросили? """

cursor.execute(
    """
    """
)
print('Задание 7, квантили')
print(tabulate(fetch_all(cursor), "keys", "psql"))

""" Выборки показали , что в предложенных для анализа данных рост и вес должны соответствовать следующим неравенствам :
    150 <= Рост <=180
    51 <= Вес <= 108
    """

cursor.execute(
    """
    """
 )
print('Задание 7, ответ')
print(tabulate(fetch_all(cursor), "keys", "psql")) 
