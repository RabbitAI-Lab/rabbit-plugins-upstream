## Description:

Security toolkit for AI workflows that helps agents scan code or repositories for vulnerabilities, audit third-party skills and agent configuration before installation, evaluate shell command risk, and generate secure design questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rafter](https://clawhub.ai/user/rafter)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to scan code and repositories for secrets and vulnerabilities, audit third-party skills and agent configurations before installation, validate shell commands, and generate security-focused review questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security hooks, command validation, scanning, logging, and redaction can affect local development workflows.

Mitigation: Enable integrations deliberately with documented opt-in flags and review Rafter configuration and audit logs after installation.

Risk: Remote scans require RAFTER_API_KEY and may send code or dependency data to the Rafter service.

Mitigation: Use a scoped RAFTER_API_KEY only when remote SAST or SCA is intended; use local secrets scanning when remote analysis is not needed.

Risk: `rafter agent exec` can execute commands after validation unless dry-run behavior is explicitly selected.

Mitigation: Use dry-run mode for classification-only checks and review higher-risk commands before allowing execution.

## Reference(s):

- [Rafter homepage](https://rafter.so)
- [ClawHub skill page](https://clawhub.ai/rafter/skills/rafter-security)
- [Rafter publisher profile](https://clawhub.ai/user/rafter)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash code blocks and optional JSON from CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May depend on the local rafter CLI; remote SAST and SCA use RAFTER_API_KEY, while local secrets scanning can run without it.]

## Skill Version(s):

0.10.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
