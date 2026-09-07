## Description:

Box (box.com). Use this skill for ANY Box request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to work with Box cloud content through an OOMOL-connected account, including reading, searching, uploading, updating, and deleting files or folders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Box content available to the connected OOMOL account.

Mitigation: Install and use it only with an account whose Box access is appropriate for the intended task.

Risk: Upload, update, and delete actions can change or remove Box content.

Mitigation: Confirm the exact target, payload, and expected effect with the user before executing write or destructive actions.

Risk: Actions depend on live connector schemas and connected account state.

Mitigation: Fetch the action schema before constructing payloads and use first-time setup steps only after an authentication or connection failure.

## Reference(s):

- [Box homepage](https://www.box.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Skill release page](https://clawhub.ai/oomol/skills/oo-box)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [Service icon](https://static.oomol.com/logo/third-party/box.svg)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with oo CLI commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; write and destructive actions require confirmation.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
