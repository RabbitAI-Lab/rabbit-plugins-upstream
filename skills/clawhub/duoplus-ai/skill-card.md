## Description: <br>
Manage and automate DuoPlus Android cloud phones through the official OpenAPI and the synchronous HTTP Gateway. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duoplusofficial](https://clawhub.ai/user/duoplusofficial) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to manage DuoPlus cloud-phone lifecycle state, configure proxy access, inspect device status, and automate Android UI tasks on a selected cloud phone. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can operate DuoPlus cloud phones with a user-provided API key, including power, proxy, account, payment, or destructive actions. <br>
Mitigation: Provide an API key only for the task at hand and explicitly confirm device power, proxy, account, payment, or destructive actions before execution. <br>
Risk: Screenshots and UI state may reveal private app data from the controlled Android device. <br>
Mitigation: Review screen observations carefully, avoid exposing screenshots unnecessarily, and treat captured UI state as sensitive task data. <br>
Risk: Powering on temporary cloud-phone compute can start billing. <br>
Mitigation: Track phones powered on by the workflow and restore the initial stopped state with power-off unless the user asked to leave the phone running. <br>
Risk: Unsupported or not-ready phones can cause failed automation or unintended lifecycle changes. <br>
Mitigation: Use list/status/ready checks first, require http_status=1 for Gateway automation, and verify UI state after each action rather than relying on HTTP 200 alone. <br>


## Reference(s): <br>
- [DuoPlus AI Skill](https://clawhub.ai/duoplusofficial/skills/duoplus-ai) <br>
- [DuoPlus control API and routing reference](references/control-api.md) <br>
- [HTTP Gateway automation actions](references/automation-actions.md) <br>
- [DuoPlus interface introduction](https://help.duoplus.cn/docs/introduction) <br>
- [DuoPlus cloud phone list](https://help.duoplus.cn/docs/cloud-phone-list) <br>
- [DuoPlus cloud phone status](https://help.duoplus.cn/docs/cloud-phone-status) <br>
- [DuoPlus cloud phone detail](https://help.duoplus.cn/docs/huo-qu-yun-ji-xiang-qing) <br>
- [DuoPlus batch power on](https://help.duoplus.cn/docs/batch-power-on) <br>
- [DuoPlus batch power off](https://help.duoplus.cn/docs/pi-liang-guan-ji) <br>
- [DuoPlus batch restart](https://help.duoplus.cn/docs/pi-liang-chong-qi) <br>
- [DuoPlus proxy list](https://help.duoplus.cn/docs/proxy-list) <br>
- [DuoPlus proxy initialization](https://help.duoplus.cn/docs/proxy-init) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Code, JSON, Files, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write screenshot image files when ui-state or action commands include screenshot output paths.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
