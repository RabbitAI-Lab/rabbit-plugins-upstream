## Description: <br>
Report helps agents configure recurring custom reports from user-defined data sources, schedule them with cron, format results, and deliver them through chat, files, Telegram, email, or trusted webhook destinations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Teams and individual users use this skill to define scheduled or on-demand reports, collect configured data sources with user-provided credentials, and deliver formatted summaries to trusted destinations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can retain report history and generated reports locally under ~/report. <br>
Mitigation: Install it only when local report storage is intended, and avoid configuring broad or sensitive local paths unless needed. <br>
Risk: Configured delivery channels can send report contents outside the local device. <br>
Mitigation: Use chat or file delivery for sensitive reports, and configure Telegram, email, or webhook delivery only for destinations the user trusts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/report) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline YAML and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local report configuration, history, and generated report files under ~/report when used as documented.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
