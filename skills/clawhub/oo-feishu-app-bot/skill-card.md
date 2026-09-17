## Description:

Feishu App Bot helps agents use the OOMOL-connected oo CLI to read, create, update, and delete Feishu App Bot data through live connector schemas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Feishu App Bot through OOMOL's connector, including chat, message, Drive, Docs, Sheets, Base, Calendar, Tasks, OKRs, Wiki, Slides, Mail, Whiteboards, and meeting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes executing a remote installer directly.

Mitigation: Review the installer path before installing and prefer a package-manager or version-pinned installation method with checksum or signature verification.

Risk: Write and destructive Feishu actions can modify, overwrite, or delete workspace data.

Mitigation: Confirm the exact target, payload, and expected effect before running write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-feishu-app-bot)
- [oo CLI Repository](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Feishu App Bot Homepage](https://open.feishu.cn)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The agent inspects each live action schema before constructing a payload.]

## Skill Version(s):

1.0.5 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
