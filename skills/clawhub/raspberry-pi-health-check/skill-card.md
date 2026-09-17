## Description:

Assesses slow, hot, freezing, restarting, unstable, storage-constrained, or service-failing Raspberry Pi systems using read-only checks for uptime, load, memory, swap, disk usage, temperature, throttling, undervoltage, resource-heavy processes, and systemd services, with optional permissioned JishuBuddy SSH evidence collection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bowen-aijishu](https://clawhub.ai/user/bowen-aijishu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and support engineers use this skill to collect and interpret Raspberry Pi health evidence before troubleshooting performance, thermal, storage, power, or service reliability issues. It emphasizes read-only diagnosis and explicit approval before installing or launching helper tooling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the helper tool downloads software from npm and writes to the global npm prefix.

Mitigation: Run the preflight first, show the exact platform, version, registry, prefix, and install command, and install only after explicit approval for the displayed version.

Risk: Running the installer or helper tool with elevated privileges could unnecessarily expand access to local files, SSH configuration, keys, agents, or remote devices.

Mitigation: Do not use sudo; run under the operator's normal account and review SSH/device configuration changes before writing them.

Risk: JishuBuddy sends activation and heartbeat telemetry by default.

Mitigation: Set JISHUBUDDY_TELEMETRY_DISABLED=true before launch when telemetry is not desired.

Risk: A failed, missing, or unsupported device check could be misread as a healthy result.

Mitigation: Mark unavailable checks as blocked or unconfirmed and base conclusions only on actual command output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bowen-aijishu/skills/raspberry-pi-health-check)
- [Publisher profile](https://clawhub.ai/user/bowen-aijishu)
- [OpenClaw homepage](https://github.com/x-aijishu/jishubuddy-skills/tree/main/raspberry-pi-health-check)
- [JishuBuddy npm package](https://www.npmjs.com/package/jishubuddy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports each check with evidence, assessment, and confirmed, unconfirmed, or blocked status; missing data is not treated as healthy.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
