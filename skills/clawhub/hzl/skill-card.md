## Description: <br>
Persistent task ledger for agent coordination. Plan multi-step work, checkpoint progress across session boundaries, and coordinate across multiple agents with project pool routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tmchow](https://clawhub.ai/user/tmchow) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agent operators use HZL to track multi-step work, checkpoint progress across sessions, and coordinate task handoffs across one or more agents using the hzl CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Task titles, descriptions, checkpoints, and shared projects can persist sensitive work context. <br>
Mitigation: Avoid placing secrets in task text or checkpoints, and scope shared projects carefully before collaborating or syncing. <br>
Risk: Force initialization and prune commands can permanently delete HZL task data. <br>
Mitigation: Use force, yes, or prune options only when the user explicitly asks to delete data and the target database or project has been confirmed. <br>
Risk: Background service, gateway token, and cloud sync features can expose or transmit task data when enabled. <br>
Mitigation: Enable service, gateway token, and cloud sync features only intentionally; protect tokens and restrict service exposure to the required network scope. <br>


## Reference(s): <br>
- [HZL project homepage](https://github.com/tmchow/hzl) <br>
- [HZL documentation site](https://hzl-tasks.com) <br>
- [ClawHub HZL listing](https://clawhub.ai/tmchow/skills/hzl) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces operational instructions for the hzl CLI, including JSON-output command variants where supported.] <br>

## Skill Version(s): <br>
3.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
