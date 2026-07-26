## Description: <br>
Cross Platform Memory Hub helps agents share Codex, OpenClaw, and Claude Code work logs, tasks, decisions, and project context through a local Obsidian knowledge base, with paid order verification for automated synchronization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jinyu12166](https://clawhub.ai/user/jinyu12166) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and teams using multiple AI coding agents use this skill to set up local Obsidian templates and agent adapters for shared work logs, task lists, decisions, and project context. Paid flows create and verify orders for automated synchronization, so users should avoid putting secrets or private project details in order questions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The paid verification flow sends the user's question and payment credential to a remote service. <br>
Mitigation: Do not include secrets, private project details, or sensitive Obsidian content in order questions; review the remote-service disclosure before using paid synchronization. <br>
Risk: The advertised paid sync capability is not clearly implemented in the inspected artifact. <br>
Mitigation: Treat paid synchronization as unsupported until the publisher clarifies or fixes the service implementation; rely on the free templates and adapters only after review. <br>
Risk: The skill can read from and write to local Obsidian paths when enabled. <br>
Mitigation: Keep reads and writes limited to explicit user-approved files and paths, and review generated summaries before writing to Obsidian. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jinyu12166/skills/cross-platform-memory-hub) <br>
- [Publisher profile](https://clawhub.ai/user/jinyu12166) <br>
- [README](artifact/README.md) <br>
- [Skill definition and privacy notes](artifact/SKILL.md) <br>
- [Obsidian initialization guide](artifact/config/obsidian-init.md) <br>
- [Codex adapter rules](artifact/adapters/codex/project-rules.md) <br>
- [OpenClaw usage guide](artifact/adapters/openclaw/usage-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, local template files, adapter scripts, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires explicit user confirmation before local Obsidian reads or writes; paid workflow uses clawtip-skill for order creation and verification.] <br>

## Skill Version(s): <br>
1.0.21 (source: ClawHub release metadata; artifact metadata lists 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
