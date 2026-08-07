## Description: <br>
Enterprise WeChat voice assistant for turning voice messages and calls into intent-driven actions such as schedule lookup, todo creation, weather lookup, messaging, call minutes, dialect handling, and ticket creation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fyniujin](https://clawhub.ai/user/fyniujin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, support teams, and Enterprise WeChat administrators use this skill to handle voice-driven office workflows, customer calls, call summaries, dialect-aware responses, and ticket creation through an Enterprise WeChat robot. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A locally exposed webhook can receive external traffic if deployed through tunneling or a public URL. <br>
Mitigation: Use HTTPS, Enterprise WeChat signature and AES verification, rate limiting, and restricted network access before production use. <br>
Risk: CorpID secrets, tokens, recordings, transcripts, call records, tickets, and scheduler files may contain sensitive business or personal data. <br>
Mitigation: Apply restrictive file permissions, define retention and deletion rules, and avoid using real users or customers until those controls are reviewed. <br>
Risk: Weather lookup can send location queries to a third-party service. <br>
Mitigation: Disable or explicitly document the wttr.in lookup in sensitive environments. <br>
Risk: Outbound call recording can create privacy and consent obligations. <br>
Mitigation: Give a recording notice, record only after explicit consent, and store recordings under controlled local retention. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/wecom-voice-agent) <br>
- [Step-by-step setup guide](references/step_by_step_setup.md) <br>
- [Enterprise WeChat robot API reference](references/wecom_bot_api.md) <br>
- [Enterprise WeChat intelligent robot documentation](https://developer.work.weixin.qq.com/document/path/101039) <br>
- [Enterprise WeChat error code documentation](https://developer.work.weixin.qq.com/document/path/90313) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON examples, Python scripts, and local text, markdown, JSON, SQLite, or audio-related outputs depending on the workflow.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local session, call, ticket, transcript, and scheduler artifacts; configured deployments may call Enterprise WeChat APIs and wttr.in.] <br>

## Skill Version(s): <br>
2.3.0 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
