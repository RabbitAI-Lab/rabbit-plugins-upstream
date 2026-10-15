## Description:

Manage and automate DuoPlus Android cloud phones, including device lifecycle, screen interaction, and authorized shell commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[duoplusofficial](https://clawhub.ai/user/duoplusofficial)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to discover and manage DuoPlus cloud phones, inspect and interact with Android screens, and run explicitly authorized device commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The DuoPlus API key grants access to remote cloud-phone controls.

Mitigation: Provide the key only for authorized tasks and avoid exposing it in reports or saved files.

Risk: Shell commands, power-on, proxy changes, and app interactions can change device state or incur charges.

Mitigation: Review commands and authorize state-changing operations; restore an initially stopped phone after the task unless asked otherwise.

Risk: Screenshots and on-device output may reveal sensitive content.

Mitigation: Inspect only the requested content and handle screenshots and outputs as sensitive data.

## Reference(s):

- [DuoPlus AI ClawHub release](https://clawhub.ai/duoplusofficial/skills/duoplus-ai)
- [DuoPlus control API and routing reference](references/control-api.md)
- [HTTP Gateway automation actions](references/automation-actions.md)
- [DuoPlus API documentation](https://help.duoplus.cn/docs/introduction)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and device status or action results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save device screenshots as PNG files when requested.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
