# Flujo de gestión delegada del agent y contrato del script — powpow-register

Detalles de ejecución de cada paso de SKILL.md. Todos los comandos tienen la forma `node scripts/powpow-register.mjs <subcomando> [parámetros]`;
el script es de **cero dependencias** y requiere **Node ≥ 18**; todas las peticiones van únicamente a `https://global.powpow.online`.

## Diseño de seguridad (por qué está diseñado así)

| Diseño | Razón |
|---|---|
| La contraseña solo entra por la variable de entorno `POWPOW_REGISTER_PASSWORD` | Los argumentos de la línea de comandos de un proceso son visibles para otros procesos de la misma máquina (superficie de fuga de argv); la variable de entorno se lee dentro del script y se usa al momento |
| La contraseña **jamás se escribe en el archivo de estado**, jamás aparece en los logs | El archivo de estado puede quedar en el disco; en modo generación se muestra solo una vez para que el usuario la guarde |
| El archivo de estado vive en el directorio temporal del sistema (`os.tmpdir()/powpow-register-state.json`, 0600) | Contiene únicamente los cinco campos email / username / nickname / token / outTradeNo; `cleanup` lo borra de un golpe |
| El JWT que recibe el agent se cambia por una cookie de navegador vía el endpoint oficial `me?token=` | Es el puente oficial diseñado por la plataforma para el WebView de HarmonyOS; la verificación de firma solo comprueba firma + validez, no ata a la huella del dispositivo, así que el navegador del usuario sirve |
| El pago solo hace create-order / query / abrir la caja | La acción de pagar y las credenciales de pago quedan siempre entre el usuario y la caja oficial de Alipay; el agent no toca nada de eso |

## Referencia de comandos

| Comando | Parámetros clave | Qué hace / cuándo |
|---|---|---|
| `status` | —— | Ver el progreso del flujo (lee el archivo de estado); tras una interrupción de la conversación, ejecuta primero esto |
| `gen-password` | —— | Genera una contraseña fuerte de 24 caracteres (mayúsculas + minúsculas + números); stdout la muestra **solo esta vez** |
| `prepare-suggest` | `--username --nickname --email` | Anota en el archivo de estado la información confirmada (así register no vuelve a pedirla) |
| `send-code` | `--email` | Dispara el envío por la plataforma del código de verificación de 6 dígitos (válido 10 minutos, enfriamiento de 60s) |
| `register` | `--code` (obligatorio); `--username --nickname --avatar --phone` (opcionales, se omiten si ya están en el archivo de estado) | Crea la cuenta pending; la contraseña va por la variable de entorno `POWPOW_REGISTER_PASSWORD`; tras el éxito el JWT se guarda automáticamente en el archivo de estado |
| `login-link` | `--target pending` o `--target home` | Genera un enlace de inicio de sesión con un clic (diseño de doble enlace, ver abajo) |
| `create-order` | `--package monthly\|quarterly\|yearly` (Alipay por defecto)<br>`--provider alipay\|paypal` | Crea el pedido de pago; Alipay devuelve la ruta del archivo de la página de pago + outTradeNo; PayPal devuelve la ruta del archivo de la página de autorización + subscriptionId (anotado automáticamente en el archivo de estado) |
| `query` | —— | Consulta el estado del pedido/suscripción. Alipay: `paid / pending / closed / unknown`; PayPal: `ACTIVE / PENDING`; sondeo cada 10–15s |
| `refresh-login` | La contraseña por variable de entorno | Vuelve a iniciar sesión y obtiene un **JWT nuevo** (la declaración de suscripción pasa de NONE a ACTIVE); obligatorio tras confirmar el cobro |
| `whoami` | —— | Consulta con el token del archivo de estado el estado de la cuenta y de la suscripción (para verificar si la activación surtió efecto) |
| `cleanup` | —— | Borra el archivo de estado (obligatorio al cerrar) |

**Paso de la variable de entorno** (la contraseña jamás va en la línea de comandos):

```bash
# bash / zsh / WSL
POWPOW_REGISTER_PASSWORD='<contraseña>' node scripts/powpow-register.mjs register --code 123456
# PowerShell
$env:POWPOW_REGISTER_PASSWORD = '<contraseña>'; node scripts/powpow-register.mjs register --code 123456
# cmd
set POWPOW_REGISTER_PASSWORD=<contraseña> && node scripts/powpow-register.mjs register --code 123456
```

## Mecanismo del doble enlace (diseño central)

El estado de sesión de la plataforma es una cookie HttpOnly, así que el agent no puede plantarle directamente una cookie al navegador; el puente es el endpoint oficial
`/api/auth/me?token=<JWT>&redirect=<ruta interna del sitio>`: verificación de firma → al usuario pending se le crea automáticamente
session → `Set-Cookie: powpow_token` (HttpOnly / SameSite=Lax / 7 días) → validación del
redirect (solo rutas que empiezan con una sola barra, prohibidos `//` y la barra invertida, y tras resolver debe ser del mismo origen) → 307 redirección temporal a la página de destino.

- **Enlace 1 (entregarlo inmediatamente tras el registro con éxito)**: `--target pending` → aterriza en `/subscription`.
  El navegador del usuario entra en estado de «semi-sesión»: la página de suscripción y la de retorno de Alipay son visibles y operables; las páginas de contenido siguen siendo rechazadas por el muro de pago
  y devueltas a la de suscripción (triple protección: comprobación en el gateway de los claims del JWT → re-comprobación en la BD → comprobación en las API centrales; es comportamiento normal).
- **Enlace 2 (entregarlo tras confirmar paid)**: primero `refresh-login` para cambiar por un JWT nuevo (el pago solo actualiza la BD, no modifica los
  claims de un JWT ya emitido; si no se cambia, se manifestará como «pagué pero no tengo membresía»), luego `--target home` → aterriza en el inicio,
  con el estado de membresía completo.

## Secuencia completa (ruta normal)

```
1.  status                          # autochequeo del entorno
2.  (el paso 2 es confirmar datos en la conversación, contraseña con dos opciones; modo generación: gen-password → que el usuario la guarde al instante)
3.  prepare-suggest --username U --nickname N --email E
4.  send-code --email E             # → el usuario va al correo a mirar el código (única salida de la conversación, momento ①)
5.  POWPOW_REGISTER_PASSWORD=*** register --code 123456 [--avatar pic.jpg]
6.  login-link --target pending     # → enlace 1 enviado al usuario
7.  (el usuario elige método de pago)
    # Alipay: create-order --package monthly|quarterly|yearly
    # PayPal: create-order --provider paypal
8.  start <archivo de la página de pago>   # Windows; en macOS usar open, en Linux xdg-open
     # → el usuario completa el pago/autorización en la caja de Alipay/PayPal (salida de la conversación, momento ②)
9.  query (cada 10–15s) hasta paid / ACTIVE
10. refresh-login                   # cambio por el JWT nuevo con declaración ACTIVE
11. login-link --target home        # → enlace 2 enviado al usuario
12. whoami                          # confirmar subscriptionStatus: ACTIVE (opcional)
13. cleanup                         # limpiar el archivo de estado
```

## Mapeo comando → API de la plataforma

| Comando del script | Endpoint de la plataforma |
|---|---|
| `send-code` | `POST /api/auth/register/send-code` |
| `register` | `POST /api/auth/register` (multipart, subida directa del avatar) |
| `login-link` | `GET /api/auth/me?token=…&redirect=…` (el enlace en sí, surte efecto al pulsarlo en el navegador) |
| `create-order` | `POST /api/payment/alipay/create-order` (Bearer, Alipay)<br>`GET /api/subscription/plans` + `POST /api/subscription/create` (Bearer, PayPal) |
| `query` | `GET /api/payment/alipay/query?outTradeNo=…` (Bearer, Alipay)<br>`GET /api/subscription/create` (Bearer, PayPal) |
| `refresh-login` | `POST /api/auth/login` (`{step:1, username, password}`) |
| `whoami` | `GET /api/auth/me?token=…` |

Fuente de las reglas: campos de registro y límites de frecuencia en `registration-flow.md`; planes y cadena de activación en
`payment-and-activation.md` (ambos citan los archivos del código fuente de la plataforma).

## Gestión de errores a nivel de script

| Síntoma | Gestión |
|---|---|
| `Versión de Node demasiado baja` | Retrocede al modo de guía pura, no insistas a lo bruto |
| Error de red / timeout | Reintenta una vez; si sigue fallando, que el usuario revise la red y continúa (el archivo de estado sigue ahí; recupera desde el principio ejecutando `status`) |
| register devuelve un error de negocio (nombre de usuario ya existe, etc.) | Trátalo según la tabla del paso 5 de SKILL.md, **no hace falta reenviar el código de verificación** (sigue siendo válido durante 10 minutos) |
| register devuelve 「邮箱验证码错误或已过期」 (código de verificación incorrecto o caducado) | Si pasó el tiempo → volver a `send-code` |
| El usuario cerró la página de pago tras `create-order` | Vuelve a ejecutar `create-order` directamente (el pedido viejo se cierra solo a las 2h; las suscripciones PENDING de PayPal expiran a la 1h) |
| `create-order --provider paypal` devuelve 409 | Ya hay una suscripción de PayPal sin terminar; espera 1h a que expire o completa la autorización antigua en el navegador |
| `query` sigue en pending / PENDING | Puede que el usuario no haya pagado; pregunta. Si de verdad pagó → sigue la tabla de diagnóstico de payment-and-activation.md |
| `refresh-login` da 403 `pending_payment` | El cobro o la autorización aún no ha llegado; vuelve al paso 9 y sigue sondeando |
| Archivo de estado perdido (borrado por error / cambio de máquina) | `whoami`/`refresh-login` dejan de servir; que el usuario actualice directamente la página de suscripción en el navegador donde abrió el enlace 1 para confirmar el estado, o inicie sesión de nuevo (modo web) |

## Modo de retroceso (guía pura)

Ante cualquiera de estas situaciones, retrocede de inmediato a la guía pura estilo v1 y deja de pelear con el script:

- No hay Node ≥ 18, o el script falla dos veces seguidas en lo mismo;
- El usuario dice claramente «lo hago yo mismo en la página web»;
- Las políticas de la empresa o del dispositivo restringen los scripts de red.

Tras la retroceso: entrega la página de registro https://global.powpow.online/register y la de suscripción
https://global.powpow.online/subscription, acompaña en la resolución de errores según las reglas de `registration-flow.md`,
mantén el mismo tono, y cierra cada ronda igualmente con el bloque de «siguiente paso».
