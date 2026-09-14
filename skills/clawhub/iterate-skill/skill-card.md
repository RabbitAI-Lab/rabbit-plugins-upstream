## Description:

Fully automated multi-round code iteration with configurable N-dimension parallel review, onboarding/personalization, and a cross-assistant installer/update system with mandatory SHA256 checksum verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use Iterate to have AI assistants perform multi-round code review, automated fixes, verification, and convergence before a change is delivered. It can also be used in review-only mode for read-only health checks and in defensive mode for normal incremental coding tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer or update paths can execute local code and install command-line tooling.

Mitigation: Use the checksum-verified npx or release path, verify release checksums, and avoid curl-to-bash installation paths.

Risk: Configured validation commands can execute high-impact code from the target repository.

Mitigation: Review iterate.config.yaml before validation runs and allow only trusted npm, npx, make, Python, or equivalent project commands.

Risk: Autonomous review and fixing can modify files and perform git operations.

Mitigation: Keep auto_merge and push_per_round disabled until diffs have been reviewed, and use review-only or dry-run mode when changes are not desired.

## Reference(s):

- [Iterate ClawHub Release](https://clawhub.ai/jingzhao-l/skills/iterate-skill)
- [Iterate GitHub Repository](https://github.com/jingzhao-l/iterate-skill)
- [Iterate npm Installer](https://www.npmjs.com/package/iterate-skill-installer)
- [Agent Skills Standard](https://agentskills.io/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries, code changes, shell command guidance, and configuration updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May edit files and run configured validation commands unless invoked in review-only or dry-run mode.]

## Skill Version(s):

3.3.1 (source: frontmatter, pyproject.toml, CHANGELOG, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
