## Description:

Process Street (process.st) helps agents read, create, and update Process Street data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to operate Process Street workflows, workflow runs, tasks, and form fields from an agent session while keeping Process Street access mediated through OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts that execute directly without verification.

Mitigation: Use a verified, pinned, or package-manager installation path for the oo CLI when available, and avoid running remote installer commands unless the OOMOL source is trusted.

Risk: The skill can perform Process Street write actions that change workflow runs, tasks, or form fields.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running any action tagged as write.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-process-street)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Process Street Homepage](https://www.process.st/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions return JSON data and metadata when the agent runs oo CLI commands.]

## Skill Version(s):

1.0.3 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
