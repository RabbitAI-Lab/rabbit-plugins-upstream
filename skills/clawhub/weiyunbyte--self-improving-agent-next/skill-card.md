## Description:

Records errors, corrections, capability gaps, and best practices so agents can reuse learnings across future work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weiyunbyte](https://clawhub.ai/user/weiyunbyte)

### License/Terms of Use:


## Use Case:

Developers and agent operators use this skill to capture command failures, user corrections, external API or tool errors, missing capabilities, and reusable practices in workspace learning files for later review. The skill also provides optional hook setup guidance for reminding agents to review and record learnings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent learning files can capture sensitive conversation, command, or error details.

Mitigation: Keep the skill project-scoped where possible and redact tokens, credentials, private paths, customer data, request bodies, and full stack traces before writing learnings.

Risk: Promoting repeated learnings into long-term agent files can affect future sessions.

Mitigation: Treat promotion into AGENTS.md, SOUL.md, TOOLS.md, or MEMORY.md as a manual review step by a trusted operator.

Risk: Optional hooks can inject reminders into future agent sessions.

Mitigation: Enable hooks explicitly, prefer project-level configuration over global hooks, and review hook behavior before deployment.

## Reference(s):

- [Hook Setup Guide](artifact/references/hooks-setup.md)
- [OpenClaw Integration](artifact/references/openclaw-integration.md)
- [Entry Examples](artifact/references/examples.md)
- [Learnings Template](artifact/assets/LEARNINGS.md)
- [Skill Template](artifact/assets/SKILL-TEMPLATE.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code blocks, shell commands, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update workspace .learnings/ files and suggest manual promotion to AGENTS.md, SOUL.md, TOOLS.md, or MEMORY.md.]

## Skill Version(s):

2.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
