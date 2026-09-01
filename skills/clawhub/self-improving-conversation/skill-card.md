## Description:

Captures redacted dialogue learnings, tone mismatches, escalation failures, and conversation quality issues in local .learnings/ files, with optional project-scoped reminder hooks and human-reviewed promotion guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jose-compu](https://clawhub.ai/user/jose-compu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and conversational-agent operators use this skill to record dialogue failures, tone mismatches, hallucinations, escalation gaps, context loss, and requested conversation capabilities as local markdown learnings. They can later review recurring patterns and promote proven guidance into agent prompt or workspace files only after a human-reviewed diff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Learning files may contain sensitive conversation excerpts or personal data.

Mitigation: Keep .learnings/ local or gitignored unless entries are reviewed, and redact names, account data, secrets, regulated content, and raw transcripts before anything is stored or promoted.

Risk: Optional hooks can persist across sessions and may add reminders more broadly than intended if configured too widely.

Mitigation: Keep hooks opt-in, project-scoped, and narrowly matched; avoid global or user-level hook installation unless it has been explicitly reviewed.

Risk: Promoting captured patterns into prompt or workspace files can introduce incorrect or misleading conversation guidance.

Mitigation: Promote only proven patterns after explicit human review of a diff.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jose-compu/skills/self-improving-conversation)
- [OpenClaw Integration](references/openclaw-integration.md)
- [Hook Setup Guide](references/hooks-setup.md)
- [Entry Examples](references/examples.md)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown entries with inline shell commands and JSON hook snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates local .learnings/ files and proposes reviewed diffs for promotion; optional hooks emit reminder text.]

## Skill Version(s):

1.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
