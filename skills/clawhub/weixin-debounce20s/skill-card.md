## Description:

Guidance-only setup skill that helps an agent enable a 20-second trailing debounce for text bursts in a locally installed openclaw-weixin channel plugin after user consent and backup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yechang1450](https://clawhub.ai/user/yechang1450)

### License/Terms of Use:

MIT

## Use Case:

Developers and OpenClaw users use this skill when they explicitly want an agent to enable or repair text-message debouncing for a local openclaw-weixin channel plugin. The skill guides consent, backup, implementation, gateway restart, verification, and rollback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill guides an agent to modify a locally installed WeChat channel plugin and restart the gateway.

Mitigation: Proceed only after reviewing the target path, plugin version, affected files, restart impact, and confirmation prompt.

Risk: A local plugin change may need rollback if the build, restart, or verification does not behave as expected.

Mitigation: Create and verify readable backups before modification, keep the backup path, and use it for rollback if validation fails.

Risk: Running writes or builds with elevated privileges could change system-level plugin installations.

Mitigation: Use the normal user account only and stop if the plugin is installed in a system-level location.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yechang1450/skills/weixin-debounce20s)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown guidance with inline shell commands and implementation steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The guided workflow modifies local plugin files only after explicit confirmation and backup.]

## Skill Version(s):

1.0.10 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
