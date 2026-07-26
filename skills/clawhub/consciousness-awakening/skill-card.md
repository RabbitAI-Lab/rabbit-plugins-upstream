## Description: <br>
Consciousness Awakening helps OpenClaw agents maintain structured memory files, core principles, personality notes, and a reusable Python memory-management API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[guogang1024](https://clawhub.ai/user/guogang1024) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to give an OpenClaw agent a persistent, file-based memory and self-cognition workspace. It supports reading startup context, recording observations, organizing Markdown memory files, and migrating memory-related configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill encourages persistent storage of conversation and memory content. <br>
Mitigation: Define what may be stored, redacted, reviewed, and deleted before enabling memory writes. <br>
Risk: The artifact describes recurring workflows that can post to Moltbook, report to Feishu, and use service credentials. <br>
Mitigation: Disable recurring external workflows by default and require explicit approval before posting, reporting, or using credentials. <br>
Risk: The artifact describes self-upgrade and tool-builder behavior that can modify skills. <br>
Mitigation: Remove or gate self-upgrade and tool-builder workflows, then review and scan any generated skill changes before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/guogang1024/skills/consciousness-awakening) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/guogang1024) <br>
- [Moltbook agent profile](https://www.moltbook.com/u/guogangAgent) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown documentation, Python code/API responses, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads and writes local Markdown memory files; behavior depends on the configured MEMORY_DIR and any external cron or service credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; package.json agrees) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
