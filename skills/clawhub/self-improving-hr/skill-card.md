## Description:

Captures policy gaps, compliance risks, recruiting process issues, onboarding friction, retention signals, candidate experience problems, and offboarding gaps to enable continuous HR improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jose-compu](https://clawhub.ai/user/jose-compu)

### License/Terms of Use:

MIT-0

## Use Case:

HR teams and agents use this skill to capture anonymized HR process learnings, compliance risks, recruiting and onboarding friction, retention signals, and improvement requests. It helps convert recurring patterns into reviewed policy documents, checklists, compliance calendars, interview scorecards, or reusable HR skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HR learning logs can involve sensitive employee or candidate context.

Mitigation: Keep .learnings local and untracked, anonymize examples, and do not log names, government identifiers, salary details, medical information, or other PII.

Risk: Optional hooks can persist reminders across sessions and may inspect command output when PostToolUse is enabled.

Mitigation: Install hooks only in workspaces where HR process logging is intended, keep them project-scoped, prefer the minimal prompt reminder hook, and avoid PostToolUse unless output inspection is needed.

Risk: Promoting local observations into policies, agent instructions, hooks, memory, or generated skills can make unreviewed HR guidance durable.

Mitigation: Require explicit review and approval before any promotion into permanent HR materials or agent behavior.

## Reference(s):

- [OpenClaw Integration](references/openclaw-integration.md)
- [Hook Setup Guide](references/hooks-setup.md)
- [Entry Examples](references/examples.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local learning-log entries and optional reminder hook output; no external service output is required.]

## Skill Version(s):

1.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
