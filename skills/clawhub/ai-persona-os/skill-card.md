## Description: <br>
AI Persona OS helps OpenClaw agents set up and maintain a persistent persona workspace with memory files, operating rules, setup flows, heartbeat routines, proactive patterns, and security guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jeffjhunter](https://clawhub.ai/user/jeffjhunter) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and external OpenClaw users use this skill to configure an agent persona workspace, create or select persona files, maintain memory and heartbeat routines, and apply repeatable operating practices. It is intended for normal ClawHub skill use where the user reviews workspace, cron, and OpenClaw configuration changes before approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent workspace memory can store and index personal or work context. <br>
Mitigation: Review USER.md, MEMORY.md, DREAMS.md, daily logs, and generated persona files; avoid saving secrets or sensitive personal data. <br>
Risk: Heartbeat, cron, memory maintenance, pruning, and archiving can create or modify workspace files automatically. <br>
Mitigation: Keep proactive maintenance and cron routines opt-in, and review proposed file changes before approving them. <br>
Risk: The skill can inspect or propose changes to OpenClaw configuration for routing and workspace behavior. <br>
Mitigation: Approve only expected OpenClaw config changes and verify that credential values are not displayed, copied, or modified. <br>


## Reference(s): <br>
- [ClawHub Skill Listing](https://clawhub.ai/jeffjhunter/skills/ai-persona-os) <br>
- [AI Persona OS Homepage](https://os.aipersonamethod.com) <br>
- [heartbeat-automation.md](references/heartbeat-automation.md) <br>
- [never-forget-protocol.md](references/never-forget-protocol.md) <br>
- [proactive-playbook.md](references/proactive-playbook.md) <br>
- [security-patterns.md](references/security-patterns.md) <br>
- [soul-md-maker.md](references/soul-md-maker.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Files, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and workspace file templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose persistent workspace files, optional cron routines, and OpenClaw configuration changes that should be reviewed before approval.] <br>

## Skill Version(s): <br>
2.0.0 (source: frontmatter, _meta.json, CHANGELOG, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
