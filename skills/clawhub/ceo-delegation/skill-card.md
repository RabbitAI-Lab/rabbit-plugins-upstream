## Description: <br>
A CEO-style workflow that directs an agent to delegate tasks to sub-agents, monitor progress, report status, and use separate reviewers for acceptance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[eisonme](https://clawhub.ai/user/eisonme) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to coordinate multi-step or time-consuming agent work by assigning executor and reviewer sub-agents, monitoring progress, and summarizing delivery status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill broadly directs the primary assistant to delegate most work to sub-agents, which can increase cost, runtime, and operational complexity. <br>
Mitigation: Set explicit limits for sub-agent creation, model selection, timeouts, retries, and budget before enabling the skill. <br>
Risk: Delegated work and memory recording may expose sensitive task content to sub-agents or persistent memory. <br>
Mitigation: Avoid sensitive tasks unless sharing with sub-agents and memory is acceptable, and disable or constrain memory writes where needed. <br>
Risk: The workflow requires separate executor and reviewer agents, but review quality depends on the reviewer prompt and available evidence. <br>
Mitigation: Require clear acceptance criteria and have the primary assistant summarize reviewer findings before final delivery. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/eisonme/skills/ceo-delegation) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands] <br>
**Output Format:** [Markdown guidance with example agent API calls and optional shell command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes delegation labels, progress summaries, acceptance checklist items, and optional monitor.py status output.] <br>

## Skill Version(s): <br>
1.0.0 (source: package.json and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
