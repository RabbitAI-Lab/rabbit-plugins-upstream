## Description:

Keelwright gives AI coding agents an autonomy-controlled loop with machine-enforced security, verification, web-guard, circuit-breaker, and plain-language reporting for users who cannot review every generated line.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ratingtesting](https://clawhub.ai/user/ratingtesting)

### License/Terms of Use:

MIT-0

## Use Case:

External builders, non-developer founders, loop-coders, and developers use Keelwright to guide AI coding sessions through security gates, autonomy approvals, loop limits, verification evidence, and plain-language status reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide file writes, commits, installs, memory persistence, and production actions.

Mitigation: Start in Checkpoint or Copilot mode and require explicit review before commits, pushes, deploys, rollbacks, or skill and memory patches.

Risk: Project-root tracking files and persistence behavior may be created when enabled.

Mitigation: Decline or disable L4 persistence unless project-local memory files are wanted, and keep those files out of commits.

Risk: Running checks on untrusted ZIPs can expose the agent environment to unsafe content.

Mitigation: Do not use --run-checks on untrusted ZIPs; inspect or isolate unfamiliar artifacts before running bundled scripts.

Risk: Global installs in autonomous QA flows can affect the operator environment.

Mitigation: Avoid global installs in QA prompts and prefer isolated, project-local environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ratingtesting/skills/keelwright)
- [ClawHub publisher profile](https://clawhub.ai/user/ratingtesting)
- [Declared author profile](https://github.com/ratingtesting)
- [Architecture overview](assets/architecture.md)
- [Security gates](references/security-gates.md)
- [Circuit breaker](references/circuit-breaker.md)
- [Web guard](references/web-guard.md)
- [Remediation guide](references/remediation.md)
- [QA results](qa-results/README.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands, code-editing instructions, reports, and file templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create project-local tracking files after consent and reports gate outcomes in plain language.]

## Skill Version(s):

1.6.8 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
