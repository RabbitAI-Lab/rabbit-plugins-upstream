## Description: <br>
Provides a structured coding workflow for individual developers, including planning, step-by-step implementation, validation, checkpoint tracking, and explicit preference memory. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers use this skill to structure personal coding work from request through planning, execution, verification, and delivery. It helps split tasks, track checkpoints, remember explicitly stated preferences, and prepare quality checks before handoff. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to read, write, test, and run commands in a project, which may affect local files. <br>
Mitigation: Keep use scoped to the active project and review proposed file changes and commands before relying on them. <br>
Risk: Preference memory and checkpoint files may capture sensitive details if the user stores them there. <br>
Mitigation: Do not place secrets in memory.md or checkpoint files, and store only preferences the user explicitly wants remembered. <br>
Risk: The optional callback_url field can send completion information outside the local environment. <br>
Mitigation: Use callback_url only when remote notification behavior is intentional and the transmitted information is understood. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/thcjp/skills/code-dev-v1-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline code, shell commands, checklists, and optional JSON status output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose file edits, tests, checkpoint records, and local preference or checkpoint files for user review.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
