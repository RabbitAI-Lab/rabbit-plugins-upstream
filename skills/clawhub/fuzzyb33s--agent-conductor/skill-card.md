## Description: <br>
Agent Conductor helps orchestrators delegate coding, scripting, data processing, and multi-stage implementation work to CLI-based coding sub-agents while retaining planning and validation in the main session. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fuzzyb33s](https://clawhub.ai/user/fuzzyb33s) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to decompose implementation work into verifiable tasks for coding agents, coordinate serial or parallel execution, and validate results before acceptance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Delegated coding agents may modify unintended files or produce outputs that do not match the requested task. <br>
Mitigation: Confirm target files, working directories, and expected outputs before dispatch, then verify completed work with the acceptance checklist. <br>
Risk: Background or tmux/screen agent runs may continue changing files or consuming resources longer than intended. <br>
Mitigation: Use bounded timeouts where possible, monitor active runs and logs, and stop or resume work deliberately when progress stalls. <br>
Risk: Parallel agents can conflict if they share output paths, progress files, or dependent work. <br>
Mitigation: Limit concurrency to two or three agents, assign separate output directories and progress files, and use serial stages when dependencies exist. <br>


## Reference(s): <br>
- [Patterns Reference](references/patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with shell command templates and checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes task decomposition, dispatch templates, acceptance criteria, checkpoint/resume patterns, and operational guardrails.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
