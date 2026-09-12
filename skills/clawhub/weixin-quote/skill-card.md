## Description:

Guides an agent through consent, backup, implementation, restart, verification, and rollback steps to add quote-as-context handling to a local openclaw-weixin plugin.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yechang1450](https://clawhub.ai/user/yechang1450)

### License/Terms of Use:

MIT

## Use Case:

Developers and OpenClaw users use this skill when they explicitly want a local agent to enable or repair quote-context behavior in the openclaw-weixin channel. The skill is guidance-only and has the agent modify the user's installed plugin after consent and backup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill guides an agent to modify a locally installed WeChat channel plugin.

Mitigation: Require explicit consent before writes and confirm the exact plugin path, files to change, backup location, restart impact, and rollback steps.

Risk: Quote handling retains message text locally so quoted messages can be resolved after restarts.

Mitigation: Keep the quote index local, owner-only readable, limited to required content, subject to 24-hour expiry and per-recipient caps, and exclude message bodies from logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yechang1450/skills/weixin-quote)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown guidance with inline shell commands and implementation specifications]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance requires explicit user consent, verified backups, local-only retained quote index controls, and rollback reporting before and after modifying the installed plugin.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
