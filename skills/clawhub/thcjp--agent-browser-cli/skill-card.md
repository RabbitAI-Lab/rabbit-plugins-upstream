## Description: <br>
Agent Browser CLI helps agents automate browser actions such as opening pages, clicking elements, filling forms, taking screenshots, and extracting information. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and agent users use this skill to automate authorized browser tasks such as sign-ins, form filling, screenshots, and information extraction. It is not suited for complex decisions that require human judgment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform broad real-browser actions, including clicking controls, filling forms, exporting data, and running commands. <br>
Mitigation: Use it only on sites and accounts where automation is authorized, and require explicit confirmation before form submission, account changes, data export, or command execution. <br>
Risk: The artifact advertises anti-crawler bypass behavior. <br>
Mitigation: Do not use bypass features or workflows that evade site access controls, anti-bot protections, rate limits, or terms of service. <br>
Risk: Browser automation can expose sensitive page content, credentials, screenshots, or extracted data. <br>
Mitigation: Limit the session scope, avoid unnecessary data capture, protect API keys in environment variables, and review outputs before sharing or storing them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/agent-browser-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON result examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include execution logs, status summaries, screenshots, or extracted structured data depending on the browser task.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
