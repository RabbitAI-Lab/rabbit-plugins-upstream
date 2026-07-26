## Description: <br>
生活助手免费版 helps individual users manage tasks, summarize long messages, coordinate schedules, and organize local personal information. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Personal users, freelancers, and independent developers use this skill to capture and break down tasks, track due dates, summarize emails, check schedule conflicts, and keep notes or reminders in a local personal-assistant workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The quick-start setup command can overwrite an existing ~/.assistant/config.json file. <br>
Mitigation: Check for an existing config file and back it up or merge settings before running commands that redirect output to ~/.assistant/config.json. <br>
Risk: The skill creates and updates local task, email, note, and reminder files under ~/.assistant. <br>
Mitigation: Review generated files before relying on them and apply normal local backup and access-control practices for personal data. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell snippets, Python examples, YAML configuration, and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Free edition focuses on single-user local storage under ~/.assistant and does not require external API keys.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
