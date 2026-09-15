## Description:

ClickUp (clickup.com). Use this skill for ANY ClickUp request -- reading, creating, updating, and deleting data. Whenever a task involves ClickUp, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate ClickUp through an OOMOL-connected account, including reading workspace data and creating, updating, organizing, or deleting ClickUp objects after appropriate confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands that execute code locally.

Mitigation: Review the setup path before installing and prefer a verified official release or package manager for the oo CLI.

Risk: Write and destructive ClickUp actions can modify or remove tasks, lists, spaces, comments, and related objects.

Mitigation: Confirm the exact target, payload, and expected effect with the user before allowing write or destructive actions.

## Reference(s):

- [ClickUp homepage](https://clickup.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClickUp Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-clickup)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; action responses are JSON.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
