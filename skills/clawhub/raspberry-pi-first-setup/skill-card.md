## Description:

Helps users safely prepare a new Raspberry Pi from imaging through first SSH or serial validation, including headless setup, Wi-Fi, hostname, and first-boot troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bowen-aijishu](https://clawhub.ai/user/bowen-aijishu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and Raspberry Pi users use this skill to prepare first-time Raspberry Pi setup, diagnose headless boot or network reachability issues, and continue with permissioned SSH or serial validation when real device evidence is required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Global JishuBuddy installation writes to the operator computer's npm prefix.

Mitigation: Run the preflight first, show the exact version, registry, prefix, and command, and install only after explicit approval.

Risk: SSH or serial validation can affect devices the user did not intend to manage if the target is misidentified.

Mitigation: Confirm the device, host key, setup stage, and intended SSH or serial target before enabling connections or writing configuration.

Risk: JishuBuddy telemetry may be unexpected in some environments.

Mitigation: Tell users they can disable telemetry before launch with JISHUBUDDY_TELEMETRY_DISABLED=true.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bowen-aijishu/skills/raspberry-pi-first-setup)
- [Skill homepage](https://github.com/x-aijishu/jishubuddy-skills/tree/main/raspberry-pi-first-setup)
- [JishuBuddy npm package](https://www.npmjs.com/package/jishubuddy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates measured device evidence from unconfirmed physical checks and blocked validation steps.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
