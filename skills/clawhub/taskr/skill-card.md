## Description: <br>
Taskr helps OpenClaw agents create and maintain persistent cloud task plans, notes, and status checkpoints that survive context resets and can be resumed across agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[echo-of-machines](https://clawhub.ai/user/echo-of-machines) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and users of OpenClaw agents use Taskr to plan multi-step work, preserve task context across sessions, coordinate handoffs between agents, and maintain task notes as an audit trail. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Task titles, project context, and progress notes may contain sensitive information stored in Taskr. <br>
Mitigation: Review what is stored in tasks and notes, avoid recording secrets, and use a separate or scoped project where possible. <br>
Risk: MCP_USER_API_KEY exposure could grant access to the user's Taskr project. <br>
Mitigation: Keep the API key out of chat, logs, notes, and source control, and rotate it if exposure is suspected. <br>
Risk: Incomplete or abandoned task states can mislead users reviewing progress. <br>
Mitigation: Complete or skip tasks deliberately, and attach a FINDING note when work is skipped. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/echo-of-machines/skills/taskr) <br>
- [Taskr Homepage](https://taskr.one) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration, API calls] <br>
**Output Format:** [Markdown guidance with inline JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MCP_API_URL, MCP_PROJECT_ID, and MCP_USER_API_KEY; stores task titles, project context, task notes, and status updates in Taskr.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
