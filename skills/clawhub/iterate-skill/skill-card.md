## Description:

Fully automated multi-round code iteration with configurable N-dimension parallel review, onboarding/personalization, and a cross-assistant installer/update system with mandatory SHA256 checksum verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use this skill to run iterative code review, code improvement, defensive programming workflows, and read-only health checks across software projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation guidance includes mutable remote code execution and unpinned package installs.

Mitigation: Install only versions you trust, prefer a pinned npx version or verified release artifact, and inspect and pin the curl-to-bash harness installer before use.

Risk: The skill can edit code and run commands from validation.commands.

Mitigation: Review validation.commands before use, keep execution on isolated branches or worktrees, and use review-only or dry-run mode when you want a read-only audit.

Risk: The installer can place an iterate executable on PATH.

Mitigation: Use --no-cli or manual skill installation when a PATH-level executable is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jingzhao-l/skills/iterate-skill)
- [Project repository](https://github.com/jingzhao-l/iterate-skill)
- [Project releases](https://github.com/jingzhao-l/iterate-skill/releases)
- [npm installer package](https://www.npmjs.com/package/iterate-skill-installer)
- [Agent Skills](https://agentskills.io/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports and summaries with code, configuration, and shell command actions when changes are performed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review-only mode produces read-only reports; normal and defensive modes may edit files and run configured validation commands.]

## Skill Version(s):

3.3.0 (source: frontmatter, pyproject.toml, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
