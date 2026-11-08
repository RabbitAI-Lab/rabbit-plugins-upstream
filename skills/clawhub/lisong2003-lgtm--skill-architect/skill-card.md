## Description:

Audits and restructures oversized SKILL.md files by externalizing content, building routing indexes, validating changes, and supporting rollback and conversation handoffs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC BY-NC-SA 4.0

## Use Case:

Developers and agent authors use this skill to audit and restructure large SKILL.md files, create routing and skill-pack materials, validate changes, and roll back from backups. They can also create and transfer summaries of long conversations for continued work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic saved-conversation discovery may select conversation material beyond the user’s intended scope.

Mitigation: Review discovered files and confirm the intended conversation scope before importing or summarizing them.

Risk: Conversation-derived summaries shared without a privacy review may expose sensitive information.

Mitigation: Review and redact summaries for private information before exporting or sharing them.

Risk: The security assessment reports a data-loss issue during extraction.

Mitigation: Create and verify a backup, then inspect extracted output before relying on the modified skill.

## Reference(s):

- [Long conversation summarization practices](references/长对话归纳最佳实践.md)
- [Cross-user transfer practices](references/跨用户传输最佳实践.md)
- [Routing priorities and troubleshooting](references/触发优先级与故障排查.md)
- [Skill slimming practices](references/瘦身最佳实践.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration files]

**Output Format:** [Markdown, JSON, and command-line instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on the selected audit, restructuring, validation, rollback, or conversation handoff task.]

## Skill Version(s):

0.3.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
