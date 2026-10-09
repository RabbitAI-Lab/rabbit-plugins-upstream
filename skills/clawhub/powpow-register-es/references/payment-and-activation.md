# Activación de la suscripción y pago — powpow-register

## Conclusión (primero la respuesta)

**El canal de Alipay ya está en línea (desde el 2026-10-07), es la vía de pago principal de esta habilidad, y el agent puede gestionar por delegación la creación del pedido y el seguimiento del cobro.**
Los usuarios del extranjero o sin Alipay retroceden a PayPal; el código QR de WeChat (confirmación manual) y Huawei IAP siguen existiendo, pero la habilidad no los gestiona por delegación.

Límites de responsabilidad en el pago: el agent puede **crear el pedido, abrir la caja y consultar el cobro**; **jamás** toca la cuenta Alipay
del usuario ni sus credenciales de pago, y jamás promete «pagar por él». La acción de pagar la realiza siempre el propio usuario en la caja oficial de Alipay.

## Canal de Alipay (vibepay, vía principal)

Compra única sin renovación: se paga una vez y se activa el periodo correspondiente, **sin renovación automática**. Los planes están fijados en
`src/lib/alipay-vibepay.ts` (`ALIPAY_PACKAGES`):

| key | planId | Nombre | Precio | Duración |
|---|---|---|---|---|
| `monthly` | alipay-monthly | Membresía mensual | ¥6.99 | 30 días |
| `quarterly` | alipay-quarterly | Membresía trimestral | ¥19.99 | 90 días |
| `yearly` | alipay-yearly | Membresía anual | ¥69.99 | 365 días |

### Contrato de las interfaces (el script de la habilidad ya las encapsula, el agent no monta las peticiones a mano)

| Interfaz | Método | Descripción |
|---|---|---|
| `/api/payment/alipay/create-order` | POST | Requiere `Authorization: Bearer <JWT>` (basta un usuario pending). body `{package}` → devuelve `{paymentHtml, outTradeNo, amount, planName}`; `paymentHtml` es una página de formulario que se autoenvía a la pasarela de Alipay |
| `/api/payment/alipay/query` | GET `?outTradeNo=` | Igualmente autenticación Bearer. Devuelve `paid` / `pending` / `closed` / `unknown` |
| `/api/payment/alipay/notify` | POST (callback del servidor de Alipay) | Verificación de firma en cinco puntos (firma, app_id, coincidencia de importe, TRADE_SUCCESS/TRADE_FINISHED, unicidad del comerciante) → actualización **idempotente** del pedido + creación de la suscripción + activación de la cuenta. La habilidad jamás toca esta interfaz |
| `/payment/alipay/return` | Página de retorno del navegador | Ruta pública; tras el pago muestra la confirmación de 「支付成功」 (pago completado) y sondea dentro de la página el estado real del backend |

- Los pedidos no pagados se **cierran automáticamente a las 2 horas**; si el usuario lo abandona a medias → vuelve a ejecutar `create-order` directamente, sin ocuparte del pedido viejo.
- El script escribe el `paymentHtml` en un archivo HTML temporal; el agent lo abre con un comando del sistema y ya se entra en la caja de Alipay
  (escaneando el código QR o iniciando sesión en Alipay para pagar).

### Cadena de activación (automática, sin intervención manual)

Verificación de firma del notify superada → `paymentOrders` marcado como pagado → `user_subscriptions` crea/prorroga
(`planId`, `currentPeriodEnd` calculados según durationDays; las renovaciones se prorrogan sobre la fecha de vencimiento original) →
`users.accountStatus: active` + `subscriptionStatus: ACTIVE` → la página de retorno sondea el paid y muestra el éxito.

## Tras el pago hay que renovar obligatoriamente el estado de sesión (importante)

El JWT lleva dentro la declaración de suscripción (en una cuenta pending es `NONE`). **El cobro del pago solo actualiza la base de datos, no modifica un
JWT ya emitido** — la declaración del token viejo sigue siendo NONE; si se usa directamente para generar el enlace de inicio de sesión, se manifestará como «sin membresía».
Por eso la habilidad, tras confirmar el `paid`, ejecuta primero `refresh-login` (reinicia sesión y cambia por un JWT nuevo, con la declaración ACTIVE)
y después genera el enlace 2. Es comportamiento de diseño, no una corrección de bug.

## Los cuatro canales de la página de suscripción

La página de suscripción `src/app/(public)/subscription/page.tsx` muestra según el entorno de ejecución:

| Canal | Entorno | Mecanismo | Forma de activación |
|---|---|---|---|
| **Alipay (principal)** | Web | `AlipayPaymentSection` va por las interfaces de vibepay (tabla de arriba) | Activación automática del servidor vía notify, en segundos |
| Suscripción PayPal | Web (no HarmonyOS) | `/api/subscription/create` → salto a la autorización de PayPal; renovación mensual automática cancelable en cualquier momento (`/api/subscription/manage`) | El Webhook de PayPal (`BILLING.SUBSCRIPTION.*`) pone active automáticamente |
| Suscripción por código QR de WeChat | Web (no HarmonyOS) | Al pie de la página 「微信扫码订阅」 (escanea el código para suscribirte): transferencia por código QR | **Confirmación manual**, el cobro puede tardar en reflejarse; no concluyas con prisa que ha fallado justo después de pagar |
| Compra in-app de Huawei | Dentro de la app HarmonyOS | `NativeBridge.purchaseSubscription()` nativo | `/api/subscription/activate-huawei` valida el pedido de Huawei y activa |

Los planes y precios de PayPal se leen dinámicamente de `/api/subscription/plans`; texto fijo de la página: Auto-renews. Cancel anytime.

## Estados y saltos

- Alipay terminado → la página de retorno muestra el éxito; PayPal con éxito → `/subscription/success` → cuenta active →
  salto automático de vuelta a la página original indicada por el parámetro `next` (si no hay, al inicio).
- Un usuario ya suscrito que vuelva a la página de suscripción → ve "You're All Set!", y a los 3 segundos regresa automáticamente al inicio.
- Pago fallido / cancelado (PayPal) → `/subscription/cancel`, se puede volver a iniciar.

## Diagnóstico

| Síntoma | Gestión |
|---|---|
| Alipay terminado pero `query` sigue en pending | El notify rara vez se retrasa; espera 30 segundos y consulta de nuevo. Si sigue sin funcionar, que el usuario mire en el navegador el estado de la página de retorno; si aun así no, contacta con el soporte de la plataforma (dongtao@outlook.com) comunicando el `outTradeNo` |
| Alipay terminado, pero al entrar con el enlace 2 sigue bloqueado | Se saltó el `refresh-login` (la declaración del JWT viejo no se actualizó) — primero `refresh-login` y luego `login-link` |
| Tras pagar sigue 403 (PayPal) | El Webhook a veces se retrasa; reinicia sesión para refrescar el estado |
| Pagado por WeChat pero sin activación | La confirmación manual es asíncrona; si en unas horas no se activa, contacta con el soporte de la plataforma |
| La página de suscripción muestra "No subscription plans available" | `/api/subscription/plans` no tiene planes PayPal disponibles, problema de configuración del lado de la plataforma; los usuarios de China continental pueden irse por Alipay |

## Nota histórica

En el código existe además **una vieja** pasarela de pago web de Alipay (`src/lib/alipay.ts`, `/api/payment/create-order`,
¥9.90/¥99 compra única, degradada a pago simulado cuando el sandbox no tiene claves configuradas), que nunca se conectó a la UI de la página de suscripción y no tiene
relación con vibepay. La habilidad no la toca en ningún caso; `alipay-vibepay.ts` es el canal vigente.
