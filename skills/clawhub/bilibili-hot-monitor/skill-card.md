## Description: <br>
生成 B站热门视频日报，并可使用字幕和 OpenRouter 模型生成视频总结、点评后发送 HTML 邮件。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jacobzwj](https://clawhub.ai/user/jacobzwj) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and content operators use this skill to collect Bilibili popular videos, summarize video content, generate a Markdown daily report, and email the report to configured recipients. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks for Bilibili cookies, OpenRouter credentials, and Gmail SMTP credentials that can grant account or email access. <br>
Mitigation: Use a dedicated or low-risk Bilibili account, a Gmail app password, and environment variables instead of command-line secrets or long-lived plaintext configuration. <br>
Risk: The local configuration workflow can store sensitive cookies and email credentials in plaintext. <br>
Mitigation: Avoid keeping bilibili-monitor.json longer than needed, restrict local file access, and remove or rotate credentials after use. <br>
Risk: The email workflow can send generated report content to configured recipients. <br>
Mitigation: Confirm the report contents and recipient list before sending email. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jacobzwj/skills/bilibili-hot-monitor) <br>
- [Bilibili WBI signature reference](https://socialsisteryi.github.io/bilibili-API-collect/docs/misc/sign/wbi.html) <br>
- [Bilibili video summary API reference](https://socialsisteryi.github.io/bilibili-API-collect/docs/video/summary.html) <br>
- [Bilibili website](https://www.bilibili.com) <br>
- [OpenRouter API keys](https://openrouter.ai/keys) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports, HTML email content, configuration guidance, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python 3 and network access to Bilibili, optional OpenRouter models, and SMTP email service.] <br>

## Skill Version(s): <br>
1.0.21 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
