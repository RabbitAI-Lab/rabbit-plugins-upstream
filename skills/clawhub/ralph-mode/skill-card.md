## Description: <br>
Ralph Mode guides agents through autonomous development loops with iteration limits, backpressure gates, completion criteria, and structured progress tracking for sustained coding tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[richginsberg](https://clawhub.ai/user/richginsberg) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineering teams use this skill to plan and execute multi-iteration coding work with validation gates, progress logs, and clear stopping conditions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can edit and commit project files during autonomous coding loops. <br>
Mitigation: Run it on a branch or disposable workspace, review diffs and PROGRESS.md, and keep explicit iteration and timeout limits. <br>
Risk: Unbounded or overlapping sessions can waste time or create conflicting changes. <br>
Mitigation: Set maximum iterations and timeouts, check for existing sessions before starting, and require clear completion or blocked status in PROGRESS.md. <br>
Risk: Destructive reset commands can discard work. <br>
Mitigation: Do not run hard resets unless the workspace is backed up and the operator has explicitly approved the reset. <br>


## Reference(s): <br>
- [Backpressure Gates Reference](artifact/references/backpressure.md) <br>
- [Code Patterns Reference](artifact/references/patterns.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/richginsberg/skills/ralph-mode) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline code blocks and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update project planning, progress, and operations files during agent workflows.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
