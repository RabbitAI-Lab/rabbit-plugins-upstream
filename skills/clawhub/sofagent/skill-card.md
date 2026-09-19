## Description:

FDE Skill helps front-line deployment engineers operationalize enterprise AI by constraining agent behavior, auditing changes, and preserving deployment knowledge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kongfangxun](https://clawhub.ai/user/kongfangxun)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, deployment engineers, and enterprise IT teams use this skill to structure front-line AI deployment work: intake, business-flow discovery, AI-node identification, knowledge capture, delivery, audit, and ongoing optimization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill describes a broad persistent enterprise agent platform with high-impact tools, data flows, and configuration changes.

Mitigation: Install only in a controlled enterprise deployment after reviewing install.sh, the MCP server implementation, and the exact configuration files that will be modified.

Risk: MCP roles and tools can create a wide operational surface if enabled broadly.

Mitigation: Restrict MCP roles and tools to the minimum needed for the deployment, and disable unneeded cloud, device, browser, connector, and daemon features.

Risk: Sensitive systems can be exposed if credentials, retention, redaction, offline mode, or rollback behavior are not verified before use.

Mitigation: Avoid broad credentials and verify data retention, redaction, offline mode, and rollback behavior before using the skill on sensitive systems.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/kongfangxun/skills/sofagent)
- [Root Skill Definition](artifact/SKILL.md)
- [Agent Library](artifact/AGENTS.md)
- [FDE Harness Subagent](artifact/agents/fde/SKILL.md)
- [Installer Workflow](artifact/harness/installer.md)
- [FDE Stage Guides](artifact/skills/01-entry.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce staged checklists, audit prompts, deployment verification steps, rollback guidance, and enterprise skill handoff material.]

## Skill Version(s):

1.4.9 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
