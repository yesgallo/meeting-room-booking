# 🗂 Gestor de Reservas de Salas de Reunión

Aplicación web desarrollada en Python con Flask para gestionar reservas de salas de reunión. Implementa Programación Orientada a Objetos y el patrón Repository.

---

## 🎯 Funcionalidades

* Crear usuarios ✅
* Crear salas de reunión ✅
* Realizar reservas con validación de horario ✅
* Consultar reservas por usuario o por sala ✅
* Feedback visual con Bootstrap 5 ✅

---

## 🧱 Estructura del Proyecto

```
meeting-room-booking/
├── src/
│   ├── main.py                  # Punto de entrada
│   ├── templates/               # Archivos HTML
│   ├── models/                  # Clases User, Room, Booking
│   ├── repositories/            # Repositorios de usuarios, salas y reservas
│   ├── services/                # Lógica de negocio
├── requirements.txt            # Dependencias
├── README.md                   # Este archivo
```

---

## ⚙️ Requisitos

* Python 3.9+
* Flask

Instalación de dependencias:

```bash
pip install -r requirements.txt
```

---

## 🚀 Cómo ejecutar la app

Desde la raíz del proyecto:

```bash
python src/main.py
python3 src/main.py
```

Esto:

* Inicia el servidor Flask
* Abre el navegador automáticamente en `http://127.0.0.1:5000`

---

## 📦 Estructura de Carpetas Importante

* `templates/` debe contener los archivos HTML correctamente nombrados:

  * `index.html`
  * `users.html`
  * `rooms.html`
  * `book.html`
  * `consult.html`

---

## 🧠 Diseño aplicado

* Programación Orientada a Objetos (POO)
* Patrón de Diseño: **Repository**
* Frontend con **Bootstrap 5**
* Estructura clara y mantenible

---

## 💡 Ideas futuras (bonus)

* Validación de formularios con JS
* Exportar reservas a PDF
* Login para administrador
* Dockerfile y despliegue en la nube

---

## ✨ Créditos

Desarrollado por un Yesica Gallo para **¡aprobar Practicas Profesionalizantes III!** 🤖 
