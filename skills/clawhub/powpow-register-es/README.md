# powpow-register

Asistente de registro en PowPow Burbuja (versión OpenClaw): lleva a un usuario nuevo desde «no sé qué es Burbuja» hasta «cuenta activada, sesión iniciada con un clic, a jugar» — presentación del producto (con capturas de la interfaz), registro gestionado por el agent (incluida la subida del avatar), creación del pedido de suscripción en Alipay o PayPal con seguimiento del cobro, inicio de sesión con un clic mediante doble enlace y resolución de errores.

**Desde v2.0.0 el modo es de gestión delegada en el agent, y desde v2.1.0 también se gestiona PayPal**: el script principal `scripts/powpow-register.mjs` no tiene dependencias (Node ≥ 18); el usuario no sale de la conversación en todo el proceso y solo la abandona momentáneamente dos veces: para mirar el código en su correo y para pagar en la caja de Alipay o PayPal. Si no hay Node, o el usuario prefiere hacerlo solo, se retrocede automáticamente al modo de guía pura.

## Instalación

```
openclaw skills install @durenzidu/powpow-register
```

## Funciones

1. **Presentación del producto**: apertura de ~120 caracteres + capturas de la interfaz incluidas en el paquete (`assets/screenshots/`, 6 imágenes: página del mapa, página de detalle de un post, etc.; elige 1–3 según la escena; sin hospedaje externo, disponible sin conexión).
2. **Registro gestionado**: el agent sugiere proactivamente nombre de usuario/apodo, la contraseña tiene dos opciones (la da el usuario o la genera el agent), envío y entrega del código de verificación, subida directa del avatar (≤5 MB, no SVG), gestión automática de los errores habituales (ocupado / caducado / límite de frecuencia).
3. **Inicio de sesión con un clic (doble enlace)**: nada más registrarse se entrega el enlace de «semi-sesión» que lleva directo a la página de suscripción; confirmado el cobro, se cambia por un estado de sesión nuevo y se entrega el enlace de membresía completa que lleva directo al inicio (usa el puente oficial `me?token=` de la plataforma, que planta automáticamente la cookie HttpOnly).
4. **Suscripción y pago**: tanto Alipay (mensual ¥6.99 / trimestral ¥19.99 / anual ¥69.99, compra única sin renovación automática) como PayPal (Premium Monthly, unos $1/mes, con renovación automática y cancelación en cualquier momento) los gestiona el agent con creación del pedido + sondeo del cobro; el código QR de WeChat y el IAP de Huawei solo se indican.
5. **Resolución de errores**: no llega el código de verificación, nombre de usuario o correo ocupados, 403 de cuenta no activada, cuenta bloqueada, etc.; todo proviene del código fuente de la plataforma con las fuentes citadas.

## Estructura de archivos

```
powpow-register/
├── SKILL.md                            # Guía principal (condiciones de activación, flujo de 8 pasos, tono, reglas firmes)
├── README.md
├── .clawhubignore
├── assets/
│   └── screenshots/                    # Capturas del producto incluidas (powpow-01~06.jpg)
├── scripts/
│   └── powpow-register.mjs             # Script principal (cero dependencias, Node≥18, 11 subcomandos)
└── references/
    ├── agent-flow.md                   # Contrato del script, secuencia completa, mecanismo de doble enlace, diseño de seguridad
    ├── registration-flow.md            # Reglas de campos, límites de frecuencia, tabla de errores (con fuentes del código)
    ├── payment-and-activation.md       # Contrato de Alipay vibepay, cadena de activación, resolución por canal
    └── screenshots.md                  # Inventario de capturas del paquete + consulta rápida por escena
```

## Seguridad

- La **contraseña** solo entra al proceso del script mediante variable de entorno; nunca en la línea de comandos, nunca a disco, nunca en el archivo de estado; la contraseña generada por el agent se muestra una sola vez para que el usuario la guarde.
- El **código de verificación** solo se usa en la interfaz oficial de registro y se descarta tras usarse; el archivo de estado (correo/nombre de usuario/token/número de pedido) vive en el directorio temporal del sistema y se borra con `cleanup` al terminar el flujo.
- **Pago**: el agent solo crea el pedido, abre la caja y consulta el cobro; jamás toca la cuenta Alipay/PayPal del usuario ni sus credenciales de pago, jamás paga por él. El pago ocurre siempre entre el usuario y la caja oficial.
- Todas las peticiones van solo al dominio oficial `https://global.powpow.online`; el paquete no contiene ninguna clave.

## Licencia

MIT-0 (licencia unificada de ClawHub).

## Enlaces

- Sitio oficial: https://global.powpow.online
- Registro: https://global.powpow.online/register
- Conocer Burbuja (vídeo): https://www.bilibili.com/video/BV1Wu826UEVz/
