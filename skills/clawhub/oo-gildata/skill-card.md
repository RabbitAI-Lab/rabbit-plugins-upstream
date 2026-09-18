## Description:

Gildata Data Map helps agents query Gildata financial data through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to answer financial data questions, screen securities and funds, compare stocks, retrieve macro data, and search company news or research reports through a connected Gildata account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup instructions include internet installer commands that can execute local code.

Mitigation: Use a verified package-manager or signed installer path for the oo CLI when possible, and inspect installer sources before running them.

Risk: The skill can run account-linked Gildata actions through the oo CLI.

Mitigation: Inspect the live action schema and payload before execution, and require user confirmation before any write or destructive action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-gildata)
- [Gildata Data Map homepage](https://www.gildata.com/products/datamap)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload or response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute oo CLI commands that return JSON data from Gildata actions.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
