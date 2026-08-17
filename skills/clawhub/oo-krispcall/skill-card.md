## Description:

KrispCall (krispcall.com). Use this skill for ANY KrispCall request — reading, creating, updating, and deleting data. Whenever a task involves KrispCall, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a connected KrispCall workspace through OOMOL, including reading workspace, member, and contact data and performing confirmed contact create, update, or delete actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, and delete KrispCall contacts in a connected workspace.

Mitigation: Confirm the exact payload, target, and expected effect with the user before running write or destructive actions.

Risk: First-time setup may require installing the oo CLI and connecting an OOMOL account.

Mitigation: Use setup commands only after an authentication or connection failure, and review one-time installer and account connection steps before approving them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-krispcall)
- [KrispCall Homepage](https://krispcall.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return connector JSON responses containing data and meta.executionId when actions are run.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
