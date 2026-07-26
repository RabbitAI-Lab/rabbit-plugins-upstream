## Description: <br>
TaskMaster helps agents break down complex work, choose cost-appropriate AI models, spawn delegated sub-agent tasks, track progress, and manage token budgets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jlwrow](https://clawhub.ai/user/jlwrow) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and external agent users use TaskMaster to plan multi-step AI work, delegate subtasks to model tiers selected by complexity, and monitor estimated or actual task cost against a budget. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated sessions_spawn commands may initiate delegated agent work with model, timeout, label, and cleanup settings. <br>
Mitigation: Review generated command payloads before running them and keep explicit task budgets in place. <br>
Risk: Cost tracking is less complete than the documentation claims, and some values may be estimates rather than verified token usage. <br>
Mitigation: Treat cost data as estimates until token usage is independently verified with session status data. <br>
Risk: Task descriptions and cost history may be written to taskmaster-costs.json. <br>
Mitigation: Avoid placing secrets, credentials, or sensitive project details in task descriptions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jlwrow/skills/taskmaster) <br>
- [Model Selection Rules](artifact/references/model-selection-rules.md) <br>
- [Task Templates](artifact/references/task-templates.md) <br>
- [Token Tracking Guide](artifact/TOKEN_TRACKING_README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, JSON spawn-command payloads, and Python code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces model-selection recommendations, budget estimates, task status summaries, and generated sessions_spawn command payloads that should be reviewed before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
