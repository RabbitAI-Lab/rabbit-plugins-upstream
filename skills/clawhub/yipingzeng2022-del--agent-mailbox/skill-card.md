## Description:

Use when a bot or person needs to install, authorize, or operate an Agent mailbox (agent.qq.com / agently-cli) — install failures, OAuth login, send/reply with two-step confirmation, attachments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yipingzeng2022-del](https://clawhub.ai/user/yipingzeng2022-del)

### License/Terms of Use:

MIT

## Use Case:

Developers, agents, and mailbox operators use this skill to install and authorize agently-cli, identify the connected mailbox, and manage email and attachments. It also guides troubleshooting for setup, authentication, and send confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation guidance runs a network-fetched installer and changes the npm registry setting.

Mitigation: Review the installer before running it, confirm the registry is trusted, and restore the previous registry setting when appropriate.

Risk: Email sends can disclose information externally, and the --confirmed option skips the normal confirmation step.

Mitigation: Check recipients and message content with --dry-run and obtain user approval before sending; use the confirmation token flow when review is required.

Risk: Troubleshooting includes sudo for global installation, which can make system-level changes.

Mitigation: Prefer a user-scoped npm setup where practical and use elevated privileges only when needed.

Risk: The security review was partial because three referenced local paths could not be resolved.

Mitigation: Review the referenced paths and their contents before adopting the skill.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/yipingzeng2022-del/skills/agent-mailbox)
- [Node.js](https://nodejs.org)
- [nvm installer script (review before running)](https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Step-by-step instructions; no files are produced.]

## Skill Version(s):

1.0.0 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
