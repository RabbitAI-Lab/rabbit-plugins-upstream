## Description:

Box (box.com). Use this skill for ANY Box request: reading, creating, updating, and deleting data through an OOMOL-connected Box account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to browse, search, retrieve, create, upload, rename, move, describe, download, and trash Box files and folders through the oo CLI. It is intended for Box tasks where the user has already connected an OOMOL account and wants the agent to use that connection instead of calling the Box API directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup includes pipe-to-shell installation commands from a remote OOMOL URL.

Mitigation: Prefer a verified package or manually inspect the installer before execution; run the installer only when the oo CLI is missing and the source is trusted.

Risk: The skill can modify or trash Box files and folders through the connected account.

Mitigation: Confirm the exact target, payload, and expected effect with the user before any write or destructive action.

Risk: Commands act through the user's connected Box account and can access content available to that account.

Mitigation: Use the least-privileged connected account suitable for the task and inspect the live action schema before constructing payloads.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-box)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Box Homepage](https://www.box.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands inspect live connector schemas before running Box actions and return JSON responses that include execution metadata.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
