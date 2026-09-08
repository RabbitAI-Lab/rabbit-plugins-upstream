## Description:

Keelwright wraps AI coding agents with safety gates, autonomy controls, circuit breakers, and plain-language reporting for people shipping AI-generated code they cannot review line by line.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ratingtesting](https://clawhub.ai/user/ratingtesting)

### License/Terms of Use:

MIT-0

## Use Case:

External builders, non-developer founders, and developers use keelwright during AI coding sessions to enforce checks for common security, correctness, supply-chain, and runaway-loop failures before committing or shipping generated code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill combines broad project file writes, shell execution, network checks, persistence, and autonomous coding authority.

Mitigation: Use Copilot or Checkpoint mode for sensitive projects, start in a disposable worktree, and require confirmation before commits, pushes, installs, model downloads, cron jobs, memory writes, or production-affecting actions.

Risk: First-load or bootstrap behavior may create files or initiate downloads if treated too permissively.

Mitigation: Do not allow bootstrap file creation, optional tooling installation, or downloads unless the operator explicitly requests them.

Risk: The security verdict flags conflicting consent and load-time behavior for review.

Mitigation: Review the skill before deployment and keep high-risk actions behind explicit human approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ratingtesting/skills/keelwright)
- [Publisher profile](https://clawhub.ai/user/ratingtesting)
- [Author profile](https://github.com/ratingtesting)
- [Architecture decision record](docs/ADR-001-layered-skill.md)
- [Security gates reference](references/security-gates.md)
- [QA results](qa-results/README.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and file-path references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce on-disk verification evidence and plain-language risk reports when the agent follows the skill.]

## Skill Version(s):

1.11.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
