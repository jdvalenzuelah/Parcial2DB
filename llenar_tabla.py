"""
Universidad del valle de Guatemala
Josue Valenzuela
Parcial 2 DB
"""

import sqlite3 as sql
import random

conn = sql.connect('parcial2.db')
cursor = conn.cursor()

"""
Create tables:
    cliente (id, nit, nombre, credito)
    tienda (id, nombre, direccion)
    compra (id, cliente_id, tienda_id, total, fecha)
"""

cursor.execute('CREATE TABLE cliente(id INT PRIMARY KEY, nit INT, nombre VARCHAR, credito FLOAT)')
cursor.execute('CREATE TABLE tienda(id INT PRIMARY KEY, nombre VARCHAR, direccion VARCHAR)')
cursor.execute('''CREATE TABLE compra(
    id INT PRIMARY KEY,
    cliente_id INT,
    tienda_id INT,
    total FLOAT,
    fecha VARCHAR,
    FOREIGN KEY(cliente_id) REFERENCES cliente(id),
    FOREIGN KEY(tienda_id) REFERENCES tienda(id))''')

# Data to fill database
nameList = [
    'Thelma',  
    'Yuriko'  ,
    'Mathew'  ,
    'Lavona'  ,
    'Jamal'  ,
    'Rochell' , 
    'Willia' , 
    'Glen'  ,
    'Jenelle' , 
    'Nelson' , 
    'Katelyn', 
    'Mackenzie' , 
    'Carman' , 
    'Lindsy' , 
    'Sheree' , 
    'Dorinda' , 
    'Jenae' , 
    'Janee' , 
    'Twana' , 
    'Yee' , 
    'Frederic' , 
    'Jaqueline' , 
    'Shelby' , 
    'Trista' , 
    'Daron' , 
    'Nikita' , 
    'Cristi',  
    'Margrett' , 
    'Chanel  '
    ]

lastnameList = [
    'Wilkins',
    'Santana',
    'Henderson',
    'Sosa',
    'Price',
    'Church',
    'Branch',
    'Spencer',
    'Sampson',
    'Burton',
    'Baker',
    'Lin',
    'Sheppard',
    'Bray',
    'Haney',
    'Morales',
    'Gilbert',
    'Rosario',
    'Rocha',
    'Copeland'
]

addressList = [
    '9072 South Leatherwood Ave.',
    'Ladson, SC 29456',
    '574 Roosevelt St.',
    'Osseo, MN 55311',
    '7704 Marsh Ave.',
    'Reidsville, NC 27320',
    '292 Fairground Street',
    'Vienna, VA 22180',
    '81 Amherst Dr.',
    'Florence, SC 29501',
    '949 Ketch Harbour Street',
    'Naugatuck, CT 06770',
    '988 Sunnyslope St.',
    'Akron, OH 44312',
    '121 North Harvey Dr.',
    'Bartlett, IL 60103',
    '8661 Lakeshore Ave.',
    'Southington, CT 06489',
    '7554 N. Arcadia St.',
    'Dearborn Heights, MI 48127',
    '173 Howard St.',
    'Graham, NC 27253',
    '525 Garfield St.',
    'Pittsford, NY 14534',
    '9259 Myrtle St.',
    'Morganton, NC 28655',
    '396 Santa Clara Dr.',
    'Murrells Inlet, SC 29576',
    '52 Henry St.',
    'Zeeland, MI 49464',
    '1 Bridge Drive',
    'Jamaica Plain, MA 02130',
    '20 Jackson St.',
    'Canonsburg, PA 15317',
    '5 Richardson Avenue',
    'Melrose, MA 02176',
    '266 La Sierra Drive',
    'Lakeville, MN 55044',
    '66 W. Essex Drive',
    'Greenville, NC 27834'
]

storeNameList = [
    'Mia bella',
    'Glam rose',
    'Honey Shop',
    'Viabella',
    'La Musa',
    'Fragatta Boutique',
    'Las flores',
    'Princess',
    'Pink Cake',
    'El encanto',
    'My Closet',
    'Bad Girl',
    'Aurora',
    'Seduction',
    'Dulce Luna',
    'Aqua marina',
    'Niña Bonita',
    'Cristal Rosa',
    'Venus Shop',
    'Studio M'
]

"""
Function to fill database with random data
"""
def generate_random_name():
    """
    Generates a random full Name picking random firstname and lastname from a pre-populated list
    """
    name = random.choice(nameList)
    lastname = random.choice(lastnameList)
    fullname = f'{name} {lastname}'
    return fullname

def generate_nit():
    """
    Generate a random 7 digit number representing the NIT
    """
    nit = random.randint(1111111, 9999999)
    return nit

def generate_date():
    """
    Generate random date dd/mm/yyyy
    """
    day = random.randint(0,28)
    day = day if day > 9 else f'0{day}'
    month = random.randint(1,12)
    month = month if month > 9 else f'0{month}'
    year = random.randint(2012, 2019) 
    date = f'{year}-{month}-{day}'
    return date

def insert_cliente(id):
    """
    Inserts a random client with a random name, nit and credito.
    """
    name = generate_random_name()
    nit = generate_nit()
    credito = random.randrange(1000, 10000)
    query = f"INSERT INTO cliente VALUES({id}, {nit}, '{name}', {credito})"
    cursor.execute(query)
    return query

def insert_tienda(id):
    """
    Inserts a store selecting a random name and address from pre-populated list
    """
    direccion = random.choice(addressList)
    nombre = random.choice(storeNameList)
    query = f"INSERT INTO tienda VALUES({id}, '{nombre}', '{direccion}')"
    cursor.execute(query)
    return query

def insert_compra(id, id_cliente, id_tienda):
    """
    Insert compra for id_cliente on id_tienda using a random date and random total
    """
    total = random.randrange(100, 10000)
    date = generate_date()
    query = f"INSERT INTO compra VALUES ({id}, {id_cliente}, {id_tienda}, {total}, '{date}')"
    cursor.execute(query)
    return query


if __name__ == '__main__':
    print('Generating...')
    for i in range(1, 500):
        insert_cliente(i)
        insert_tienda(i)
    for i in range(1, 1500):
        insert_compra(i, random.randint(1, 500), random.randint(1, 500))
    conn.commit()
    print('completed')
