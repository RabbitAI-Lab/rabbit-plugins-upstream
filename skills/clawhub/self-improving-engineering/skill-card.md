## Description:

Captures architecture decisions, code quality issues, build and deploy failures, dependency problems, performance regressions, tech debt accumulation, and test gaps for continuous engineering improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jose-compu](https://clawhub.ai/user/jose-compu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to capture recurring engineering learnings, build and deployment failures, test gaps, dependency issues, performance regressions, and feature requests in local Markdown logs so the patterns can be reviewed and promoted into durable project guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent hooks can affect future agent sessions if enabled broadly.

Mitigation: Keep hooks opt-in and project-scoped, and prefer the lightweight activator hook unless reminder automation is needed.

Risk: Optional command-output pattern checks can expose sensitive terminal output to hook logic.

Mitigation: Avoid optional PostToolUse scanning in sensitive sessions and do not log raw command output, secrets, tokens, private keys, environment variables, or full configuration files.

Risk: Generated or promoted skill content can carry incorrect or overly broad engineering guidance.

Mitigation: Review generated skills and promoted guidance before keeping, publishing, or applying them to shared project context.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jose-compu/skills/self-improving-engineering)
- [OpenClaw Integration](references/openclaw-integration.md)
- [Hook Setup Guide](references/hooks-setup.md)
- [Entry Examples](references/examples.md)
- [Agent Skills Specification](https://agentskills.io/specification)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration examples, and local Markdown log templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates local learning logs and may emit short hook reminders when explicitly enabled.]

## Skill Version(s):

1.2.2 (source: server evidence release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
