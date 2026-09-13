## Description:

安装、启动和使用 Proactive Agent，记录项目进展并在合适时机提醒下一步。

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to install, operate, and validate a Proactive Agent service that tracks project progress across conversations and suggests next steps through a web workspace. It currently focuses on Hermes integration for conversation capture and approved same-session resume.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the external runtime gives it a high-trust role over Hermes conversations and session actions.

Mitigation: Install only after trusting the publisher and exact release artifact, verifying the wheel, and reviewing Hermes modifications in dry-run mode.

Risk: Complete Hermes question-and-answer content is stored locally and processed by the service.

Mitigation: Confirm the data directory and keep credentials out of logs, environment dumps, and copied outputs.

Risk: Connector setup modifies Hermes source and configuration.

Mitigation: Use the documented dry-run, preserve rollback paths for Hermes source/configuration and user data, and validate the target session before considering setup complete.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/sensenova-skills/skills/sn-proactive-agent)
- [Installation and Operation](references/install/overview.md)
- [macOS Installation](references/install/macos.md)
- [Windows Installation](references/install/windows.md)
- [Hermes Integration](references/connectors/hermes.md)
- [Hermes Installation Documentation](https://hermes-agent.nousresearch.com/docs/getting-started/installation/)
- [pipx Installation Documentation](https://pipx.pypa.io/stable/how-to/install-pipx.html)
- [pipx CLI Reference](https://pipx.pypa.io/stable/reference/cli.html)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Markdown]

**Output Format:** [Markdown with inline shell and PowerShell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes OS-specific setup paths, diagnostic checks, and validation steps for Hermes integration.]

## Skill Version(s):

2026.9.11 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
