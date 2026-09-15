## Description:

Asana lets agents read, search, create, update, and delete Asana workspaces, projects, tasks, and related resources through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Asana from an agent session, including reading project data and managing tasks, projects, teams, users, comments, attachments, tags, custom fields, and related workspace resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path recommends executing a remote installer directly in a shell.

Mitigation: Review the installer path before installing and prefer a signed or package-manager source, or download and verify the installer before running it.

Risk: Write and destructive Asana actions can change or remove workspace data.

Mitigation: Confirm the exact target, payload, and intended effect with the user before running write or destructive actions.

Risk: Action inputs may drift from documented examples as connector schemas change.

Mitigation: Inspect the live action schema before constructing each payload.

## Reference(s):

- [Asana homepage](https://asana.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-asana)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; action results are returned as JSON by the oo CLI.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
