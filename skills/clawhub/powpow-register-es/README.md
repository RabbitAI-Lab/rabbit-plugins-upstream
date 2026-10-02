# powpow-register

El asistente de registro de Bubble de PowPow (edición OpenClaw): lleva a un usuario nuevo de « no sé qué es Bubble » a « cuenta activada y lista para usar » — presentación del producto (con capturas de la interfaz), guía paso a paso del registro, resolución de errores y explicación de la activación de la suscripción.

Skill puramente orientativo, sin scripts ni dependencias; todas las acciones de registro las realiza el usuario en el navegador/App.

## Instalación

```
openclaw skills install @durenzidu/powpow-register
```

## Funciones

1. **Presentación del producto**: introducción de ~120 caracteres + enlaces de capturas alojadas en un repositorio público de GitHub (6 imágenes: página de mapa, página de detalle de post, etc.; envía 1–3 según el escenario).
2. **Guía de registro**: reglas de campos (nombre de usuario/contraseña/código de verificación de correo/teléfono/avatar), inicio de sesión de terceros (Google/Watcha/Huawei), parámetros de limitación de frecuencia — todo tomado del código fuente de la plataforma con sus fuentes.
3. **Resolución de errores**: 13 problemas comunes, incluidos no recibir el código de verificación, nombre de usuario/correo ya en uso, 403 no activado, cuenta bloqueada.
4. **Activación de la suscripción**: tres canales — PayPal (web) / código QR de WeChat (confirmación manual) / IAP de Huawei (HarmonyOS) — con explicaciones y resolución de errores; la cadena de pago existente se reutiliza tal cual, el skill solo muestra el camino.

## Estructura de archivos

```
powpow-register/
├── SKILL.md                            # Guía principal (activadores, flujo, reglas de tono)
├── README.md
├── .clawhubignore
└── references/
    ├── registration-flow.md            # Reglas de campos, limitaciones, tabla de errores (con fuentes)
    ├── payment-and-activation.md       # Activación de suscripción, canales de pago, conclusión de reutilización
    └── screenshots.md                  # Lista de capturas alojadas + consulta rápida por escenario
```

## Seguridad

- No contiene secretos; sin scripts, nunca toca credenciales del usuario.
- **Nunca pidas** la contraseña, el código de verificación o los comprobantes de pago del usuario; el registro y el pago ocurren por completo en las páginas de la plataforma.

## Licencia

MIT-0 (licencia unificada de ClawHub).

## Enlaces

- Sitio oficial: https://global.powpow.online
- Registro: https://global.powpow.online/register
- Conocer Bubble (vídeo): https://www.bilibili.com/video/BV1Wu826UEVz/