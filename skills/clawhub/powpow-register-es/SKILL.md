---
name: powpow-register
description: Ayuda al usuario a completar en la conversación el registro en PowPow (Burbuja), la activación de la suscripción con Alipay y el inicio de sesión con un clic. El agent rellena el formulario en su nombre (incluida la subida del avatar), envía el código de verificación por correo, crea el pedido de pago y hace seguimiento hasta que llega el cobro; el usuario solo proporciona la información básica, consulta una vez el código en su correo y paga en la caja de Alipay, sin salir en ningún momento de la conversación. Se activa cuando el usuario dice «regístrate en Burbuja», «crear una cuenta de powpow», «cómo me registro en Burbuja», «ayúdame a crear una cuenta de powpow», «sign up powpow»; también resuelve atascos del registro (no llega el código de verificación, nombre de usuario o correo ocupados) y problemas de activación (al iniciar sesión aparece «cuenta no activada» / pending_payment, cómo pagar la suscripción). Requiere Node ≥ 18; si no está disponible, retrocede automáticamente al modo de guía pura. No incluye publicar posts ni crear humanos digitales (eso es cosa de powpow-simple) ni desarrollo de código.
version: 2.0.1
metadata:
  openclaw:
    emoji: "\U0001F4DD"
    homepage: https://global.powpow.online
---

# PowPow Register (asistente de registro en Burbuja)

Lleva a un usuario nuevo desde «no sé qué es Burbuja» hasta «cuenta activada, sesión iniciada con un clic, a jugar» — todo dentro de la conversación. El usuario solo tiene que salir de la conversación dos veces: **ir al correo a mirar el código de verificación** y **pagar en la caja de Alipay** (el agent abre automáticamente la página de pago).

**Versión 2.0.1** · 2026-10-08 (desde v2 el modo es de gestión delegada en el agent: el contrato del script y la secuencia completa están en `references/agent-flow.md`; las reglas de campos, límites de frecuencia y resolución de errores en `references/registration-flow.md`; los canales de pago en `references/payment-and-activation.md`; el inventario de capturas del producto en `references/screenshots.md`. Desde v2.0.1 las capturas del producto viajan con la habilidad en `assets/screenshots/`, sin depender de un hospedaje externo de imágenes)

## Entorno de ejecución

- Script principal `scripts/powpow-register.mjs`: **cero dependencias**, requiere **Node ≥ 18**. Antes de empezar, ejecuta una vez `node scripts/powpow-register.mjs status` para confirmar que el entorno funciona.
- Todas las peticiones del script van únicamente al dominio oficial `https://global.powpow.online`.
- **Sin Node / si el script da errores**: retrocede automáticamente al modo de guía pura — entrega al usuario la página de registro https://global.powpow.online/register y la de suscripción https://global.powpow.online/subscription, y acompáñalo según `references/registration-flow.md`. No insistas una y otra vez con el script.
- Reanudación tras una interrupción de la conversación: ejecuta primero `status` para ver en qué punto del flujo estás y continúa desde ahí.

## Trigger Conditions

- Intención de registro: «regístrate en Burbuja», «crear una cuenta de powpow», «cómo me registro en Burbuja», «sign up powpow»
- Registro atascado: «no me llega el código de verificación», «dice que el nombre de usuario ya existe», «la contraseña nunca pasa la validación»
- Problemas tras el registro: «al iniciar sesión dice cuenta no activada», «403 pending_payment», «cómo se paga o se suscribe uno en Burbuja»

**No se activa para**: publicar posts ni crear humanos digitales (→ powpow-simple); desarrollo de código del lado web (ver habilidades de desarrollo). Si el usuario quiere registrarse y también publicar: completa primero esta habilidad y, tras la activación, pásalo a powpow-simple.

## Resumen del flujo

| Paso | Qué hace el agent | Qué hace el usuario |
|---|---|---|
| 1 Presentación del producto | Presenta + envía capturas | Echa un vistazo |
| 2 Confirmación de datos | Sugiere nombre de usuario/apodo, contraseña con dos opciones, pide el correo | Confirma, proporciona |
| 3 Envío del código | `send-code` | —— |
| 4 Lectura del código | —— | Va al correo, busca el código de 6 dígitos y lo envía de vuelta |
| 5 Envío del registro | `register` (con subida directa del avatar), gestiona errores automáticamente | —— |
| 6 Semi-sesión + pago | `login-link(pending)` → `create-order` → abre la caja → sondea `query` | Abre el enlace, paga |
| 7 Inicio de sesión formal | `refresh-login` → `login-link(home)` | Abre el enlace y entra al inicio |
| 8 Cierre | `cleanup` + entrega de credenciales + guía de uso + recomendación de plugins | Empieza a jugar |

## Paso 1: presentación del producto + capturas (no se puede saltar)

La mayoría de los usuarios nunca ha visto Burbuja. Lo primero no es explicar el flujo, sino hacer que **vea** el producto:

1. Presenta Burbuja en ~120 caracteres: convierte las fotos tomadas al vuelo en un diario de viaje, clavado en el mapa público como una «burbuja»; las burbujas pierden vigencia con el tiempo y los «me gusta» de otros pueden revivirlas; en el mapa también hay «humanos digitales» con los que se puede conversar. Dirección de la plataforma: https://global.powpow.online ; si quiere ver primero un vídeo: https://www.bilibili.com/video/BV1Wu826UEVz/
2. **Envía capturas**. Las capturas ya viajan con la habilidad en `assets/screenshots/powpow-0N.jpg` — envíalas directamente como archivos locales, sin necesidad de conexión. El inventario, el contenido de cada imagen y cuándo usarlas están en `references/screenshots.md`. La combinación más habitual al abrir: página del mapa (powpow-03) + página de detalle de un post (powpow-06).

Reglas de capturas (reglas firmes):

- Las capturas **ya van incluidas con la habilidad** en `assets/screenshots/` (`powpow-0N.jpg`) — envíalas directamente como archivos de imagen locales; sirven en cualquier entorno, incluidos aquellos donde GitHub no abre.
- Envía solo 1–3 imágenes relacionadas con el tema actual, no las pegues todas de golpe.
- Si por accidente faltan archivos del paquete, recurre a los enlaces hospedados listados en `references/screenshots.md` (ojo: puede que no abran en China continental).

Al terminar la presentación, deja la decisión en manos del usuario: **«Si quieres registrarte, en tres minutos dejamos la cuenta creada aquí en la conversación; solo tendrás que mirar una vez el código que llega a tu correo.»**

## Paso 2: confirmar los datos de registro (una pregunta por turno, no las preguntes todas de golpe)

- **Nombre de usuario** (obligatorio): **sugiere proactivamente uno** a partir del contexto de la conversación o del nombre de usuario del sistema (2~50 caracteres, sin distinguir mayúsculas de minúsculas); si el usuario asiente, se usa; si quiere cambiarlo, se cambia.
- **Contraseña** (obligatoria; primero ofrece dos opciones):
  - El usuario la proporciona → luego se pasa al script mediante una variable de entorno, **nunca como argumento de la línea de comandos**;
  - La genera el agent → ejecuta `node scripts/powpow-register.mjs gen-password` y **envía de inmediato la contraseña generada al usuario para que la guarde** (se muestra solo esta vez y no vuelve a aparecer).
- **Correo electrónico** (obligatorio): debe proporcionarlo el usuario — es el ancla de identidad de la cuenta, **no lo adivines por él**.
- **Apodo** (opcional): sugiere que por defecto coincida con el nombre de usuario.
- **Avatar** (opcional): si el usuario da la ruta de una imagen local (≤5 MB, no SVG), el script la sube directamente; si no, se omite (la plataforma usa el logo por defecto); si tienes capacidad de generar imágenes, puedes ofrecerte a crearle una.
- **Teléfono** (opcional, número de China continental): omítelo por defecto; pídelo solo si el usuario quiere vincularlo.

Una vez confirmado, puedes ejecutar `prepare-suggest --username U --nickname N --email E` para dejarlo anotado en el archivo de estado (así register no vuelve a pedirlo).

## Pasos 3–4: código de verificación por correo (la única parte que exige salir de la conversación)

```
node scripts/powpow-register.mjs send-code --email <correo>
```

Después dile claramente al usuario: **ve al correo y busca el código de verificación de 6 dígitos, válido durante 10 minutos; acuérdate de mirar también la carpeta de spam o correo publicitario**; cuando lo encuentre, que vuelva y te lo envíe. El envío tiene una espera de 60 segundos, no lo repitas en cadena.

## Paso 5: enviar el registro (gestión delegada en el agent)

```
POWPOW_REGISTER_PASSWORD=<contraseña> node scripts/powpow-register.mjs register --code <código> [--username U] [--nickname N] [--avatar <ruta de imagen local>] [--phone P]
```

Si tiene éxito, la cuenta queda creada (estado pending, con 3 insignias iniciales). Los errores habituales se gestionan automáticamente, sin interrumpir al usuario:

| Error | Gestión |
|---|---|
| 「用户名已存在」(el nombre de usuario ya existe) | Sugiere automáticamente una variante (nombre de usuario + número) y, cuando el usuario la confirma, reintenta directamente (el código sigue siendo válido, no hace falta reenviarlo) |
| 「邮箱已被使用」(el correo ya está en uso) | Pregunta al usuario: ¿cambias de correo, o en realidad ya tienes cuenta? (pásalo a inicio de sesión / recuperación de contraseña) |
| 「邮箱验证码错误或已过期」(código de verificación incorrecto o caducado) | Si pasaron más de 10 minutos → volver a `send-code` |
| Envío/registro demasiado frecuentes (429) | Espera 1 minuto y reintenta; basta con avisar al usuario |

## Paso 6: inicio de sesión con un clic (enlace 1) + pago

1. Nada más completar el registro con éxito:
   ```
   node scripts/powpow-register.mjs login-link --target pending
   ```
   Envía el enlace al usuario: **al abrirlo, el navegador cae directamente en la página de suscripción, ya con la sesión iniciada** — así la página de retorno puede mostrar correctamente «pago completado» cuando termine el pago. (En este estado, las páginas de contenido siguen redirigiéndose a la de suscripción: es el funcionamiento normal del muro de pago de la plataforma, no es un bug, y tampoco hace falta explicarle al usuario el mecanismo interno.)
2. Tres planes a elegir; muéstralos con su precio:
   - Mensual **¥6.99** (recomendado para empezar a probar) / Trimestral **¥19.99** / Anual **¥69.99** — Alipay compra una sola vez el periodo correspondiente, **sin renovación automática**
3. Cuando el usuario elija:
   ```
   node scripts/powpow-register.mjs create-order --package monthly
   ```
   El script devuelve la ruta del archivo de la página de pago; **ábrela directamente con un comando del sistema** (Windows: `start <archivo>`; macOS: `open <archivo>`; Linux: `xdg-open <archivo>`). El navegador saltará automáticamente a la caja oficial de Alipay; el usuario escanea el código QR o inicia sesión en Alipay para pagar.
4. Ejecuta `query` cada 10–15 segundos hasta que devuelva `paid` (el cobro suele tardar de unos segundos a un minuto). Si el usuario cierra la página de pago a medias → vuelve a ejecutar `create-order` directamente (el pedido viejo se cierra solo a las 2 horas, no hay que ocuparse de él).
5. Usuarios en el extranjero o sin Alipay: guíalos hacia el canal PayPal de la página de suscripción (la habilidad no lo gestiona, solo indica el camino); el canal de código QR de WeChat es de confirmación manual y el cobro tarda en reflejarse. Cuando hayan pagado, siguen igualmente por el paso 7.

## Paso 7: inicio de sesión formal (enlace 2)

Confirmado el cobro, cambia primero por un estado de sesión con la declaración de suscripción más reciente y genera después el enlace directo al inicio:

```
POWPOW_REGISTER_PASSWORD=<contraseña> node scripts/powpow-register.mjs refresh-login
node scripts/powpow-register.mjs login-link --target home
```

Envía el enlace al usuario: **al abrirlo cae directamente en el inicio, con el estado de membresía completo**; con esto el flujo de registro queda terminado.

## Paso 8: cierre

1. `node scripts/powpow-register.mjs cleanup` limpia el archivo de estado temporal local (las credenciales de la sesión).
2. Entrega al usuario una «tarjeta de cuenta»: nombre de usuario, correo y fecha de caducidad de la membresía (la contraseña no se vuelve a mostrar — en modo generación ya se le pidió guardarla cuando se generó; la que puso él mismo ya la conoce).
3. Guía la primera experiencia: pasear por el mapa, publicar el primer diario de viaje (→ pásalo a powpow-simple).
4. Recomienda extensiones: la habilidad `@durenzidu/powpow-integration` y el plugin `@durenzidu/openclaw-channel-powpow` — conectan Burbuja con el agent del propio usuario; si le interesan, dale los comandos de instalación.
5. Cierra con un bloque de «siguiente paso».

## Conversation UX

Mantén el tono de servicio habitual de powpow:

- **El usuario es el sujeto de la frase**; «puedes…» es mejor que «necesito que…»; nada de sermones ni tono condescendiente.
- **Cada turno avanza una sola decisión**; antes de pedir un dato, da la razón.
- **Al final de cada respuesta** va un bloque fijo de «siguiente paso» (separador + 👉 + una única acción + una frase de «cuando lo hagas, yo…»), por ejemplo:
  ```
  ────────────────────
  👉 Ahora te toca: ve al correo, busca el código de 6 dígitos y envíamelo directamente
     (en cuanto lo reciba, creo la cuenta)
  ```
- **No sueltes sermones de seguridad sobre la contraseña**; no expliques mecanismos internos, límites de frecuencia ni diseño de seguridad, salvo que el usuario pregunte.
- Cuando el agent gestione tareas, informa todavía más del progreso: tras cada paso de script, di en una frase qué acaba de pasar («la cuenta ya está creada», «ya te abrí la página de pago»).

## Reglas firmes

- **Seguridad de las credenciales**: la contraseña se pasa al script solo mediante la variable de entorno `POWPOW_REGISTER_PASSWORD`, **nunca** como argumento de la línea de comandos (visible en la lista de procesos) ni escrita en ningún archivo (en modo generación se muestra una vez para que el usuario la guarde y no se vuelve a repetir). El código de verificación solo se usa en la interfaz oficial de registro y se descarta tras usarse.
- **Límite oficial**: todas las peticiones van únicamente a `https://global.powpow.online` (ya integrado en el script); jamás envíes información del usuario a direcciones de terceros.
- **Límite de pago**: el agent solo crea el pedido, abre la caja y consulta el cobro; **jamás** toca la cuenta Alipay del usuario ni sus credenciales de pago, y jamás promete «pagar por él».
- **El muro de pago no es un bug**: que en estado pending se pueda entrar a la página de suscripción / de retorno es una apertura prevista por diseño; que las páginas de contenido estén bloqueadas es el muro de pago funcionando con normalidad; no intentes saltártelo.
- **Libertad de retroceso**: si en cualquier paso el usuario quiere hacerlo por sí mismo, o el entorno no soporta el script, retrocede en cualquier momento al modo de guía pura — da los enlaces, explica las reglas y acompaña en la resolución de errores.
- No inventes reglas de la plataforma: las reglas de campos, los textos de error y los parámetros de límite provienen del código de la plataforma (`references/registration-flow.md` cita las fuentes); si la plataforma se actualiza, manda el comportamiento real.
- Para mostrar imágenes usa solo las capturas incluidas en `assets/screenshots/` (el uso de cada una está en `references/screenshots.md`).
- Cierra cada turno con el bloque de «siguiente paso», para que el usuario sepa siempre qué le toca hacer ahora.
