## Description:

Enables agents to operate Salesmate CRM through the OOMOL oo CLI connector for reading, creating, updating, and deleting Salesmate data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to inspect Salesmate action schemas and run CRM actions for companies, products, users, and modules through an OOMOL-connected Salesmate account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup recommends piping remote installer scripts directly into a shell.

Mitigation: Use a verified official installation method, inspect downloaded scripts before execution, and avoid elevated shells unless they are explicitly required.

Risk: Salesmate write and destructive actions can change or delete CRM records.

Mitigation: Inspect the live action schema first and require explicit user confirmation for the exact payload and target before running write or delete actions.

## Reference(s):

- [Salesmate Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-salesmate)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Salesmate Homepage](https://www.salesmate.io)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Salesmate action responses are JSON returned by the oo connector run command.]

## Skill Version(s):

1.0.2 (source: skill frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
