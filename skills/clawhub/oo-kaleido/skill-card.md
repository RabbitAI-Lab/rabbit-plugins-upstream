## Description:

Kaleido helps agents inspect and read Kaleido consortia, memberships, environments, nodes, and services through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to retrieve Kaleido account, consortium, environment, node, service, and status information from an OOMOL-connected Kaleido account. It also guides agents to inspect live action schemas before constructing connector payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that execute shell or PowerShell scripts directly.

Mitigation: Do not let an agent automatically run curl-to-shell or irm-to-iex setup commands; install the oo CLI through reviewed official instructions or a verified package.

Risk: Future or schema-discovered Kaleido actions could change state if they are tagged as write or destructive.

Mitigation: Require user confirmation for any state-changing action and inspect the live action schema before constructing a payload.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-kaleido)
- [Kaleido Homepage](https://www.kaleido.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and execution metadata.]

## Skill Version(s):

1.0.2 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
