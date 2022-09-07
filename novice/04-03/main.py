from flask import Flask, render_template, request, redirect
import psycopg2
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index(): 
    conn = psycopg2.connect(
        host="localhost",
        database="project",
        user="postgres",
        password="rizabila")
    curs = conn.cursor()
    if request.method == "POST":
        nama = request.form.get("nama")
        nik = request.form.get("nik")
        departemen = request.form.get("departemen")
        jabatan = request.form.get("jabatan")
        email = request.form.get("email")
        query = f"insert into karyawan(nama, nik, departemen, jabatan, email) values('{nama}', '{nik}', '{departemen}', '{jabatan}', '{email}')"
        curs.execute(query)
        conn.commit()

    print(request.method)
    query = f"select * from karyawan"
    curs.execute(query)
    data = curs.fetchall()
    curs.close()
    conn.close()
    return render_template("index.html", context=data)


# @app.route("/nama/<karyawan_id>")
# def index(karyawan_id):
#     conn = psycopg2.connect(
#         host="localhost",
#         database="project",
#         user="postgres",
#         password="rizabila"
#     )
#     curs = conn.cursor()
#     query = f"select * from karyawan where id = {karyawan_id}"
#     curs.execute(query)
#     data = curs.fetchone()
#     curs.close()
#     conn.close()
#     print(data)
#     return render_template("index.html", context=data)

# @app.route("/email/<karyawan_id>")
# def index(karyawan_id):
#     conn = psycopg2.connect(
#         host="localhost",
#         database="project",
#         user="postgres",
#         password="rizabila"
#     )
#     curs = conn.cursor()
#     query = f"select * from karyawan where id = {karyawan_id}"
#     curs.execute(query)
#     data = curs.fetchone()
#     curs.close()
#     conn.close()
#     print(data)
#     return render_template("index.html", context=data)

# @app.route("/absensi/<karyawan_id>")
# def index(karyawan_id):
#     conn = psycopg2.connect(
#         host="localhost",
#         database="project",
#         user="postgres",
#         password="rizabila"
#     )
#     curs = conn.cursor()
#     query = f"select * from karyawan where id = {karyawan_id}"
#     curs.execute(query)
#     data = curs.fetchone()
#     curs.close()
#     conn.close()
#     print(data)
#     return render_template("index.html", context=data)

@app.route("/delete/<karyawan_id>")
def delete(karyawan_id):
    conn = psycopg2.connect(
        host="localhost",
        database="project",
        user="postgres",
        password="rizabila"
    )
    curs = conn.cursor()
    query = f"delete from karyawan where id = {karyawan_id}"
    curs.execute(query)
    conn.commit()
    curs.close()
    conn.close()
    return redirect("/")
    
# @app.route("/update/<karyawan_id>", methods=["GET", "POST"])
# def update (karyawan_id):
#     conn = psycopg2.connect(
#         host="localhost",
#         database="project",
#         user="postgres",
#         password="rizabila"
#     )
#     curs = conn.cursor()
#     if request.method == "POST":
#         nama = request.form.get("nama")
#         detail = request.form.get("detail")
#         query = f"update karyawan set nama = '{nama}', detail = '{detail}' where id ={karyawan_id}"
#         curs.execute(query)
#         conn.commit()
#         return redirect("/")


#     query = f"select * from karyawan where id = {karyawan_id}"   
#     curs.execute(query)
#     data = curs.fetchone()
#         # conn.commit()
#     curs.close()
#     conn.close()
#     return render_template("update.html", context=data)

    
if __name__ == "__main__":
    app.run()