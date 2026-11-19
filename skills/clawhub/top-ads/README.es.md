# Denote Top Ads

[EN](README.md) · [ZH](README.zh.md) · [JA](README.ja.md) · [KO](README.ko.md) · ES · [NL](README.nl.md) · [DE](README.de.md) · [FR](README.fr.md)

Encuentra anuncios que te sirvan de referencia para tu próxima campaña. Denote sigue más de 10 millones de anuncios y actualiza sus clasificaciones cada semana. Con una cuenta gratuita puedes consultar tres listas de juegos o aplicaciones de la última semana completa, con hasta diez anuncios por lista. [Explorar Denote Top Ads](https://denote.net/top-ads).

![Accede a las tres clasificaciones semanales desde el menú lateral.](https://cdn.denote.net/denote/static/source/denote-top-ads/assets/screenshots/top-ads-navigation.jpg)

*Accede a las tres clasificaciones semanales desde el menú lateral.*

| Lista gratuita | Qué te permite descubrir |
| --- | --- |
| Anuncios populares | Los anuncios que más atención recibieron la semana pasada. |
| Anuncios en ascenso | Los que más ganaron en popularidad respecto a la semana anterior. |
| Anuncios nuevos | Los detectados por primera vez durante esa semana, ordenados por su popularidad inicial. |

![Anuncios populares de juegos del 9 al 15 de noviembre de 2026, por popularidad semanal.](https://cdn.denote.net/denote/static/source/denote-top-ads/assets/screenshots/trending-ads.jpg)

*Anuncios populares de juegos del 9 al 15 de noviembre de 2026, por popularidad semanal.*

![Anuncios de juegos que más ganaron en popularidad respecto a la semana anterior.](https://cdn.denote.net/denote/static/source/denote-top-ads/assets/screenshots/rising-ads.jpg)

*Anuncios de juegos que más ganaron en popularidad respecto a la semana anterior.*

![Anuncios de juegos recién detectados, ordenados por su popularidad inicial.](https://cdn.denote.net/denote/static/source/denote-top-ads/assets/screenshots/new-ads.jpg)

*Anuncios de juegos recién detectados, ordenados por su popularidad inicial.*

## Obtén tus primeras tres listas

Ejecuta este comando en tu espacio de trabajo de OpenClaw. Necesitas Python 3.

```sh
git clone https://github.com/Denote-Business/denote-top-ads.git skills/denote-top-ads
```

1. Abre una sesión nueva y pregunta «¿Qué anuncios puedo descubrir con Denote?».
2. [Crea una cuenta gratuita de Denote](https://denote.net/user/register). Si ya tienes cuenta, inicia sesión. Crea una clave de API de Denote con el permiso `top_ads:read` o añádelo a una clave existente.
3. Guarda la clave como `DENOTE_API_KEY` en la configuración de secretos de tu agente y pídele «Muéstrame los mejores anuncios de aplicaciones de la semana pasada». Recibirás las tres listas. Si omites la categoría, verás anuncios de juegos.

**Posición · Título · Anunciante · Formato · Plataformas · Vista previa**

## Consulta un anuncio en detalle

Prueba con «Abre el segundo anuncio en ascenso». Con Top Ads Pro o Business puedes consultar los datos disponibles de rendimiento y audiencia. Las tres listas semanales son gratuitas.

![Resumen de la creatividad de Vita Mahjong, con su formato e impresiones estimadas.](https://cdn.denote.net/denote/static/source/denote-top-ads/assets/screenshots/overview.jpg)

*Resumen de la creatividad de Vita Mahjong, con su formato e impresiones estimadas.*

![Evolución de la puntuación diaria de Vita Mahjong frente a las líneas de referencia.](https://cdn.denote.net/denote/static/source/denote-top-ads/assets/screenshots/data-trend.jpg)

*Evolución de la puntuación diaria de Vita Mahjong frente a las líneas de referencia.*

![Anuncios que utilizan la misma creatividad, con sus anunciantes y fechas de difusión.](https://cdn.denote.net/denote/static/source/denote-top-ads/assets/screenshots/related-ads.jpg)

*Anuncios que utilizan la misma creatividad, con sus anunciantes y fechas de difusión.*

![Alcance de Vita Mahjong por país, edad y género.](https://cdn.denote.net/denote/static/source/denote-top-ads/assets/screenshots/audience.jpg)

*Alcance de Vita Mahjong por país, edad y género.*
