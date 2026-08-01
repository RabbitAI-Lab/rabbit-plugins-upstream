## Description: <br>
Local Python orchestration skill for multi-agent workflows using a shared blackboard file, permission gating, token budget scripts, and persistent project context. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jovancoding](https://clawhub.ai/user/jovancoding) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to coordinate local multi-agent work, share task state through a project blackboard, manage persistent project context, and gate sensitive local operations with advisory permission checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local blackboard, audit, grant, and context files can retain task data, justifications, and advisory tokens. <br>
Mitigation: Use the skill only in trusted workspaces, restrict access to the data directory, and periodically clear or rotate stored state. <br>
Risk: Permission grant tokens are advisory hints and do not authenticate the caller identity. <br>
Mitigation: Require separate platform authentication and human approval before using any grant result for real database, payment, email, or file export access. <br>
Risk: Free-text justifications and project context can contain sensitive information if operators provide it. <br>
Mitigation: Do not enter secrets, credentials, or PII in justifications, blackboard entries, or project context. <br>


## Reference(s): <br>
- [Network-AI homepage](https://network-ai.org) <br>
- [ClawHub skill page](https://clawhub.ai/jovancoding/skills/network-ai) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/jovancoding) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON outputs from local scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local-only state files may be created or updated under the project data directory and shared blackboard.] <br>

## Skill Version(s): <br>
5.15.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
