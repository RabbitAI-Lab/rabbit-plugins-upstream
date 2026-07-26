## Description: <br>
MindVault helps agents archive conversations, extract memory rules, create project snapshots, and apply the DRAS-V thinking protocol. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhouxin121](https://clawhub.ai/user/zhouxin121) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users can use this skill to preserve local conversation history, extract reusable memory rules, restore project context, and trigger a structured DRAS-V reasoning flow during agent work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Conversation archives and operational metadata can retain sensitive chats, credentials, private third-party content, or sensitive file paths. <br>
Mitigation: Avoid archiving secrets or private content, protect the archive directory, and review generated JSONL, memory notes, and project snapshots before sharing or reusing them. <br>
Risk: The security review notes uncertainty around local-only storage, Coze cloud use, and paid automation data destinations. <br>
Mitigation: Use local modes by default and confirm data destinations, retention, and any report-sending behavior before enabling Coze or paid automation workflows. <br>


## Reference(s): <br>
- [Mindvault on ClawHub](https://clawhub.ai/zhouxin121/skills/mindvault) <br>
- [Additional MindVault usage guide](https://pay.ldxp.cn/item/p0r2lb) <br>
- [Elite Longterm Memory](https://clawhub.ai/nextfrontierbuilds/elite-longterm-memory) <br>
- [Memory Tiering](https://clawhub.ai/sarielwang93/memory-tiering) <br>
- [Fluid Memory](https://clawhub.ai/againta/fluid-memory) <br>
- [Memory Qdrant](https://clawhub.ai/zuiho-kai/memory-qdrant) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, JSONL archives, Markdown snapshots, and shell commands for bundled Python scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local archive files, memory notes, and project snapshot documents when the agent follows the skill instructions.] <br>

## Skill Version(s): <br>
1.0.3 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
