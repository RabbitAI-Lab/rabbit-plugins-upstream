# Flujo de registro en detalle — powpow-register

Referencia para resolver problemas. Todas las reglas provienen del código fuente de la plataforma (validación coherente de Next.js en frontend y backend), con las fuentes citadas.
Cuando la plataforma se actualice, manda el comportamiento real en línea.

## Entradas

- Página de registro: https://global.powpow.online/register
- Página de inicio de sesión: https://global.powpow.online/login
- Página de suscripción: https://global.powpow.online/subscription
- Si se llega desde un enlace compartido con `?next=...`, tras el registro + pago se vuelve automáticamente a la página original.

## Campos del formulario y reglas

| Campo | Obligatorio | Regla | Fuente |
|---|---|---|---|
| Avatar | Opcional | Imagen ≤5MB, no se admite SVG; el servidor comprime automáticamente (>100 KB se comprime a 400×400 / calidad 90) | `src/app/api/auth/register/route.ts` |
| Nombre de usuario | Obligatorio | 2–50 caracteres, se guarda en **minúsculas** tras el trim (Tom y tom se tratan como el mismo nombre de usuario; registro e inicio de sesión no distinguen mayúsculas) | ídem (esquema zod) |
| Contraseña | Obligatorio | 8–100 caracteres, debe contener mayúsculas, minúsculas y números | ídem |
| Confirmar contraseña | Obligatorio | Debe coincidir con la contraseña (solo validación en frontend) | `src/app/(public)/register/page.tsx` |
| Apodo | Opcional | ≤100 caracteres; si se deja vacío, se usa el nombre de usuario | register route |
| Correo | **Obligatorio** | Formato de correo válido, ≤255 caracteres; un correo solo puede registrar una cuenta | register route |
| Código de verificación de correo | **Obligatorio** | 6 dígitos; **válido 10 minutos**; se invalida tras verificar; reenviar marca el código anterior como usado | `src/lib/email-verification.ts` |
| Teléfono | Opcional | Número de China continental que empieza por `1[3-9]`, 11 dígitos en total; un teléfono solo puede vincularse a una cuenta | register route |

La página ofrece además tres botones de inicio de sesión de terceros: **Google, Watcha, cuenta Huawei** (`GoogleSignInButton` / `WatchaLoginButton` / `HuaweiLoginButton`). Las cuentas de terceros no tienen contraseña local; intentar iniciar sesión con contraseña más tarde devuelve « 该账号未设置密码，请使用其他方式登录 » (Esta cuenta no tiene contraseña establecida, usa otro método de inicio de sesión).

## Límites de frecuencia y parámetros anti-fuerza bruta

| Comportamiento | Límite | Fuente |
|---|---|---|
| Envío de registro | **3 veces/min/IP**, 429 al superarlo | `src/lib/rate-limit.ts` `REGISTER_RATE_LIMIT` |
| Enviar código de verificación | Misma IP 1 vez/min **y** mismo correo 1 vez/min, 429 al superarlo; cuenta atrás de 60 segundos en el botón del frontend | `src/app/api/auth/register/send-code/route.ts` |
| Verificación del código | Máximo **5 intentos** por correo en 10 minutos; al alcanzar el límite se rechaza incluso con el código correcto, se necesita uno nuevo | `src/lib/email-verification.ts` |
| Código de contraseña olvidada | 1 vez/min/IP | `src/app/api/auth/forgot-password/route.ts` |
| Inicio de sesión | 5 veces/min/IP; **5 fallos seguidos bloquean la cuenta 30 minutos** (423), con aviso decreciente de intentos restantes | `src/app/api/auth/login/route.ts`, `rate-limit.ts` |

**Comportamiento de protección de privacidad**: al enviar el código de verificación / de contraseña olvidada, la interfaz devuelve el mismo mensaje de éxito tanto si el correo está registrado como si no, sin revelar si existe.

## Transición de estados tras un registro exitoso

1. El usuario se guarda con `accountStatus: 'pending'` y **3 insignias iniciales** (register route).
2. El servidor crea a la vez dos cookies HttpOnly: JWT (permite acceder directamente a `/subscription`) y pendingUserToken (credencial de identidad para el flujo de suscripción).
3. La página de registro detecta `pending_payment` → salta a `/subscription` (conservando el parámetro de retorno `next`).
4. Pago completado → `accountStatus` pasa a `active` (PayPal activa automáticamente por Webhook; código QR de WeChat por confirmación manual; IAP de Huawei vía `activate-huawei`). Ver `payment-and-activation.md`.

Las llamadas de un usuario no activado (pending) a las API principales (feed, mapa, chat con humanos digitales, check-ins, etc.) devuelven siempre 403; los enlaces de posts compartidos son la excepción (siguen siendo públicos).

## Tabla de errores comunes

| Mensaje | Causa | Qué hacer |
|---|---|---|
| 「用户名已存在」(El nombre de usuario ya existe) | El nombre de usuario está ocupado (sin distinguir mayúsculas) | Elige otro nombre de usuario |
| 「邮箱已被使用」(El correo ya está en uso) | El correo ya está registrado | Usa otro correo; o entra por inicio de sesión + « Contraseña olvidada » para recuperar la cuenta anterior |
| 「邮箱验证码错误或已过期」(El código de verificación de correo es incorrecto o ha caducado) | Código mal escrito / más de 10 minutos / rechazado tras más de 5 intentos | Pulsa « Reenviar » y usa el código del **último** correo |
| No llega el código de verificación | Límite de 60 segundos; o cayó en spam/promociones | Espera a que termine la cuenta atrás para reenviar; revisa la carpeta de spam |
| 「手机号已被使用」(El teléfono ya está en uso) | El teléfono está vinculado a otra cuenta | Elimina el teléfono (campo opcional) o usa otro |
| 「注册请求过于频繁」/ 429 (Demasiadas solicitudes de registro) | Se alcanzó el límite de 3 registros/min/IP | Espera unos minutos y reintenta |
| 409「用户名或邮箱已被注册」(Nombre de usuario o correo ya registrados) | Colisión con otro usuario al enviar (respaldo por concurrencia) | Cambia el nombre de usuario o el correo y reintenta |
| 「图片大小不能超过5MB」/「不支持 SVG」(El tamaño de la imagen no puede superar 5MB / SVG no admitido) | El avatar no cumple las normas | Cambia de imagen u omite el avatar |
| Registro exitoso pero inicio de sesión 403「请完成订阅以激活账户」(Completa tu suscripción para activar la cuenta) | La cuenta sigue pending | Tras iniciar sesión, sigue el aviso de la página y ve a `/subscription` para completar la suscripción |
| Inicio de sesión 423「账户已锁定」(Cuenta bloqueada) | Contraseña incorrecta 5 veces | Espera 30 minutos |
| Inicio de sesión 401「还剩 N 次尝试机会」(Quedan N intentos) | Contraseña incorrecta, cerca del bloqueo | Piensa bien antes de reintentar, o ve directo a « Contraseña olvidada » |
| 「该账号未设置密码，请使用其他方式登录」(Esta cuenta no tiene contraseña establecida, usa otro método de inicio de sesión) | Cuenta de terceros (Google/Watcha/Huawei) | Inicia sesión con el botón de terceros original |
| 「该账号已注销」(Esta cuenta ha sido desactivada) | La cuenta está desactivada | Hace falta registrarse de nuevo |

## Datos útiles de inicio de sesión (también para resolver problemas)

El inicio de sesión acepta un campo combinado de **nombre de usuario / correo / teléfono** (cualquiera de los tres funciona como nombre de cuenta).
Contraseña olvidada: página de inicio de sesión → « Contraseña olvidada » → introduce el correo de registro, recibe un código de 6 dígitos → restablece.