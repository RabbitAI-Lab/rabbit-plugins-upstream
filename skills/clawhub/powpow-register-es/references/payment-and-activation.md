# Activación de suscripción y pago — powpow-register

## Conclusión (la respuesta primero)

**Los métodos de pago existentes son directamente reutilizables — el skill de asistente de registro no requiere ningún desarrollo de pagos.**

Motivos:

1. La interfaz de registro (`src/app/api/auth/register/route.ts`) ya emite una cookie JWT + una cookie HttpOnly pendingUserToken al crear la cuenta pending, de modo que cuando el usuario llega a `/subscription` ya tiene la sesión iniciada — los tres canales de pago cuelgan de esta página de suscripción y todos activan la misma cuenta pending.
2. La interfaz de inicio de sesión devuelve 403 + `redirectTo: '/subscription'` para cuentas pending y crea las cookies igualmente — un usuario que pague más tarde siempre será llevado de vuelta a la misma página.
3. Por tanto, el límite de responsabilidad de un skill de guía de registro es simplemente « llevar al usuario a /subscription »; no hace falta nueva interfaz de pago, ni nuevo modelo de pedido, ni cambios de backend.

También hay que tener en cuenta: el paso de pago (botón del SDK JS de PayPal, confirmación manual del QR de WeChat, IAP nativo de Huawei) **hace que sea imposible e inapropiado que un skill de línea de comandos/chat pague por el usuario**. No intentes llamar a interfaces de pago desde un script para pagar en su lugar, ni pidas los comprobantes de pago del usuario.

## Los tres canales de la página de suscripción

La página de suscripción `src/app/(public)/subscription/page.tsx` muestra automáticamente el canal adecuado según el entorno de ejecución:

| Canal | Entorno | Mecanismo | Activación |
|---|---|---|---|
| Suscripción PayPal | Web (no HarmonyOS) | `/api/subscription/create` crea una suscripción de PayPal → redirige a la autorización de PayPal; renovación automática mensual, cancelable en cualquier momento (`/api/subscription/manage`) | El Webhook de PayPal (`BILLING.SUBSCRIPTION.*`) pone `accountStatus` en active automáticamente |
| Suscripción por código QR de WeChat | Web (no HarmonyOS) | Sección « Suscríbete escaneando WeChat » al final de la página: transferencia escaneando el código, **activación tras confirmación manual** (`WechatQrPaymentSection`) | Confirmación manual; el ingreso puede tardar — no concluyas rápido que falló justo después del pago |
| Compra integrada Huawei (IAP) | Dentro de la App HarmonyOS | En la WebView de HarmonyOS PayPal/WeChat Pay no están disponibles; la página usa el nativo `NativeBridge.purchaseSubscription()` | `/api/subscription/activate-huawei` verifica el pedido de Huawei y activa |

Los planes y precios se leen dinámicamente de `/api/subscription/plans` (planes de PayPal); el texto fijo de la página: Auto-renews. Cancel anytime.

## Estados y redirecciones

- Pago correcto → `/subscription/success` (el callback de PayPal lleva `subscriptionId`) → cuenta active → vuelta automática a la página original indicada por el parámetro `next` (inicio si no hay).
- Un usuario ya suscrito que visite la página de suscripción → muestra "You're All Set!", vuelve al inicio a los 3 segundos.
- Fracaso/cancelación del pago → `/subscription/cancel`, se puede reintentar.

## Resolución de problemas

| Mensaje | Tratamiento |
|---|---|
| Sigue en 403 tras pagar | PayPal: el Webhook a veces va con retraso — cierra y abre sesión para refrescar el estado (el inicio de sesión revisa el último estado en la BD); WeChat: la confirmación manual no ha terminado, espera un poco; Huawei: comprueba si apareció la página de éxito del pago integrado |
| La página de suscripción muestra "No subscription plans available" | No hay planes de PayPal utilizables en `/api/subscription/plans` — un problema de configuración del lado de la plataforma; pide al usuario que lo intente más tarde |
| Pagado por WeChat pero sin activar | La confirmación manual es asíncrona; si en unas horas no se ha activado, contacta con el soporte de la plataforma (dongtao@outlook.com) |

## Nota: Alipay

En el código existe un conjunto de pagos web de Alipay (`src/lib/alipay.ts`, `/api/payment/create-order`, un modelo de compra única: membresía normal ¥9,90 / membresía premium ¥99; degrada automáticamente a pago simulado si la clave del sandbox no está configurada), **pero no está conectado a la UI de la página de suscripción** — es código inactivo/en reserva. Si en el futuro hay que habilitar Alipay en la página de suscripción, basta con conectar este código ya hecho — no tiene relación con este skill y se anota solo como referencia para decisiones del lado de la plataforma.