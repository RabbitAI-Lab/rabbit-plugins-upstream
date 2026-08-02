## Description: <br>
Cross-platform persistent memory system for AI agents: session continuity, task tracking, decision records, and project context across coding sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jinyu12166](https://clawhub.ai/user/jinyu12166) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to configure a cross-platform memory workflow for Obsidian-backed notes, task lists, decision records, and session summaries across OpenClaw, Codex, and Claude Code. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and write approved local memory files. <br>
Mitigation: Confirm the requested read or write scope before use, keep adapter read/write environment toggles disabled until consent, and avoid storing secrets in memory notes. <br>
Risk: The paid workflow uses clawtip order details and CLAWTIP_* environment variables. <br>
Mitigation: Review the payment amount and order details before authorizing clawtip, and set CLAWTIP_* variables only for the intended payment workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jinyu12166/skills/cross-platform-memory-hub) <br>
- [README](artifact/README.md) <br>
- [OpenClaw usage guide](artifact/adapters/openclaw/usage-guide.md) <br>
- [Obsidian initialization guide](artifact/config/obsidian-init.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with inline shell commands and JSON-like command outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces user-confirmed local memory configuration guidance, template content, order details, payment status, and service authorization messages.] <br>

## Skill Version(s): <br>
1.0.25 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
