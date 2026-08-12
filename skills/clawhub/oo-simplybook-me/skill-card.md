## Description:

SimplyBook.me helps an agent operate a connected SimplyBook.me account through OOMOL's oo CLI for reading, creating, and updating booking data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they need an agent to inspect SimplyBook.me services, performers, company information, and availability, and to prepare or run schema-checked connector actions through OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill operates a SimplyBook.me account through the OOMOL oo CLI and connector.

Mitigation: Before installing or using it, confirm that the user trusts OOMOL and wants Codex to operate the connected SimplyBook.me account.

Risk: Actions marked write or destructive can change, remove, or overwrite account data.

Mitigation: Fetch the live action schema, review the exact payload and expected effect, and get explicit user confirmation before running state-changing actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-simplybook-me)
- [SimplyBook.me homepage](https://simplybook.me/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include structured data and execution metadata when run with --json.]

## Skill Version(s):

1.0.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
