## Description:

Install OpenClaw's official WeChat plugin and complete account pairing via QR code scan.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lanlan314](https://clawhub.ai/user/lanlan314)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users use this skill to install the WeChat plugin and pair a WeChat account through a local QR-code flow without using command-line steps directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install an npm package automatically as part of the WeChat plugin setup.

Mitigation: Run it only when intentionally installing the WeChat plugin, and verify the npm package source and version in sensitive environments.

Risk: The skill saves a WeChat bot token locally and updates OpenClaw channel configuration.

Mitigation: Review local account storage and channel allowlist settings after pairing, and remove saved credentials when they are no longer needed.

Risk: The skill may restart the OpenClaw gateway in the background.

Mitigation: Use it during a maintenance window or when an OpenClaw gateway restart is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lanlan314/skills/wechat)
- [WeChat iLink API base](https://ilinkai.weixin.qq.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Files, API calls, Guidance]

**Output Format:** [Local HTML pairing page, generated QR image, JSON account files, and OpenClaw configuration changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates temporary files under /tmp, saves WeChat account state under ~/.openclaw/openclaw-weixin, and may restart the OpenClaw gateway.]

## Skill Version(s):

2.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
