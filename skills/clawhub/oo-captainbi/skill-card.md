## Description:

CaptainBI helps an agent search and read CaptainBI business, product, store, inventory, refund, and return data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to retrieve CaptainBI reporting and operational data, including business reports, profit reports, inventory, products, stores, refunds, and returns. It is intended for read-oriented CaptainBI workflows through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CaptainBI reports and store data may contain commercially sensitive operational or financial information.

Mitigation: Install and use the skill only when the agent is intended to read CaptainBI business reports through the user's OOMOL-connected account.

Risk: Setup commands or connection recovery steps can affect local tooling, authentication state, billing, or service connections.

Mitigation: Review setup commands before running them and use recovery steps only after a matching command failure.

## Reference(s):

- [CaptainBI ClawHub listing](https://clawhub.ai/oomol/skills/oo-captainbi)
- [CaptainBI homepage](https://www.captainbi.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; connector responses are JSON with data and meta.executionId fields.]

## Skill Version(s):

1.0.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
