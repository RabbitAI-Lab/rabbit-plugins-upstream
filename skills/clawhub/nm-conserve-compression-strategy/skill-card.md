## Description:

Recommends context compression strategies for bloated or quota-heavy sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to analyze context pressure, choose an appropriate compression or delegation strategy, and preserve useful session state before reducing context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved session-state or context archive files may contain sensitive conversation details from the active session.

Mitigation: Review and prune saved context files before retaining or sharing them, especially when the session included secrets or sensitive data.

Risk: Suggested cleanup commands or delegation steps could change a workflow if applied without review.

Mitigation: Review recommended commands and agent handoffs before execution; the skill itself is documentation-only and does not automatically run commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-conserve-compression-strategy)
- [Project Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/conserve)
- [Log Debugging Hygiene Module](artifact/modules/log-debugging-hygiene.md)
- [Drain3](https://github.com/logpai/Drain3)
- [logs-tokenizer](https://github.com/sergeivaskov/logs-tokenizer)
- [LLMLingua](https://github.com/microsoft/LLMLingua)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with inline command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only guidance; it does not automatically run commands.]

## Skill Version(s):

1.9.19 (source: server release metadata; artifact frontmatter reports 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
