### Información del repositorio
En este repositorio encontramos la entrega del seminario 3 de la asignatura SCAV (parte de vídeo).

Para poder utilizarlo correctamente necesitamos el vídeo "Big Buck Bunny", incluído en el repositorio.

Tenemos 4 archivos .py y en cada de uno de ellos encontramos una explicación detallada sobre cómo utilizarlos:


##  **ex1.py**
Obtenemos el vídeo anterior en 4 nuevos formatos*:
- Resolución 720p con códec de video vp8.
- Resolución 480p con códec de video vp9.
- Resolución 360x240 con códec de video .h265.
- Resolución 160x120 con códec de video av1.

*Los formatos no son exactamente los definidos ya que he priorizado conservar el aspect ratio. En caso de querer forzarlo se puede utilizar el siguiente código:

`$ ffmpeg -i <input_video> -s 720x480 <output_video>`


##  **ex2.py**
Tras ejecutar el script anterior, gracias a este podemos empaquetar todos los vídeos obtenidos en un único container (4 canales de vídeo y 4 de audio).

<img src="https://drive.google.com/uc?export=view&id=1uOJt5dCAuRYckoc0V5GL0OzgB60ha037" width="600">

A través de un reproductor de vídeo como puede ser VLC podemos cambiar entre los distintos formatos. Podemos observar como, por ejemplo, se ve con mayor calidad el vídeo de 480p con codec vp9 que el de 720p con codec vp8. Esto puede deberse a la compatibilidad entre los códecs y el tipo de contenedor.


##  **ex3.py**
En este script realizamos un steaming en la red local del vídeo generado en el script anterior. Para poder visualizarlo simplemente tenemos que acceder a la url a través de la cual lo compartimos.

<img src="https://drive.google.com/uc?export=view&id=1bhuSNG4dfAXGMzM5dHiu7ZUqkKUk0wn1"  width="300" height ="200">     <img src="https://drive.google.com/uc?export=view&id=1Vw9Bos3Ut5B-6EatIxWLux96EKwWx7uj" width="300" height ="200">


##  **ex4.py**
En este script encontramos un menú que nos permite seleccionar cuál de los scripts anteriores queremos ejecutar.

<img src="https://drive.google.com/uc?export=view&id=19B9Q_6w9t7t89fs0w0-kmlUP8ZtRP7O2"  width="300">
