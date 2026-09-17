## Description:

EchoTik (echotik.live) helps agents search and read EchoTik TikTok Shop market, product, creator, live, video, shop, and review data through the OOMOL `oo` connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to inspect EchoTik schemas and run read-oriented TikTok Shop commerce queries through an OOMOL-connected EchoTik account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded scripts.

Mitigation: Prefer an official signed or checksum-verified oo CLI installer before running setup commands.

Risk: Authenticated connector use can query EchoTik through an OOMOL-connected account.

Mitigation: Authenticate and connect EchoTik only when the user intentionally wants the skill to run EchoTik queries through OOMOL.

## Reference(s):

- [EchoTik Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-echotik)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [EchoTik API Service](https://echotik.live/zh/api-service)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data plus an execution ID under meta.executionId.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
