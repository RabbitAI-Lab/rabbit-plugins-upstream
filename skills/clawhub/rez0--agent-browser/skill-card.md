## Description: <br>
Agent Browser provides a browser automation CLI that lets AI agents navigate pages, fill forms, click controls, take screenshots, extract data, test web apps, and automate supported Electron or Slack workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rez0](https://clawhub.ai/user/rez0) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use Agent Browser when an agent needs to automate browser interactions, web app testing, data extraction, Slack workflows, or supported Electron desktop app tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent broad authority over websites, logged-in browser sessions, desktop apps, Slack, and persisted state. <br>
Mitigation: Install it only where that level of browser and app automation is intended, and avoid sensitive accounts unless the automation task requires them. <br>
Risk: Browser automation can submit forms, send messages, or act through stored authentication. <br>
Mitigation: Require explicit confirmation before sending messages, submitting forms, or using stored authentication. <br>
Risk: The artifact delegates detailed workflows to CLI-provided content that can affect agent behavior. <br>
Mitigation: Review the npm package and CLI-provided workflow content before deployment. <br>


## Reference(s): <br>
- [Agent Browser on ClawHub](https://clawhub.ai/rez0/agent-browser) <br>
- [Publisher profile: rez0](https://clawhub.ai/user/rez0) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct the agent to load version-matched workflow content from the installed agent-browser CLI.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
