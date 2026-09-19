## Description:

Rafter Security helps developers scan code and repositories for security issues, audit third-party skills and agent configurations, evaluate shell command risk, and generate secure design questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rafter](https://clawhub.ai/user/rafter)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill to run Rafter-assisted security checks during AI-assisted development, including secret scanning, command-risk evaluation, skill audits, audit-log review, and configuration guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the Rafter CLI and may install agent hooks, keep audit or configuration state, and scan local code.

Mitigation: Install and use it only when the Rafter CLI is trusted for the target environment; review configuration and audit state after initialization.

Risk: `rafter run` can send remote analysis when RAFTER_API_KEY is configured.

Mitigation: Use local `rafter secrets` when remote analysis is not intended, and configure RAFTER_API_KEY only for environments where remote SAST, SCA, and deep-dive analysis are approved.

Risk: The `/rafter-bash` workflow may execute a command rather than only classify it.

Mitigation: Use explicit dry-run command-risk classification when analysis-only behavior is required, and review high-risk commands before execution.

## Reference(s):

- [Rafter Security ClawHub skill page](https://clawhub.ai/rafter/skills/rafter-security)
- [Rafter publisher profile](https://clawhub.ai/user/rafter)
- [Rafter homepage](https://rafter.so)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured security findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference RAFTER_API_KEY for remote analysis; local secret scanning can run without the API key.]

## Skill Version(s):

0.10.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
