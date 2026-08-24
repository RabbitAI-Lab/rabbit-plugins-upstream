## Description:

Keelwright gives AI coding agents machine-enforced safety gates, an autonomy dial, self-healing loop controls, and plain-language reporting for users who ship AI-generated code they cannot review line by line.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ratingtesting](https://clawhub.ai/user/ratingtesting)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, builders, and product operators use Keelwright to supervise AI coding sessions with automated security checks, loop controls, approval modes, and plain-language status reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review found broad autonomous coding, persistence, production, and self-modification authority with inconsistent consent language.

Mitigation: Use Checkpoint or Copilot mode for real projects and require fresh approval before production deploys, rollbacks, package installs, or skill and memory changes.

Risk: Automatic tracking or scheduled behavior can persist project memory or activity beyond a single prompt.

Mitigation: Disable or ignore automatic tracking and cron behavior unless persistent memory is explicitly desired.

Risk: The release is suspicious rather than clearly benign according to the authoritative security verdict.

Mitigation: Install only when broad autonomous coding powers are acceptable for the target project and review generated actions before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ratingtesting/skills/keelwright)
- [Publisher profile](https://clawhub.ai/user/ratingtesting)
- [Clawdis author link](https://github.com/ratingtesting)
- [README](README.md)
- [Security gates](references/security-gates.md)
- [Web guard](references/web-guard.md)
- [R3 review protocol](references/r3-review-protocol.md)
- [QA results](references/qa-results-20260721.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code, shell commands, templates, and plain-language reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local tracking files only after user consent or explicit instruction.]

## Skill Version(s):

1.7.0 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
