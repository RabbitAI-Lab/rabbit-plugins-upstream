## Description:

Handelsregister AI (handelsregister.ai) helps an agent search for and read German commercial-register organization data through the OOMOL Handelsregister AI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill when an agent needs to inspect the live connector schema, then search for German organizations or fetch company profiles by name, register number, search query, or entity ID.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include installing the oo CLI through internet-delivered shell commands, which the security evidence marks as suspicious.

Mitigation: Review the setup path before installing, prefer a pinned and verifiable CLI release or package manager, and avoid running installer commands from an elevated shell.

Risk: Connector actions may consume paid Handelsregister AI enrichment or fail when the account has insufficient credit.

Mitigation: Inspect the live schema and requested payload before execution, and resolve billing or credit issues through the connected OOMOL account before retrying.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-handelsregister-ai)
- [Handelsregister AI homepage](https://handelsregister.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text, JSON]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to inspect the live connector schema before sending JSON payloads and to use read-only Handelsregister AI actions unless an action is explicitly tagged otherwise.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
