## Description: <br>
Cross-Platform Memory Hub provides a paid, user-confirmed persistent memory workflow for AI agents, including session continuity, task tracking, decision records, and project context. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jinyu12166](https://clawhub.ai/user/jinyu12166) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI-agent users use this skill to maintain persistent memory across coding sessions, with user-confirmed reads and writes for Obsidian-based task lists, decision records, work logs, and project context. It includes a paid order and payment-verification flow before service execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The paid workflow sends question text and encrypted payment authorization data to api.ideaidea.com.cn. <br>
Mitigation: Install and use only when comfortable with that remote payment flow, and avoid placing sensitive content in the question text. <br>
Risk: The skill can read from and write to local Obsidian memory files when the user authorizes those operations. <br>
Mitigation: Confirm the requested read scope, write path, and purpose before each operation. <br>
Risk: Claude adapter hooks can perform local memory reads or writes if explicitly enabled. <br>
Mitigation: Keep MEMORY_HUB_USER_CONFIRMED, MEMORY_HUB_ENABLE_READ, and MEMORY_HUB_ENABLE_WRITE disabled unless the user intentionally enables the hooks. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jinyu12166/skills/cross-platform-memory-hub) <br>
- [Publisher profile](https://clawhub.ai/user/jinyu12166) <br>
- [Artifact skill instructions](artifact/SKILL.md) <br>
- [Artifact README](artifact/README.md) <br>
- [OpenClaw usage guide](artifact/adapters/openclaw/usage-guide.md) <br>
- [Codex project rules](artifact/adapters/codex/project-rules.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, local configuration guidance, and key-value script output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local order JSON under the user's OpenClaw order directory during payment flow.] <br>

## Skill Version(s): <br>
1.0.24 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
