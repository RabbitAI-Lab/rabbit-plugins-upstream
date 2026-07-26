## Description: <br>
Agent Browser Cli guides agents in using the agent-browser CLI to automate browser tasks such as sign-ins, form filling, screenshots, and information extraction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to control browser sessions through CLI commands for repetitive web tasks, page snapshots, clicks, form fills, screenshots, and extraction. It is not suited for tasks that require human creative judgment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Browser automation can submit forms, post messages, make purchases, change accounts, upload files, download files, or otherwise send data and alter remote state. <br>
Mitigation: Require explicit user approval before any action that sends data, changes state, or accesses an authenticated session. <br>
Risk: The artifact advertises anti-crawler bypass, which can violate site policies or legal constraints. <br>
Mitigation: Do not use the skill for anti-bot or anti-crawler bypass; only automate pages the user is authorized to access. <br>
Risk: The skill requests broad exec-backed authority to drive a local browser CLI. <br>
Mitigation: Review proposed commands before execution and run the skill with least-privilege local permissions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/agent-browser-cli) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include browser task summaries, extracted data, execution logs, and recovery guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
