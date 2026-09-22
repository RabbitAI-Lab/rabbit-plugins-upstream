## Description:

Set up, inspect, or maintain a local user-preference memory shared across coding agents such as Codex and Claude Code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cutd](https://clawhub.ai/user/cutd)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding-agent users use Dongwo to configure, inspect, and maintain an opt-in local preference memory shared across agents. It is intended for explicit memory setup, review, trust, forgetting, and lifecycle-hook maintenance workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected preference-like prompts are persisted locally after hooks are enabled.

Mitigation: Enable hooks only with explicit user consent, review .dongwo/memory/inbox/ regularly, and delete unwanted evidence before rebuilding memory.

Risk: Confidential projects may retain local preference evidence even with filtering and redaction.

Mitigation: Avoid enabling Dongwo in highly confidential projects unless local retention is acceptable and the inbox is regularly reviewed and cleaned.

Risk: Prompt-derived memory may be stale, untrusted, or lower priority than current instructions.

Mitigation: Treat current user requests and project instructions as higher priority, inject only trusted profile data and active preferences, and keep pending or conflicted entries out of agent context.

## Reference(s):

- [Dongwo memory policy](references/memory-policy.md)
- [ClawHub skill page](https://clawhub.ai/cutd/skills/dongwo)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local file paths, lifecycle-hook snippets, and memory-maintenance commands; does not require network access.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
