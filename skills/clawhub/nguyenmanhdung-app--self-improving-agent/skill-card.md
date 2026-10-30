## Description:

Captures learnings, errors, feature requests, and corrections so coding agents can maintain structured improvement notes and promote durable guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nguyenmanhdung-app](https://clawhub.ai/user/nguyenmanhdung-app)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI coding-agent users use this skill to log operational failures, user corrections, knowledge gaps, and feature requests into structured local Markdown files. It supports later review and optional promotion of broadly useful learnings into project or workspace agent guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist learned content into future agent instructions.

Mitigation: Review proposed changes before promoting entries into CLAUDE.md, AGENTS.md, SOUL.md, TOOLS.md, or copilot instructions.

Risk: Broad always-on hooks can add reminders or inspect command outcomes more often than intended.

Mitigation: Prefer project-local setup, use constrained hook matchers, start with activator-only hooks, and review hook scripts before enabling them.

Risk: Learning entries may accidentally capture sensitive details from errors, transcripts, environment values, or configuration.

Mitigation: Record short sanitized summaries, redact secrets, and avoid storing raw transcripts or full command output unless explicitly required.

## Reference(s):

- [Self Improving Agent on ClawHub](https://clawhub.ai/nguyenmanhdung-app/skills/self-improving-agent)
- [OpenClaw Integration](references/openclaw-integration.md)
- [Hook Setup Guide](references/hooks-setup.md)
- [Examples](references/examples.md)
- [Agent Skills Specification](https://agentskills.io/specification)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates structured .learnings Markdown files; optional hooks can emit learning and error reminders.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
