from flask import Flask, render_template, request
from datetime import datetime, timedelta
import math
import csv
import io
from flask import Response

app = Flask(__name__)

# Prime checker
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    root = int(math.sqrt(n)) + 1
    for i in range(3, root, 2):
        if n % i == 0:
            return False
    return True

# Chinese zodiac data
zodiac_animals = [
    "Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake",
    "Horse", "Goat"
]

# Partial range for demo
chinese_new_years = {
    1990: datetime(1990, 1, 27), 1991: datetime(1991, 2, 15), 1992: datetime(1992, 2, 4),
    1993: datetime(1993, 1, 23), 1994: datetime(1994, 2, 10), 1995: datetime(1995, 1, 31),
    1996: datetime(1996, 2, 19), 1997: datetime(1997, 2, 7), 1998: datetime(1998, 1, 28),
    1999: datetime(1999, 2, 16), 2000: datetime(2000, 2, 5), 2001: datetime(2001, 1, 24),
    2002: datetime(2002, 2, 12), 2003: datetime(2003, 2, 1), 2004: datetime(2004, 1, 22),
    2005: datetime(2005, 2, 9),  2006: datetime(2006, 1, 29), 2007: datetime(2007, 2, 18),
    2008: datetime(2008, 2, 7),  2009: datetime(2009, 1, 26), 2010: datetime(2010, 2, 14),
    2011: datetime(2011, 2, 3),  2012: datetime(2012, 1, 23), 2013: datetime(2013, 2, 10),
    2014: datetime(2014, 1, 31), 2015: datetime(2015, 2, 19), 2016: datetime(2016, 2, 8),
    2017: datetime(2017, 1, 28), 2018: datetime(2018, 2, 16), 2019: datetime(2019, 2, 5),
    2020: datetime(2020, 1, 25), 2021: datetime(2021, 2, 12), 2022: datetime(2022, 2, 1),
    2023: datetime(2023, 1, 22), 2024: datetime(2024, 2, 10), 2025: datetime(2025, 1, 29),
}

def get_chinese_zodiac(date):
    year = date.year
    new_year = chinese_new_years.get(year)
    if new_year and date < new_year:
        year -= 1
    return zodiac_animals[year % 12]

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        date_str = request.form['birthday']
        try:
            birthday = datetime.strptime(date_str, '%Y-%m-%d')
            for age in range(1, 121):
                try:
                    bday = birthday.replace(year=birthday.year + age)
                except ValueError:
                    bday = birthday.replace(month=2, day=28, year=birthday.year + age)

                days = (bday - birthday).days
                prime_year = is_prime(age)
                prime_days = is_prime(days)
                zodiac = get_chinese_zodiac(bday)
                if prime_year or prime_days:
                    results.append({
                        'age': age,
                        'birthday': bday.strftime('%Y-%m-%d'),
                        'days': days,
                        'prime_year': prime_year,
                        'prime_days': prime_days,
                        'zodiac': zodiac
                    })
        except ValueError:
            return render_template('index.html', error="Invalid date format. Use YYYY-MM-DD.")

    return render_template('index.html', results=results)

@app.route('/download', methods=['POST'])
def download():
    birthday = datetime.strptime(request.form['birthday'], '%Y-%m-%d')
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['Age', 'Birthday', 'Days Since Birth', 'Chinese Zodiac', 'Year Is Prime', 'Days Is Prime'])

    for age in range(1, 121):
        try:
            bday = birthday.replace(year=birthday.year + age)
        except ValueError:
            bday = birthday.replace(month=2, day=28, year=birthday.year + age)

        days = (bday - birthday).days
        prime_year = is_prime(age)
        prime_days = is_prime(days)
        if prime_year or prime_days:
            zodiac = get_chinese_zodiac(bday)
            writer.writerow([age, bday.strftime('%Y-%m-%d'), days, zodiac, prime_year, prime_days])

    output.seek(0)
    return Response(output, mimetype='text/csv', headers={'Content-Disposition': 'attachment; filename=prime_birthdays.csv'})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request
from datetime import datetime, timedelta
import math
import csv
import io
from flask import Response

app = Flask(__name__)

# Prime checker
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    root = int(math.sqrt(n)) + 1
    for i in range(3, root, 2):
        if n % i == 0:
            return False
    return True

# Chinese zodiac data
zodiac_animals = [
    "Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake",
    "Horse", "Goat"
]

# Partial range for demo
chinese_new_years = {
    1990: datetime(1990, 1, 27), 1991: datetime(1991, 2, 15), 1992: datetime(1992, 2, 4),
    1993: datetime(1993, 1, 23), 1994: datetime(1994, 2, 10), 1995: datetime(1995, 1, 31),
    1996: datetime(1996, 2, 19), 1997: datetime(1997, 2, 7), 1998: datetime(1998, 1, 28),
    1999: datetime(1999, 2, 16), 2000: datetime(2000, 2, 5), 2001: datetime(2001, 1, 24),
    2002: datetime(2002, 2, 12), 2003: datetime(2003, 2, 1), 2004: datetime(2004, 1, 22),
    2005: datetime(2005, 2, 9),  2006: datetime(2006, 1, 29), 2007: datetime(2007, 2, 18),
    2008: datetime(2008, 2, 7),  2009: datetime(2009, 1, 26), 2010: datetime(2010, 2, 14),
    2011: datetime(2011, 2, 3),  2012: datetime(2012, 1, 23), 2013: datetime(2013, 2, 10),
    2014: datetime(2014, 1, 31), 2015: datetime(2015, 2, 19), 2016: datetime(2016, 2, 8),
    2017: datetime(2017, 1, 28), 2018: datetime(2018, 2, 16), 2019: datetime(2019, 2, 5),
    2020: datetime(2020, 1, 25), 2021: datetime(2021, 2, 12), 2022: datetime(2022, 2, 1),
    2023: datetime(2023, 1, 22), 2024: datetime(2024, 2, 10), 2025: datetime(2025, 1, 29),
}

def get_chinese_zodiac(date):
    year = date.year
    new_year = chinese_new_years.get(year)
    if new_year and date < new_year:
        year -= 1
    return zodiac_animals[year % 12]

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        date_str = request.form['birthday']
        try:
            birthday = datetime.strptime(date_str, '%Y-%m-%d')
            for age in range(1, 121):
                try:
                    bday = birthday.replace(year=birthday.year + age)
                except ValueError:
                    bday = birthday.replace(month=2, day=28, year=birthday.year + age)

                days = (bday - birthday).days
                prime_year = is_prime(age)
                prime_days = is_prime(days)
                zodiac = get_chinese_zodiac(bday)
                if prime_year or prime_days:
                    results.append({
                        'age': age,
                        'birthday': bday.strftime('%Y-%m-%d'),
                        'days': days,
                        'prime_year': prime_year,
                        'prime_days': prime_days,
                        'zodiac': zodiac
                    })
        except ValueError:
            return render_template('index.html', error="Invalid date format. Use YYYY-MM-DD.")

    return render_template('index.html', results=results)

@app.route('/download', methods=['POST'])
def download():
    birthday = datetime.strptime(request.form['birthday'], '%Y-%m-%d')
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['Age', 'Birthday', 'Days Since Birth', 'Chinese Zodiac', 'Year Is Prime', 'Days Is Prime'])

    for age in range(1, 121):
        try:
            bday = birthday.replace(year=birthday.year + age)
        except ValueError:
            bday = birthday.replace(month=2, day=28, year=birthday.year + age)

        days = (bday - birthday).days
        prime_year = is_prime(age)
        prime_days = is_prime(days)
        if prime_year or prime_days:
            zodiac = get_chinese_zodiac(bday)
            writer.writerow([age, bday.strftime('%Y-%m-%d'), days, zodiac, prime_year, prime_days])

    output.seek(0)
    return Response(output, mimetype='text/csv', headers={'Content-Disposition': 'attachment; filename=prime_birthdays.csv'})

import os

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
