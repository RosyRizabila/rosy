# from logging import exception


try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="rizabila")

# except Exception as e:
#         print(e)

    curs = conn.cursor()

    nama = "derista"
    umur = 12
    query = f"insert into siswa(nama, umur) values('{nama}', {umur})"

    curs.execute(query)
    conn.commit()
    print("data masuk")
except Exception as e:
    print(e)