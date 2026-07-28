## Description: <br>
Use AgentMesh Job Agent for resume-driven job discovery, signed review and automatic selected delivery on Boss直聘, 猎聘, 智联招聘 and 51Job. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiyangnan](https://clawhub.ai/user/jiyangnan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and job seekers use this skill to drive the AgentMesh Job Agent CLI through resume analysis, platform login, job discovery, selected-list review, delivery, and audit flows across supported Chinese job platforms. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can submit real job applications after a round starts and the selected list is shown, without asking again per platform. <br>
Mitigation: Confirm the target role, resume, platforms, API key, browser sessions, selected list, and delivery preview before continuing to send commands. <br>
Risk: The workflow preserves login state and account-bound local data across browser sessions. <br>
Mitigation: Use revocable credentials, confirm account ownership when prompted, and rely on the CLI account bind or switch commands instead of manually editing local state. <br>
Risk: Cloud resume analysis and discovery can consume credits when the signed cloud response authorizes charges. <br>
Mitigation: Report the CLI-provided balance source, charges, refunds, and insufficient-credit errors, and stop for user action only when the CLI marks it required. <br>


## Reference(s): <br>
- [AgentMesh360 Job Agent homepage](https://jobagent.agentmesh360.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands, compact tables, and concise status summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include delivery previews, category counts, audit evidence, credit status, and next-step guidance emitted by the CLI.] <br>

## Skill Version(s): <br>
0.5.3 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
