## Description:

SKILL is a Field Deployment Engineer methodology skill for enterprise AI rollout that constrains agent behavior, audits changes, and preserves deployment knowledge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kongfangxun](https://clawhub.ai/user/kongfangxun)

### License/Terms of Use:

MIT-0

## Use Case:

Frontline deployment engineers and enterprise AI teams use this skill to assess business workflows, identify AI deployment nodes, quantify value, and deliver governed enterprise-specific skills and operating guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is intended for high-trust enterprise deployment and administration workflows.

Mitigation: Install it only in environments where that role is intended, and review the installer and changed MCP configuration files before enabling it.

Risk: Broad MCP capabilities can affect auditing, automation, training, browser actions, model switching, and restore operations.

Mitigation: Restrict MCP roles to the minimum tools needed and keep human confirmation enabled for destructive or high-impact operations.

Risk: Persistent local task logs, knowledge files, and deployment records can retain sensitive enterprise information.

Mitigation: Define retention and redaction rules before use, and avoid storing secrets or sensitive personal data in skill-managed knowledge files.

Risk: Background daemon, webhook, browser, training, snapshot-restore, and USB-key behavior can expand the operational attack surface.

Mitigation: Disable those features unless explicitly required, and review their schedules, endpoints, permissions, and recovery paths before activation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kongfangxun/skills/sofagent)
- [Publisher profile](https://clawhub.ai/user/kongfangxun)
- [Skill entrypoint](artifact/SKILL.md)
- [Agent and MCP reference](artifact/AGENTS.md)
- [Delivery workflow](artifact/skills/04-deliver.md)
- [Exit and continuous improvement workflow](artifact/skills/05-exit.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration snippets, and structured checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local enterprise knowledge, audit reports, MCP tools, and deployment state when configured.]

## Skill Version(s):

1.4.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
