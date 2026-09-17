## Description:

ClickUp enables agents to read, create, update, and delete ClickUp data through OOMOL-connected oo CLI actions instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to inspect ClickUp action schemas and run OOMOL-connected ClickUp actions for workspace, task, list, view, comment, checklist, dependency, tag, attachment, and custom-field workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote shell installer commands that could execute unverified installer code.

Mitigation: Review and install the oo CLI through an official, versioned, verifiable installer or package-manager method; do not let an agent run curl|bash or irm|iex automatically, especially from an elevated shell.

Risk: Write and destructive ClickUp actions can change or remove workspace data.

Mitigation: Confirm the exact action, target identifiers, payload, and expected effect before executing any write or destructive command.

## Reference(s):

- [ClickUp homepage](https://clickup.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClickUp skill on ClawHub](https://clawhub.ai/oomol/skills/oo-clickup)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes confirmation guidance for state-changing and destructive ClickUp actions.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
