## Description:

Statamic (statamic.com). Use this skill for ANY Statamic request: reading, creating, updating, and deleting data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Statamic account site licenses through OOMOL, including listing sites and creating, updating, or deleting site licenses after inspecting the live action schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that could run unverified code if pasted or executed without review.

Mitigation: Use an official package manager or verified release when possible, and review installer commands before execution.

Risk: The skill can create, update, or delete Statamic site licenses.

Mitigation: Inspect the live action schema and get explicit user confirmation for the exact payload and target before write or destructive actions.

Risk: Using the connector routes Statamic account operations through OOMOL as an intermediary.

Mitigation: Install and use the skill only when the user is comfortable with OOMOL mediating Statamic account access.

## Reference(s):

- [Statamic homepage](https://statamic.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-statamic)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands call the OOMOL oo CLI and may return JSON responses from the Statamic connector.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
