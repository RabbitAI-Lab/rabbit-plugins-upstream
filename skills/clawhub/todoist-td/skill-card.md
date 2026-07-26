## Description: <br>
Helps an agent use the td Todoist CLI to list, summarize, add, update, complete, delete, and move Todoist tasks from the terminal. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mattjefferson](https://clawhub.ai/user/mattjefferson) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to have an agent manage Todoist tasks through the td CLI, including agenda review, task creation, task updates, completion, deletion, and project or label workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Setup commands install and link the upstream td CLI, creating ordinary supply-chain exposure. <br>
Mitigation: Review or pin the upstream Todoist CLI before running setup commands. <br>
Risk: Generic task, agenda, or checklist requests may cause the agent to consult or modify Todoist account data. <br>
Mitigation: Install only when the agent is intended to access Todoist, and confirm before destructive task deletion. <br>
Risk: Ambiguous task matches could lead to edits on the wrong Todoist item. <br>
Mitigation: Ask for clarification or present candidates when multiple tasks match a user description. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mattjefferson/skills/todoist-td) <br>
- [Todoist CLI repository](https://github.com/Doist/todoist-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and concise task summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses td JSON or NDJSON output when available; confirms destructive deletions and asks for clarification when multiple tasks match.] <br>

## Skill Version(s): <br>
0.1.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
