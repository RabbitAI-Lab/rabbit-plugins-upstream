## Description: <br>
自研三层记忆恢复系统。解决session重启后"忘记一切"的问题，提供永久记忆、今日记忆、临时记忆的完整架构。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[daoistbro](https://clawhub.ai/user/daoistbro) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to recover local work context after session restarts by reading permanent, daily, and session memory files. It supports continuity workflows where memory is intentionally stored and reviewed in local Markdown files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Intentional local memory retention can preserve personal or work context and shape future agent behavior. <br>
Mitigation: Review memory files periodically, keep secrets and highly private details out of them, and delete or edit entries that should not be reused later. <br>
Risk: The recovery script prints local memory file contents into the active session. <br>
Mitigation: Run it only in trusted workspaces and inspect the memory directory before use when sensitive context may be present. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with bash command snippets and local shell output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads local memory files when the recovery script is run; no API credentials were detected in the release evidence.] <br>

## Skill Version(s): <br>
1.0.0 (source: package.json and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
