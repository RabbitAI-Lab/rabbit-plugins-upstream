## Description:

PlanetScale CLI Skills helps agents provide command references, safety guidance, and workflow support for PlanetScale operations through the pscale CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, database operators, and platform engineers use this skill to operate PlanetScale databases, branches, deploy requests, credentials, billing, metrics, SQL, backups, webhooks, and related workflows with the pscale CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help perform sensitive or destructive PlanetScale operations, including deploys, deletes, billing or payment-method changes, webhook updates, service-token work, and write-capable SQL.

Mitigation: Review proposed pscale commands before execution, require explicit approval for sensitive changes, and verify targets and results with read-only commands where possible.

Risk: PlanetScale tokens, service-token details, billing data, and raw CLI output may expose sensitive operational information.

Mitigation: Keep tokens in a secret manager or environment variables, avoid pasting secrets into chat, and redact or limit CLI output before sharing it.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/vince-winkintel/skills/planetscale-cli-skills)
- [PlanetScale CLI reference](https://planetscale.com/docs/reference/planetscale-cli)
- [PlanetScale CLI GitHub repository](https://github.com/planetscale/cli)
- [Webhook API reference](https://planetscale.com/docs/api/reference/create_webhook)
- [Webhook events reference](https://planetscale.com/docs/api/webhook-events)
- [Artifact skill overview](artifact/SKILL.md)
- [Artifact version history](artifact/VERSION)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, command examples, scripts, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose pscale CLI commands and bundled shell scripts; review commands before execution.]

## Skill Version(s):

1.0.28 (source: server release metadata and artifact/VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
