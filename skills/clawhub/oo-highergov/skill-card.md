## Description:

Enables agents to search and read HigherGov data through an OOMOL-connected HigherGov account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query HigherGov agencies, contracts, NAICS codes, and federal, state, local, grant, and DIBBS opportunities through an OOMOL connector without handling raw API credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute unverified code on the user's machine.

Mitigation: Use a verified package or separately downloaded and checked installer when possible, and run setup as an unprivileged user.

Risk: Login, service connection, and billing steps can affect account access or charges.

Mitigation: Require explicit user approval before initiating authentication, HigherGov connection, or billing-related recovery steps.

Risk: Connector payloads may be malformed or use stale assumptions about supported HigherGov action fields.

Mitigation: Fetch the live action schema with `oo connector schema` before constructing each payload.

## Reference(s):

- [ClawHub HigherGov skill page](https://clawhub.ai/oomol/skills/oo-highergov)
- [HigherGov homepage](https://www.highergov.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns connector responses with data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
