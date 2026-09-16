## Description:

Clockify (clockify.me) skill for reading, creating, updating, and deleting Clockify data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Clockify through an OOMOL-connected account, including listing workspaces and projects, creating tasks and time entries, and updating or deleting projects with confirmation safeguards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup includes one-line remote installer commands that can execute arbitrary local code.

Mitigation: Avoid running the remote installer commands unless the installer source is independently trusted; prefer a verified, pinned installer or official package-manager flow.

Risk: Clockify write and destructive actions can change or delete workspace data.

Mitigation: Confirm the exact payload, target resource, and expected effect with the user before running write or destructive connector actions.

## Reference(s):

- [Clockify Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-clockify)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Clockify](https://clockify.me)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Clockify Connection Settings](https://console.oomol.com/app-connections?provider=clockify)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agents inspect live connector schemas before constructing request payloads.]

## Skill Version(s):

1.0.3 (source: ClawHub release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
