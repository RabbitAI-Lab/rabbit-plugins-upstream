## Description: <br>
Use AgentMesh Job Agent for resume-driven job discovery, signed review and automatic selected delivery on Boss直聘, 猎聘, 智联招聘 and 51Job. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiyangnan](https://clawhub.ai/user/jiyangnan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and job seekers use this skill to drive AgentMesh Job Agent for resume analysis, job discovery, signed review, and delivery of selected applications or greetings across supported recruiting platforms. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can automatically send real job applications and platform greetings after a round starts without a final per-platform confirmation. <br>
Mitigation: Review selected jobs carefully before delivery begins, and start rounds only when automatic delivery of selected items is acceptable. <br>
Risk: The skill may use the user's resume, API key, browser login sessions, and recruiting-platform accounts. <br>
Mitigation: Use accounts and resumes intended for this workflow, keep credential setup under user control, and stop when the CLI reports required user action. <br>


## Reference(s): <br>
- [Job Agent homepage](https://jobagent.agentmesh360.com/) <br>
- [AgentMesh360 app](https://agentmesh360.com/app/) <br>
- [ClawHub skill page](https://clawhub.ai/jiyangnan/skills/job-agent) <br>
- [Publisher profile](https://clawhub.ai/user/jiyangnan) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text] <br>
**Output Format:** [Markdown instructions with CLI command blocks and concise status/reporting text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides the agent to run the jobagent CLI, relay required user prompts, and report audit and delivery results.] <br>

## Skill Version(s): <br>
0.4.7 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
