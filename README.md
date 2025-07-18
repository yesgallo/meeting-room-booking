# 🗂 Gestor de Reservas de Salas de Reunión

Aplicación web desarrollada en Python con Flask para gestionar reservas de salas de reunión. Implementa Programación Orientada a Objetos y el patrón Repository.

---

## 🎯 Funcionalidades

* Alta de usuarios y salas ✅
* Reservas con validación de fechas y solapamiento ✅
* Consultas de reservas por usuario o por sala ✅
* Interfaz minimalista con Bootstrap 5 ✅
- Docker ready 🐳

---

## 🧱 Estructura del Proyecto

```
meeting-room-booking/
├── src/
│   ├── main.py                  
│   ├── templates/             
│   ├── models/                 
│   ├── repositories/            
│   ├── services/              
├── requirements.txt             
├── Dockerfile            
├── README.md                  
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


## 🧠 Diseño aplicado

* Programación Orientada a Objetos (POO)
* Patrón de Diseño: **Repository**
* Frontend con **Bootstrap 5**
* Estructura clara y mantenible

---

## 💡 Ideas futuras (bonus)

* Exportar reservas a PDF
* Login para administrador

---

## ✨ Créditos

Desarrollado por un Yesica Gallo para **¡aprobar Practicas Profesionalizantes III!** 🤖 
