# 🛠️ Token Formatter

**Token Formatter** es una herramienta sencilla y práctica diseñada para procesar y formatear datos de tokens. 💾  
Permite separar y guardar la información en diferentes formatos según las necesidades del usuario.  

---

## 🌟 **Características**
- **Opciones de formato:**  
  - 🔑 Solo `Token`.  
  - 📧 `Email:Pass`.  
  - 🧩 `Email:Pass:Token`.  
- **Interfaz en consola interactiva.**  
- Detecta y notifica sobre entradas con formato inválido. ⚠️  
- Guarda automáticamente los resultados en un archivo con una carpeta organizada por la fecha y hora. 📂  
- **Colorida interfaz visual** gracias a las librerías `fade`, `colorama` y `pystyle`. 🎨  
- Sistema robusto para manejar errores y salidas seguras.  

---

## 🖥️ **Requisitos**
- Python 3.8 o superior.  
- Librerías necesarias:  
  ```bash
  pip install colorama pystyle fade
  ```

---

## 🚀 **Cómo usar**
1. Clona el repositorio en tu máquina local.  
   ```bash
   git clone https://github.com/tuusuario/TokenFormatter.git
   cd TokenFormatter
   ```
2. Asegúrate de que tienes un archivo llamado `tokens.txt` en el mismo directorio del script.  
   - Este archivo debe contener líneas en el formato:  
     ```
     email:password:token
     ```
3. Ejecuta el programa.  
   ```bash
   python main.py
   ```
4. Sigue las instrucciones en la consola:  
   - Selecciona el formato que deseas extraer.  
   - Los resultados se guardarán automáticamente en la carpeta `output`.

---

## 📋 **Formato del archivo de entrada**
El archivo `tokens.txt` debe contener líneas con los siguientes formatos:  
- **Formato válido (separados por `:`):**  
  ```
  email:password:token
  ```

- **Ejemplo de archivo de entrada:**  
  ```plaintext
  example1@gmail.com:password123:token12345
  example2@gmail.com:password456:token67890
  ```

---

## 📂 **Salida de resultados**
- Los resultados se guardan automáticamente en una carpeta con la fecha y hora como nombre, por ejemplo:  
  ```
  output/
      15-11-24 16-17-39/
          tokens.txt
  ```
- Este archivo contiene los datos formateados según la opción seleccionada.

---

## 🛑 **Errores comunes y cómo manejarlos**
- **Archivo no encontrado:**  
  Asegúrate de que `tokens.txt` existe en el mismo directorio del programa.
- **Formato inválido:**  
  El programa notificará y omitirá cualquier línea con formato incorrecto.  

---

## 📝 **Personalización**
Si deseas cambiar el formato de la hora que se muestra, modifica la función `obtener_hora_actual` en el archivo `main.py`.  
Por ejemplo, para usar el formato `Hora:Minuto AM/PM`:  
```python
def obtener_hora_actual():
    return datetime.now().strftime('%I:%M %p')
```

---

## 🛡️ **Licencia**
Este proyecto está bajo la Licencia MIT. Puedes usarlo, modificarlo y compartirlo libremente.  

---

## ✨ **Contribuciones**
¡Contribuciones, sugerencias y reportes de errores son bienvenidos! 🫶  
Por favor, abre un issue o envía un pull request en este repositorio.  

---

## 🤝 **Contacto**
Creado con ❤️ por [SwiftDesk](https://github.com/swiftdeskk).  
Si tienes dudas o sugerencias, no dudes en escribirme.
