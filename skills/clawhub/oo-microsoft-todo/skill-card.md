## Description:

Operate Microsoft To Do task lists, tasks, and checklist items through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to read, create, update, and delete Microsoft To Do lists, tasks, and checklist items through the OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or update Microsoft To Do lists, tasks, and checklist items.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

Risk: The skill can delete checklist items, tasks, or entire task lists.

Mitigation: Get explicit approval for the exact deletion target before running destructive actions.

Risk: The skill relies on OOMOL to mediate access to the user's Microsoft To Do account.

Mitigation: Install and use the skill only when the user trusts OOMOL and has intentionally connected the Microsoft To Do account.

## Reference(s):

- [Microsoft To Do](https://to-do.office.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-microsoft-todo)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include connector commands that return JSON data from Microsoft To Do.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
