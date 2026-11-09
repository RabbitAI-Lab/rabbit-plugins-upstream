## Description:

JPVerify helps agents choose checks for Japanese companies, invoice issuers, suppliers, addresses, and JP PINT e-invoices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[japanverify](https://clawhub.ai/user/japanverify)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use JPVerify to select and run Japanese business registry, invoice, supplier, and address checks, or validate JP PINT e-invoices. It provides routing guidance for choosing a suitable check and interpreting the returned evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review marks this release suspicious with medium confidence. It cites full-invoice upload examples without a privacy checkpoint and capabilities beyond the stated verification purpose.

Mitigation: Send only the fields needed for a check. Before sending sensitive invoice information to the external service, confirm authorization and that its use is appropriate; review uncertain results before acting.

Risk: Scanner coverage is partial, and some local references were unresolved, so the available review does not establish that every referenced item was assessed.

Mitigation: Review unresolved references and the service's data handling before relying on the skill.

## Reference(s):

- [JPVerify release page](https://clawhub.ai/japanverify/skills/jpverify)
- [JPVerify API key guide](https://api.jpverify.com/docs/api-key)
- [JPVerify x402 guide](https://api.jpverify.com/docs/x402)
- [endpoints.md](references/endpoints.md)
- [examples.md](references/examples.md)

## Skill Output:

**Output Type(s):** [Guidance, API requests, JSON]

**Output Format:** [Concise text guidance and structured JSON service results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No files are produced by default.]

## Skill Version(s):

1.2.1 (source: server-resolved release metadata, SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
