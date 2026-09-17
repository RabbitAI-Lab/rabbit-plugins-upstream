## Description:

Use Asana through the OOMOL-connected oo CLI to read, search, create, update, and delete Asana work items and related resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Asana workspaces from an agent through OOMOL-connected actions, including task, project, team, tag, attachment, story, and custom field workflows. It is suited to agent-assisted project management automation where state-changing actions are confirmed before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup instructions include direct execution of remote installer scripts without verification.

Mitigation: Review setup before installation, prefer an official package manager or pinned installer, and verify checksums or signatures when available.

Risk: The skill can create, update, delete, or remove Asana resources.

Mitigation: Confirm the exact target, payload, and expected effect before any write or destructive action is executed.

## Reference(s):

- [Asana homepage](https://asana.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON-oriented action payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include Asana action results returned through the oo CLI and guidance for confirming write or destructive operations.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
