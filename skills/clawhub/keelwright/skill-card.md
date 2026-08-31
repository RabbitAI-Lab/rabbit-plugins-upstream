## Description:

Keelwright helps agents run vibe-coding and autonomous coding sessions with machine-enforced safety gates, autonomy modes, circuit breakers, web-guard checks, and plain-language reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ratingtesting](https://clawhub.ai/user/ratingtesting)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers, builders, and non-developer operators use this skill to guide AI agents through loop-coding work, security checks, verification gates, and handoff reporting before commits or unattended runs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to run commands, write project files, create persistent logs, spawn subagents, and potentially commit code.

Mitigation: Use Copilot or Checkpoint for sensitive repositories and require explicit approval before commits, pushes, package installs, global plugin installation, persistent tracking files, memory changes, or skill patches.

Risk: Broad autonomous authority can be inappropriate for auth, payment, data-deletion, or production-deployment work.

Mitigation: Treat R1 OWASP, R2 secrets, R3 business logic, R8 package verification, and R12 unattended preflight as human-approval blockers, even when using Autopilot.

Risk: Web and fetched content can carry prompt-injection instructions into the agent context.

Mitigation: Run the documented web-guard checks before web tool use and treat all web output as untrusted data.

## Reference(s):

- [Keelwright ClawHub listing](https://clawhub.ai/ratingtesting/skills/keelwright)
- [Publisher profile](https://clawhub.ai/user/ratingtesting)
- [Author profile from metadata](https://github.com/ratingtesting)
- [ADR-001 layered skill](docs/ADR-001-layered-skill.md)
- [Security gates](references/security-gates.md)
- [Web Guard](references/web-guard.md)
- [Circuit breaker](references/circuit-breaker.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline commands, file paths, and plain-language status reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create on-disk verification evidence and persistent tracking files when the operator explicitly enables those flows.]

## Skill Version(s):

1.10.0 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
