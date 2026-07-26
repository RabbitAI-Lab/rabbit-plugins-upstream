## Description: <br>
Dingding provides a zero-dependency DingTalk group-robot CLI for text, markdown, and link notifications with HMAC signing, plus guidance for DingTalk Open Platform API development. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhangifonly](https://clawhub.ai/user/zhangifonly) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and agents use this skill to send DingTalk group notifications for CI/CD status, monitoring alerts, daily reports, and targeted reminders. It also provides practical guidance for DingTalk Open Platform token, approval, contact, and work-notification APIs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent needs access to a DingTalk webhook URL and optional signing secret to send messages. <br>
Mitigation: Use a narrowly scoped robot, prefer DingTalk signing or IP restrictions, and avoid exposing the webhook or signing secret beyond the intended runtime. <br>
Risk: A supplied markdown file can be posted to a DingTalk group. <br>
Mitigation: Confirm the destination and inspect sensitive files before sending markdown content. <br>
Risk: Using @all or posting to large groups can create broad notification impact. <br>
Mitigation: Require explicit user confirmation before using @all or posting high-impact alerts. <br>


## Reference(s): <br>
- [Dingding Skill Page](https://clawhub.ai/zhangifonly/skills/dingding) <br>
- [DingTalk Open Platform](https://open.dingtalk.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON CLI responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses user-provided DingTalk webhook settings and may read a local markdown file only when that path is supplied to the markdown command.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
