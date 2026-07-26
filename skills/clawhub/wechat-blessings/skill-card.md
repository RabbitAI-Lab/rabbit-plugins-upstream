## Description: <br>
Create personalized Chinese or multilingual greetings for holidays, birthdays, milestones, and customer care, then preview and send them through WeChat only after explicit confirmation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhimibuhui](https://clawhub.ai/user/zhimibuhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and teams use this skill to draft culturally appropriate greetings for personal, holiday, milestone, or customer-care messages and optionally send or schedule them through WeChat after reviewing an exact preview. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A message could be sent or scheduled to the wrong WeChat recipients or at the wrong time if the preview is not checked. <br>
Mitigation: Review the exact text, recipient list, schedule, and confirmation code before executing delivery. <br>
Risk: The skill requires an operations endpoint and bearer token for execution. <br>
Mitigation: Configure credentials only in trusted environments, limit token scope, and avoid exposing tokens in prompts, previews, or logs. <br>
Risk: Batch or customer-care greetings can imply unsupported personal knowledge or use manipulative wording. <br>
Mitigation: Use only verified recipient details and avoid pressure, unsupported benefits, health promises, or identical mass-personalized claims. <br>


## Reference(s): <br>
- [Blessing style guide](artifact/references/styles.md) <br>
- [ClawHub skill page](https://clawhub.ai/zhimibuhui/skills/wechat-blessings) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown conversation with optional bash command examples and JSON preview or execution output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires explicit confirmation before WeChat delivery; supports one or more recipients, scheduled sending, and configured WX_OPENCLAW_OPS_URL and WX_OPENCLAW_OPS_TOKEN credentials.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
