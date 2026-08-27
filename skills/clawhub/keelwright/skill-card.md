## Description:

Keelwright helps agents run autonomous coding sessions with machine-enforced safety gates, autonomy controls, self-healing loop guidance, and plain-language reports for operators who cannot review every line of generated code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ratingtesting](https://clawhub.ai/user/ratingtesting)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, product builders, non-developer founders, and agent operators use keelwright to add safety gates, circuit breakers, approval checkpoints, and plain-language reporting to loop-coding or autonomous coding sessions. It is intended for use before agent coding runs, autonomous tasks, or commits where the operator wants additional verification and control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide autonomous coding behavior that writes files, runs shell commands, uses the network, creates commits, and keeps local state.

Mitigation: Install only in repositories where those actions are acceptable, keep work revertible, and use Copilot or Checkpoint mode for auth, payments, databases, production, or any repository you cannot safely roll back.

Risk: The security evidence reports conflicting persistence rules and broad memory, install, update-check, attack-logging, promotional prompt, and self-improvement behavior.

Mitigation: Before using Autopilot, explicitly decide which tracking files, network checks, logs, tool installs, prompts, and recurring self-improvement actions are allowed.

Risk: The authoritative security verdict is suspicious and says the release needs review before installation.

Mitigation: Review the artifact and its security guidance before deployment, then limit the skill to a lower-autonomy mode until its local behavior is understood.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ratingtesting/skills/keelwright)
- [Publisher profile](https://clawhub.ai/user/ratingtesting)
- [Author profile from Clawdis metadata](https://github.com/ratingtesting)
- [README](README.md)
- [Security gates](references/security-gates.md)
- [Web Guard](references/web-guard.md)
- [Circuit breaker](references/circuit-breaker.md)
- [QA results](qa-results/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, code-oriented recommendations, and plain-language status or review reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local evidence, tracking files, attack logs, and session summaries when the operator authorizes those behaviors.]

## Skill Version(s):

1.7.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
