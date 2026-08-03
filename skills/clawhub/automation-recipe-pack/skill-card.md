## Description: <br>
Provides automation recipes for file processing, data conversion, batch operations, and workflow orchestration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, teams, and automation-focused users can use this skill to draft and run automation workflows for repeated file, data, scheduling, and pipeline tasks. It is not suited to tasks that require human creative or aesthetic judgment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad read, write, and command execution authority while covering deletion, synchronization, API use, scheduled tasks, and shell command recipes. <br>
Mitigation: Use it only for clearly named low-risk directories and files, preview changes, and require explicit confirmation before rename, delete, sync, API call, scheduled task, or command execution. <br>
Risk: The artifact describes sandboxed command execution, but server security evidence warns that this claim should not be relied on by itself. <br>
Mitigation: Depend on independently enforced sandboxing and permission controls in the agent runtime before allowing filesystem writes or command execution. <br>
Risk: Automated file and data transformations can produce incorrect, destructive, or misleading outputs if inputs, rules, or paths are wrong. <br>
Mitigation: Review generated commands and outputs, back up important files, validate paths and formats, and inspect logs or summaries after execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/automation-recipe-pack) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, code snippets, shell commands, JSON-like result summaries, and generated files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or perform filesystem changes, command execution, API calls, scheduled tasks, and directory synchronization depending on the agent runtime permissions.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
