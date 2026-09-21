## Description:

Google Slides (workspace.google.com). Use this skill for ANY Google Slides request -- reading, creating, updating, and deleting data. Whenever a task involves Google Slides, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate a connected Google Slides account through OOMOL's oo CLI, including reading presentations, creating slides decks, copying templates, retrieving thumbnails, and applying batch updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate a connected Google Slides account, including actions that create or modify presentations.

Mitigation: Install and use it only when you trust OOMOL and intend to let an agent operate that connected account.

Risk: Write and destructive actions can change, overwrite, or remove presentation content if the payload or target is wrong.

Mitigation: Review the exact write or batch update payload and confirm the target presentation before approving the action.

Risk: The optional first-time setup path includes a remote pipe-to-shell installer.

Mitigation: Avoid running the installer unless it has been verified against OOMOL's official installation documentation.

## Reference(s):

- [ClawHub Google Slides skill](https://clawhub.ai/oomol/skills/oo-googleslides)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Google Slides](https://workspace.google.com/products/slides/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector schemas before running Google Slides actions; command responses include data and execution metadata.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
