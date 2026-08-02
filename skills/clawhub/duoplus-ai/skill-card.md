## Description: <br>
Manage and automate DuoPlus Android cloud phones through the official OpenAPI and the synchronous HTTP Gateway. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duoplusofficial](https://clawhub.ai/user/duoplusofficial) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and support teams use this skill to discover DuoPlus cloud phones, manage lifecycle and proxy setup, and automate requested Android UI workflows on supported devices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can operate DuoPlus cloud phones using a user-provided API key. <br>
Mitigation: Provide the API key only for intended tasks, avoid echoing the full key, and review each requested phone, screenshot, proxy, and UI action before execution. <br>
Risk: Power, restart, and proxy operations can change billable devices or device configuration. <br>
Mitigation: Perform state-changing operations only when requested or when restoring the initial state; track phones powered on by the client and power them off after the task unless the user asks to leave them running. <br>
Risk: Gateway UI actions may affect accounts and data visible inside the cloud phone. <br>
Mitigation: Observe the UI before and after each action, require visible completion rather than HTTP success alone, and pause for ambiguous targets, CAPTCHA, payment, account recovery, or destructive confirmations. <br>


## Reference(s): <br>
- [DuoPlus AI skill page](https://clawhub.ai/duoplusofficial/skills/duoplus-ai) <br>
- [Publisher profile](https://clawhub.ai/user/duoplusofficial) <br>
- [DuoPlus control API and routing reference](references/control-api.md) <br>
- [HTTP Gateway automation actions](references/automation-actions.md) <br>
- [DuoPlus interface introduction](https://help.duoplus.cn/docs/introduction) <br>
- [DuoPlus cloud phone list API](https://help.duoplus.cn/docs/cloud-phone-list) <br>
- [DuoPlus cloud phone status API](https://help.duoplus.cn/docs/cloud-phone-status) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash commands, JSON parameters, and optional screenshot files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a user-provided DuoPlus API key for the current task and may write screenshots when requested with --screenshot-out.] <br>

## Skill Version(s): <br>
1.0.4 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
