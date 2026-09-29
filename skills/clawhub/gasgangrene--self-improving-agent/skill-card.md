## Description:

Captures learnings, errors, feature requests, and corrections in workspace files so OpenClaw agents can reuse validated lessons across sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gasgangrene](https://clawhub.ai/user/gasgangrene)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill to record command failures, user corrections, knowledge gaps, and feature requests as structured markdown entries. It also supports optional session-start reminders and session-end error sweep triage for workspaces that intentionally enable the hook.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Conversation-derived content can persist into .learnings files and later influence workspace guidance if promoted.

Mitigation: Review entries before promotion, require explicit approval before writing to SOUL.md, TOOLS.md, or AGENTS.md, and keep .learnings out of version control unless intentionally shared.

Risk: The optional OpenClaw hook can automatically influence later sessions by injecting reminders and pending-triage notes.

Mitigation: Install and enable the hook only in workspaces where durable self-improvement behavior is intended; disable the hook or remove .learnings to stop the session-end sweep.

Risk: Session-end error sweep excerpts may still contain sensitive context despite best-effort truncation and redaction.

Mitigation: Avoid enabling the hook in sensitive workspaces until transcript containment and retention controls are reviewed, and prefer sanitized summaries over raw transcripts or full command output.

## Reference(s):

- [OpenClaw Integration](references/openclaw-integration.md)
- [Entry Examples](references/examples.md)
- [Uninstall Guide](references/uninstall.md)
- [Changelog](CHANGELOG.md)
- [ClawHub Skill Page](https://clawhub.ai/gasgangrene/skills/self-improving-agent)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands and structured markdown file templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May append or initialize .learnings markdown files when the workspace intentionally uses the skill; optional OpenClaw hook can inject reminders and append triage entries from session-end sweeps.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 4.0.0 and artifact _meta.json reports 4.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
