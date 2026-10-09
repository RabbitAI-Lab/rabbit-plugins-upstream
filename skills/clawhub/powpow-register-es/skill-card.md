## Description:

Ayuda a crear y activar una cuenta de PowPow (Burbuja) desde la conversación, incluida la verificación por correo, la suscripción con Alipay y el inicio de sesión.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

Los usuarios de PowPow pueden pedir ayuda para registrarse, resolver problemas de verificación y activar su suscripción. El agente guía la conversación y, cuando hay Node.js 18 o superior, realiza el registro y consulta el estado del pago; el usuario consulta su correo y completa el pago personalmente.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: El registro comparte correo, contraseña, código de verificación y, si se proporciona, avatar con PowPow.

Mitigation: Confirma que el usuario quiere crear la cuenta y facilita estos datos solo para el registro en PowPow.

Risk: La sesión se guarda temporalmente durante el registro y la activación.

Mitigation: Ejecuta cleanup al finalizar para eliminar el estado local de la sesión.

Risk: El flujo abre una página de pago de Alipay y consulta el estado del cobro.

Mitigation: Deja que el usuario pague directamente en la página de Alipay; no solicites sus credenciales de pago.

## Reference(s):

- [Ficha de PowPow Registro en ClawHub](https://clawhub.ai/durenzidu/skills/powpow-register-es)
- [PowPow](https://global.powpow.online)
- [Flujo de registro](artifact/references/registration-flow.md)
- [Pago y activación](artifact/references/payment-and-activation.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Mensajes conversacionales con enlaces de inicio de sesión y resumen de cuenta]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Incluye orientación para completar el pago o continuar manualmente si no hay Node.js.]

## Skill Version(s):

2.0.1 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
