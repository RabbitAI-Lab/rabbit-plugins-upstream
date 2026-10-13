## Description:

Audita afirmaciones sobre repositorios y proyectos ejecutando comprobaciones y contrastando sus resultados con los códigos de salida.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cha0smagick](https://clawhub.ai/user/cha0smagick)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and auditors use this skill to test project claims against executable checks, record verified, unverified, and refuted findings, and report residual risk.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Executing a repository's audit commands can run untrusted code with access to local files, secrets, or the network.

Mitigation: Run audits only on trusted repositories or in a disposable sandbox or container without mounted secrets and with restricted filesystem and network access.

## Reference(s):

- [Auditoria por ejecucion on ClawHub](https://clawhub.ai/cha0smagick/skills/auditoria-por-ejecucion)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Text, JSON]

**Output Format:** [Markdown audit records and plain-text or JSON check results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Records commands, exit codes, claim status, and residual risk.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
