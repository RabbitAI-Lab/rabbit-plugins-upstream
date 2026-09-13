## Description:

Security toolkit for AI workflows that helps scan code or repositories for vulnerabilities, audit third-party skills, MCPs, and agent configurations, evaluate shell commands before running them, and generate secure design questions for new features.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rafter](https://clawhub.ai/user/rafter)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to ask an agent to run or guide Rafter security checks for code, repositories, third-party skills, MCPs, agent configuration, shell-command risk, secrets, and secure design review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on the Rafter CLI to mediate commands, logs, output filtering, and scans.

Mitigation: Install it only when you trust the Rafter CLI and review generated command guidance before running it.

Risk: Remote scans may send scan data to Rafter's service when RAFTER_API_KEY is configured.

Mitigation: Provide RAFTER_API_KEY only when remote scanning is appropriate for the repository and data being inspected.

Risk: Broad setup with `rafter agent init --all` may enable more integrations than needed.

Mitigation: Prefer explicit `--with-*` setup flags for the integrations required in the current agent environment.

Risk: Shell-command validation behavior can differ depending on whether the agent hook is installed or commands are routed through `/rafter-bash`.

Mitigation: Confirm whether commands are automatically validated by the installed hook or explicitly classified through `/rafter-bash` before relying on enforcement.

## Reference(s):

- [Rafter website](https://rafter.so)
- [Rafter publisher profile](https://clawhub.ai/user/rafter)
- [Rafter Security skill page](https://clawhub.ai/rafter/skills/rafter-security)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured security guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local Rafter CLI commands and optional remote scans when RAFTER_API_KEY is configured.]

## Skill Version(s):

0.10.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
