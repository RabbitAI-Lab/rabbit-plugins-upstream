## Description: <br>
Creates 2Do tasks from Chinese or English natural-language requests by extracting title, due date, priority, list, and tags, then sending the task to the user's configured 2Do inbox by email. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chuckiefan](https://clawhub.ai/user/chuckiefan) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers running OpenClaw or Moltbot use this skill to capture natural-language reminders and todos from chat into 2Do via email, with optional due dates, priorities, lists, and tags. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad no-prefix task capture can send ordinary chat text through the user's SMTP provider to 2Do. <br>
Mitigation: Configure the agent to invoke this skill only for explicit task-creation requests and require confirmation before sending. <br>
Risk: SMTP credentials and the 2Do recipient address are required for operation. <br>
Mitigation: Use a dedicated SMTP account or app-specific password and scope the required environment variables only to this skill. <br>
Risk: Running without compiled output can use a development npx fallback. <br>
Mitigation: Build the project before deployment so the wrapper runs compiled dist/main.js, or avoid the fallback path. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/chuckiefan/skills/moltbot-plugin-2do) <br>
- [OpenClaw Documentation](https://docs.openclaw.ai) <br>
- [2Do Email to 2Do Knowledge Base](https://www.2doapp.com/kb/category/ios/email-to-2do/44/) <br>
- [2Do Website](https://www.2doapp.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration] <br>
**Output Format:** [Plain text status messages and shell command invocations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Sends SMTP email to the configured 2Do inbox; requires Node.js and SMTP/2Do environment variables.] <br>

## Skill Version(s): <br>
1.0.2 (source: evidence.release.version, package.json, CHANGELOG) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
