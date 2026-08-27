## Description:

OpenClaw Skill Packager packages, validates, and prepares OpenClaw skills for backup, deployment, or reuse across environments while checking structure, secrets, and platform compatibility.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT

## Use Case:

Developers and operators use this skill to package one or more OpenClaw skills into portable, validated bundles before backup, deployment, sharing, or workspace migration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill inspects and copies local OpenClaw skill folders, so selecting an unintended source path could package files the user did not mean to share.

Mitigation: Use the skill only on intended skill paths and review the generated package before backup, deployment, or external sharing.

Risk: A packaged skill could expose secrets if source files contain credentials or tokens.

Mitigation: Run the described secret checks before and after copying, remove any sensitive files from the package, and rescan before sharing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/skill-packager)
- [README](artifact/README.md)
- [Skill source](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, markdown, files]

**Output Format:** [Markdown guidance with shell command snippets and packaging report text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce copied skill package files after validating source paths, structure, secret exposure, and platform compatibility.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; skill frontmatter lists 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
