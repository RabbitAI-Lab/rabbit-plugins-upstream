## Description:

Validaciones y datos de Argentina para agentes (CUIT/CUIL, CBU/CVU, teléfonos, cotización del dólar). Usar cuando el usuario mencione un CUIT, CUIL, CBU, CVU, un teléfono argentino o pregunte el valor del dólar en Argentina. Servidor MCP remoto + REST; cobra por créditos prepagos con key de prueba gratis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[torlettijoaquin](https://clawhub.ai/user/torlettijoaquin)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to validate Argentine CUIT/CUIL and CBU/CVU identifiers, normalize Argentine phone numbers, and retrieve current Argentine dollar exchange quotes.

### Deployment Geography for Use:

Argentina

## Known Risks and Mitigations:

Risk: Sensitive identifiers such as CUIT/CUIL or CBU/CVU may be sent to the external service without a clear user request.

Mitigation: Require an explicit validation request before sending identifiers, and check the provider's privacy and retention terms.

Risk: An exposed API key or unattended calls can consume prepaid credits.

Mitigation: Protect the API key, review charges before enabling the service, and stop when credits are insufficient instead of retrying in a loop.

## Reference(s):

- [AR Tools service](https://ar-tools-api.vercel.app)
- [AR Tools OpenAPI specification](https://ar-tools-api.vercel.app/openapi.json)
- [AR Tools MCP endpoint](https://ar-tools-api.vercel.app/mcp)
- [AR Tools on ClawHub](https://clawhub.ai/torlettijoaquin/skills/ar-tools)

## Skill Output:

**Output Type(s):** [API Calls, Guidance, Configuration instructions, Shell commands]

**Output Format:** [Markdown instructions, shell command examples, and structured API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API results may include validation details, exchange quotes, credit cost, and remaining balance.]

## Skill Version(s):

0.1.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
