from flask import Flask, render_template, request, redirect, url_for, flash
from services.booking_service import BookingService
from services.user_service import UserService
from services.room_service import RoomService
import webbrowser
import threading


app = Flask(__name__)
app.secret_key = "supersecretkey"

# Inicializar servicios
user_service = UserService()
room_service = RoomService()
booking_service = BookingService(user_service, room_service)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "POST":
        username = request.form["username"]
        user_service.create_user(username)
        flash(f"Usuario '{username}' creado con éxito!", "success")
        return redirect(url_for("users"))
    
    # CORREGIDO: Pasar la lista de usuarios al template
    # El template users.html espera una variable llamada 'users' con objetos User
    users_list = list(user_service.repo.users.values())  # Obtener los objetos User, no solo las claves
    return render_template("users.html", users=users_list)

@app.route("/rooms", methods=["GET", "POST"])
def rooms():
    if request.method == "POST":
        roomname = request.form["roomname"]
        room_service.create_room(roomname)
        flash(f"Sala '{roomname}' creada con éxito!", "success")
        return redirect(url_for("rooms"))
    
    # CORREGIDO: Pasar la lista de salas al template
    # Similar al problema con usuarios, necesitamos pasar los objetos Room
    rooms_list = list(room_service.repo.rooms.values())
    return render_template("rooms.html", rooms=rooms_list)

@app.route("/book", methods=["GET", "POST"])
def book():
    if request.method == "POST":
        username = request.form["username"]
        roomname = request.form["roomname"]
        start = request.form["start"].replace("T", " ")[:16]
        end = request.form["end"].replace("T", " ")[:16]
        
        # CORREGIDO: Ahora book_room() devuelve True/False correctamente
        result = booking_service.book_room(username, roomname, start, end)
        if result:
            flash("Reserva realizada con éxito!", "success")
        else:
            flash("Conflicto de horario o datos inválidos. La reserva NO se realizó.", "danger")
        return redirect(url_for("book"))
    
    # CORREGIDO: El problema principal estaba aquí
    # El template book.html espera las claves (nombres) como strings, no objetos
    # Por eso usamos .keys() para obtener solo los nombres
    usuarios = list(user_service.repo.users.keys())  # Lista de nombres de usuario
    salas = list(room_service.repo.rooms.keys())     # Lista de nombres de salas
    
    # Debug: Agregar estas líneas para verificar que los datos se están pasando correctamente
    print(f"DEBUG: Usuarios disponibles: {usuarios}")
    print(f"DEBUG: Salas disponibles: {salas}")
    
    return render_template("book.html", usuarios=usuarios, salas=salas)

@app.route("/consult", methods=["GET"])
def consult():
    user_query = request.args.get("user")
    room_query = request.args.get("room")
    bookings = []
    
    if user_query:
        bookings = booking_service.get_bookings_by_user(user_query)
        flash(f"Mostrando reservas para usuario '{user_query}'", "info")
    elif room_query:
        bookings = booking_service.get_bookings_by_room(room_query)
        flash(f"Mostrando reservas para sala '{room_query}'", "info")
    
    return render_template("consult.html", bookings=bookings)


def open_browser():
    import time
    time.sleep(1)
    webbrowser.open("http://127.0.0.1:5000")

if __name__ == "__main__":
    threading.Thread(target=open_browser).start()
    app.run(debug=True)





    