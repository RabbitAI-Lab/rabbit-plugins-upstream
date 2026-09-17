## Description:

Data247 enables agents to run Data247 phone intelligence, account balance, and name-based gender inference actions through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use this skill to query Data247 for phone verification, DNC checks, carrier type detection, account balance checks, and probable gender inference without handling raw Data247 API credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands for the oo CLI.

Mitigation: Do not let an agent run the installer automatically; install the CLI from an official, versioned source after reviewing integrity details.

Risk: Data247 requests are routed through OOMOL as an intermediary with server-side credentials.

Mitigation: Use the skill only when the user is comfortable with OOMOL brokering Data247 queries and has deliberately signed in and connected Data247.

Risk: Connector payloads may be malformed or target an unintended Data247 action.

Mitigation: Fetch the live action schema with oo connector schema before constructing payloads, and confirm exact payloads before any write or destructive action if such actions are added later.

## Reference(s):

- [Data247 homepage](https://www.data247.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-data247)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and metadata when actions are run.]

## Skill Version(s):

1.0.3 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
