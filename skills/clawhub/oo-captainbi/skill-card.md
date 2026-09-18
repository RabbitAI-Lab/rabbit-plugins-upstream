## Description:

CaptainBI helps agents query CaptainBI business reports, profit reports, inventory, product, refund, return, and authorized-store data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve CaptainBI business, profit, inventory, product, refund, return, and store data from a connected OOMOL account after inspecting the live connector schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructs users to run a remote installer directly in a shell.

Mitigation: Review or replace the install step with a pinned oo CLI release and checksum or signature verification before deployment.

Risk: CaptainBI account data becomes available through the OOMOL connector once connected.

Mitigation: Connect only accounts whose business data is appropriate for agent-mediated access and review requested reports before sharing outputs.

## Reference(s):

- [CaptainBI Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-captainbi)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [CaptainBI homepage](https://www.captainbi.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
