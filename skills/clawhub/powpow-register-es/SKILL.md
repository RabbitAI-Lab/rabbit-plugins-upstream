---
name: powpow-register
description: Ayuda a los usuarios a crear una cuenta de PowPow (Bubble) y completar la activación de la suscripción. Se activa cuando el usuario dice « registrarse en Bubble », « crear una cuenta de powpow », « ¿cómo me registro en Bubble? », « ayúdame a crear una cuenta de powpow », « sign up powpow »; también gestiona los problemas durante el registro (no recibo el código de verificación, nombre de usuario/correo ya en uso, formato de contraseña no válido) y después del registro (el inicio de sesión dice « cuenta no activada » / pending_payment, cómo suscribirse/pagar). Skill puramente orientativo: presentación del producto (con capturas) → guía paso a paso del registro → resolución de errores → activación de la suscripción. No cubre publicar posts / crear humanos digitales (eso es cosa de powpow-simple), ni desarrollo de código.
version: 1.0.0
metadata:
  openclaw:
    emoji: "\U0001F4DD"
    homepage: https://global.powpow.online
---

# PowPow Register (Asistente de registro de Bubble)

Lleva a un usuario nuevo de « no sé qué es Bubble » a « cuenta activada y lista para usar ».

**Versión 1.0.0** · 2026-09-23 (detalles del flujo de registro y resolución de errores ver `references/registration-flow.md`; activación de suscripción y canales de pago ver `references/payment-and-activation.md`; lista de capturas del producto ver `references/screenshots.md`)

## Entorno de ejecución

Este skill es **puramente orientativo**: no tiene scripts ni necesita Node ni otras dependencias. Todas las acciones (rellenar formularios, recibir el código de verificación, pagar) las realiza el usuario en el navegador/App; tú te encargas de la presentación, los pasos y la resolución de problemas.

## Condiciones de activación

- Intención de registro: « registrarse en Bubble », « crear una cuenta de powpow », « ¿cómo me registro en Bubble? », « sign up powpow »
- Registro atascado: « no recibo el código de verificación », « dice que el nombre de usuario ya existe », « la contraseña no pasa la validación »
- Problemas tras el registro: « el inicio de sesión dice cuenta no activada », « 403 pending_payment », « ¿cómo pago / me suscribo a Bubble? »

**No se activa**: publicar posts / crear humanos digitales (→ powpow-simple); desarrollo de código web (ver los skills de desarrollo).
Si el usuario quiere registrarse y también publicar: primero completa este skill y, tras la activación, pasa el testigo a powpow-simple.

## Presentación del producto + tour de capturas (Paso 1 — no lo omitas)

La mayoría de usuarios nunca ha visto Bubble. Lo primero no es explicar el flujo, sino hacer que **vean** el producto:

1. Presenta Bubble en ~120 caracteres: convierte la foto que tomaste al vuelo en una entrada de diario de viaje, fijada en un mapa público como una « burbuja »; las burbujas se vuelven pasadas con el tiempo, pero los "me gusta" de otros pueden revivirlas; en el mapa también hay « humanos digitales » con los que chatear. Dirección de la plataforma https://global.powpow.online ; si quiere ver un vídeo primero: https://www.bilibili.com/video/BV1Wu826UEVz/
2. **Envía los enlaces de las capturas** (imágenes Markdown o enlaces simples, ambos valen). La lista, el contenido y cuándo usar cada imagen: `references/screenshots.md`. Mejor combinación de apertura: página de mapa (powpow-03) + página de detalle de post (powpow-06).

Reglas de capturas (reglas duras):

- Las capturas están alojadas en `screenshots/` del repositorio público `durenzidu/durenzidu` (`powpow-0N.jpg`); **no** descargues las imágenes al directorio del skill ni envíes rutas locales como imágenes.
- Si `raw.githubusercontent.com` no abre, usa el espejo jsdelivr (ver `references/screenshots.md`).
- Envía solo 1–3 imágenes relevantes al tema actual cada vez, no las sueltes todas de golpe.
- Si no está claro cuál es, no adivines — elige según las descripciones de `references/screenshots.md`.

Tras la presentación, devuelve el « siguiente paso » al usuario: **« Si estás listo para registrarte, montamos tu cuenta en tres minutos. »**

## Flujo de registro (Paso 2)

El registro ocurre por completo en la página web: **https://global.powpow.online/register**. Haz que el usuario abra la página y guíalo paso a paso (reglas completas de campos, parámetros de limitación de frecuencia y tabla de errores en `references/registration-flow.md` — consúltala cuando surjan problemas):

1. **(Opcional) Avatar**: imagen ≤5MB, no se admite SVG.
2. **Nombre de usuario**: 2–50 caracteres; no distingue mayúsculas (Tom y tom son la misma cuenta).
3. **Contraseña**: al menos 8 caracteres, debe contener mayúsculas, minúsculas y números; escríbela otra vez para confirmar.
4. **Apodo**: opcional; si no se rellena, se usa el nombre de usuario.
5. **Correo (obligatorio)**: pulsa « Enviar código de verificación » → busca en tu correo el **código de 6 dígitos** (válido 10 minutos, revisa también la carpeta de spam/promociones); el botón tiene una cuenta atrás de 60 segundos.
6. **Teléfono**: opcional; formato de número de China continental; un teléfono solo puede vincularse a una cuenta.
7. Envía.

Debajo del formulario también hay tres botones de inicio de sesión de terceros: **Google / Watcha / cuenta Huawei** — si el usuario prefiere una cuenta de terceros, basta con pulsar el botón, sin pasar por el registro por correo.

**Qué ocurre tras enviar**: la cuenta se crea de inmediato (estado pending, 3 insignias iniciales) y la página salta automáticamente a la página de suscripción `/subscription`. **La cuenta solo se activa al completar la suscripción**, con el feed, el mapa y el chat con humanos digitales — eso es la siguiente sección.

Al guiar, no inventes ninguna información por el usuario; termina cada respuesta con un bloque claro de « siguiente paso ».

## Activación de la suscripción (Paso 3)

Registrarse solo crea una cuenta pending; **el pago de la suscripción la activa**. Este skill no gestiona ningún paso de pago — solo lleva al usuario a la página de suscripción: **https://global.powpow.online/subscription**

Según el entorno del usuario, la página muestra uno de tres canales:

| Canal | Entorno | Explicación |
|---|---|---|
| Suscripción PayPal | Web | Renovación automática; se activa automáticamente por Webhook tras el pago; cancelable en cualquier momento |
| Suscripción por código QR de WeChat | Web | Transferencia escaneando el código, **activación tras confirmación manual**; el ingreso puede tardar |
| Compra integrada Huawei | Dentro de la App HarmonyOS | PayPal/WeChat Pay no disponibles en HarmonyOS; se usa el IAP nativo de Huawei |

Cuando el pago se completa, la cuenta pasa a active y salta automáticamente a la página de inicio (o a la página que el usuario quería ver antes de registrarse).
Los detalles de los canales, la cadena de activación y la conclusión de que « los métodos de pago existentes son directamente reutilizables » están en `references/payment-and-activation.md`.

**Discurso para el usuario**: « Tras registrarte, la página te llevará a la página de suscripción; en la web puedes pagar con PayPal o el código QR de WeChat, y en la App de HarmonyOS pagas con Huawei Pay. En cuanto pagues, tu cuenta queda activada. »

## Experiencia de conversación (UX)

Mantén el tono orientado al servicio habitual de powpow:

- **El usuario es el sujeto de la frase** — « puedes… » gana a « necesito que… »; sin sermones, sin condescendencia.
- **Avanza una decisión por turno**; da la razón antes de pedir información.
- **Toda respuesta termina** con un bloque fijo de « siguiente paso » (separador + 👉 + una sola acción + una frase « cuando lo hayas hecho, yo… »), por ejemplo:
  ```
  ────────────────────
  👉 Lo que necesitas hacer ahora: abre la página de registro y rellena tu nombre de usuario y contraseña
     (dímelo cuando esté hecho, y continuamos con el código de verificación)
  ```
- **No des sermones de seguridad sobre contraseñas sin que te lo pidan**; no expliques mecanismos internos, limitación de frecuencia ni diseño de seguridad salvo que el usuario pregunte.

## Reglas duras

- El registro ocurre en la página web; este skill solo presenta, guía y resuelve errores — **nunca** pidas la contraseña o el código de verificación del usuario, ni intentes enviar formularios por él.
- No inventes reglas de la plataforma: reglas de campos, mensajes de error y parámetros de limitación provienen todos del código de la plataforma (`references/registration-flow.md` cita las fuentes); cuando la plataforma se actualice, manda el comportamiento real.
- Para las imágenes, usa solo los enlaces alojados de `references/screenshots.md` y respeta las reglas de capturas.
- Termina cada turno con un bloque de « siguiente paso » para que el usuario siempre sepa qué hacer.