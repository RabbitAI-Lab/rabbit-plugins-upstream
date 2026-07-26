## Description: <br>
Captures learnings, errors, and corrections to enable continuous improvement. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[txmerlxn](https://clawhub.ai/user/txmerlxn) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and coding-agent users use this skill to capture corrections, command failures, feature requests, knowledge gaps, and reusable lessons in project learning files. The skill also guides review and promotion of durable learnings into agent or project instruction files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persist conversation, command, and tool details into learning files. <br>
Mitigation: Use it only in trusted workspaces and redact secrets, personal data, raw transcripts, command outputs, tokens, and environment details before logging or sharing entries. <br>
Risk: Promoted learnings may change future-agent instruction files such as CLAUDE.md, AGENTS.md, Copilot instructions, SOUL.md, or TOOLS.md. <br>
Mitigation: Require explicit review and approval before promoting learnings into instruction files or extracting them into new skills. <br>
Risk: Global or always-on hooks may capture more context than intended across projects. <br>
Mitigation: Prefer project-level opt-in setup, keep hooks minimal, and avoid global always-on hooks unless the workspace policy allows them. <br>


## Reference(s): <br>
- [Hook Setup Guide](references/hooks-setup.md) <br>
- [Clawdbot Integration Guide](references/clawdbot-integration.md) <br>
- [Entry Examples](references/examples.md) <br>
- [Agent Skills Specification](https://agentskills.io/specification) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance, Code] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update persistent learning files and may scaffold reusable skill files when explicitly run.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
