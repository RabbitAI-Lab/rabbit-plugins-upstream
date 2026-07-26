## Description: <br>
Manages multiple user instructions as independent tasks, with priority scheduling, dependency handling, progress tracking, result collection, and execution reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erichy777](https://clawhub.ai/user/erichy777) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and automation-focused agent users use this skill to coordinate multiple independent tasks, order them by priority and dependencies, and summarize execution outcomes. It is best suited for workflows where the user can review proposed file, shell, browser, network, or data operations before execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can coordinate broad automation tasks involving shell commands, file changes, browser actions, network calls, API calls, and database queries. <br>
Mitigation: Require review and explicit confirmation before deletes, overwrites, shell or script execution, uploads, database changes, and external network calls. <br>
Risk: Parallel execution can amplify mistakes by running multiple unsafe or incorrect tasks at once. <br>
Mitigation: Use conservative concurrency limits, sandbox sensitive workspaces, and review the generated task queue before execution. <br>
Risk: Automated retry behavior can repeat a harmful or failing operation. <br>
Mitigation: Limit retries for destructive or externally visible operations and inspect failure reports before retrying. <br>


## Reference(s): <br>
- [Parallel Task Executor Skill Page](https://clawhub.ai/erichy777/skills/parallel-task-executor) <br>
- [Execution Report Format](references/reports.md) <br>
- [Task Priority Specification](references/priorities.md) <br>
- [Scheduling Algorithm Notes](references/scheduler.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration, Markdown, JSON] <br>
**Output Format:** [Markdown with inline code blocks and JSON execution reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include task queues, progress summaries, retry details, and success or failure reports.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
