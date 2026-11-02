## Description:

Operate a Siemens TIA Portal V19/V20 project through the TiaLink gateway to configure hardware and networks, create PLC blocks with SCL, compile, download to S7-PLCSIM, and verify results by reading them back.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tia-forge](https://clawhub.ai/user/tia-forge)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and industrial automation engineers use this skill to guide an AI agent through inspecting and changing TIA Portal V19/V20 projects via TiaLink, then checking changes with compile results and read-back. It is intended for PLC project work where a local TiaLink gateway and Siemens Openness access are available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Changes to PLC projects or downloads could cause unintended equipment behavior, especially in production.

Mitigation: Begin in a scratch project and simulator, keep backups, and require human confirmation before production changes or downloads; compile and read back each change.

Risk: The gateway uses a long-lived bearer token, and plain HTTP can expose it when traffic crosses an untrusted network.

Mitigation: Keep the token in protected client configuration, never in prompts or commits; use SSH or TLS across machines and do not expose the gateway port to the internet.

## Reference(s):

- [TiaLink product information](https://tia.hubwiz.com/tia-link?utm_source=clawhub&utm_medium=skill)
- [TiaLink project repository](https://github.com/tia-forge/tialink)
- [ClawHub release page](https://clawhub.ai/tia-forge/skills/tialink-tia-portal)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown instructions with inline JSON, SCL, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable gateway is included; operation requires a separately installed TiaLink gateway.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
