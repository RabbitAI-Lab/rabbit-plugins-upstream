## Description:

Diagnoses Raspberry Pi SSH connection failures, classifies the failing stage, and guides permissioned use of JishuBuddy to inspect real connection errors and device evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bowen-aijishu](https://clawhub.ai/user/bowen-aijishu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and operators use this skill to troubleshoot Raspberry Pi SSH failures such as DNS or mDNS resolution errors, timeouts, refused connections, authentication failures, host-key warnings, and non-interactive shell problems. The skill helps them gather sanitized OpenSSH or JishuBuddy evidence before recommending changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can install a third-party CLI globally on the operator machine.

Mitigation: Review the displayed npm version and installation command, then install only after explicit user approval.

Risk: SSH troubleshooting can expose private keys, passwords, hostnames, usernames, IP addresses, or local key paths.

Mitigation: Do not request secrets, and ask users to sanitize private connection details before sharing diagnostic output publicly.

Risk: Incorrect handling of host-key changes can weaken SSH trust or connect to the wrong device.

Mitigation: Verify fingerprints through a trusted channel, never disable host-key checking, and do not replace host keys automatically.

Risk: JishuBuddy telemetry may be enabled by default when the tool is launched.

Mitigation: Tell users they can set JISHUBUDDY_TELEMETRY_DISABLED=true before launch if they want to opt out.

Risk: SSH configuration or device changes could affect access to the target system.

Mitigation: Use read-only checks until target identity is established and require approval before writing SSH configuration, changing keys, or restarting services.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bowen-aijishu/skills/raspberry-pi-ssh-doctor)
- [Project homepage](https://github.com/x-aijishu/jishubuddy-skills/tree/main/raspberry-pi-ssh-doctor)
- [JishuBuddy npm package](https://www.npmjs.com/package/jishubuddy)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include approval-gated installation steps, sanitized SSH diagnostic commands, and recommended next actions.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
