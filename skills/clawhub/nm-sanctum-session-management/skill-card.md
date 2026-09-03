## Description:

Manages Claude Code sessions with naming, checkpointing, and resume strategies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to name, resume, and organize long-running Claude Code work across debugging, feature development, PR review, and investigation sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Session names, summaries, work logs, and resumed agent settings may carry context forward between sessions.

Mitigation: Avoid storing secrets, credentials, or sensitive regulated data in sessions unless the retention behavior is understood and accepted.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-sanctum-session-management)
- [Metadata Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No files, scripts, hooks, or automatic execution are included in the artifact.]

## Skill Version(s):

1.9.19 (source: server release metadata; artifact frontmatter says 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
