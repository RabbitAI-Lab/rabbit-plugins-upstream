## Description:

keelwright helps agents run safer AI coding sessions by combining an autonomy dial, machine-enforced security gates, circuit breakers, and plain-language reports for users who cannot review every line of generated code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ratingtesting](https://clawhub.ai/user/ratingtesting)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and non-developer builders load keelwright before AI coding sessions, autonomous loops, or commits to make agents run checks for security, dependency, loop-control, and reporting risks before code is shipped.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for broad operational authority, including project file changes and local command execution.

Mitigation: Install it only for operational coding-assistant use, and choose Checkpoint or Copilot unless unattended Autopilot behavior is explicitly desired.

Risk: Autonomous actions such as installs, commits, pushes, deploys, rollback, cron changes, memory updates, or skill patching can have persistent effects.

Mitigation: Require explicit confirmation before those action classes are allowed.

Risk: Persistent tracking files and viral prompt behavior may create unwanted local state or user-facing prompts.

Mitigation: Review or disable those behaviors before use, and allow bootstrap tracking files only after explicit consent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ratingtesting/skills/keelwright)
- [ratingtesting publisher profile](https://clawhub.ai/user/ratingtesting)
- [ratingtesting author profile](https://github.com/ratingtesting)
- [README](README.md)
- [ADR-001 layered skill](docs/ADR-001-layered-skill.md)
- [Security gates](references/security-gates.md)
- [Circuit breaker](references/circuit-breaker.md)
- [QA results](qa-results/README.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and file-backed report templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May instruct agents to create or update local tracking files only after explicit user consent.]

## Skill Version(s):

1.10.8 (source: ClawHub release metadata; artifact frontmatter lists 1.10.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
