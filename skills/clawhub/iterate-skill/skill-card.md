## Description:

Fully automated multi-round code iteration with configurable N-dimension parallel review, onboarding/personalization, and a cross-assistant installer/update system with mandatory SHA256 checksum verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use Iterate to run structured multi-round code review, apply scoped fixes, generate project onboarding context, and validate changes before release.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify code and run configured validation commands during normal iteration.

Mitigation: Use review-only or dry-run mode when changes are not desired, and review validation.commands before allowing execution.

Risk: Git automation can create branches or worktrees and may merge or push when those settings are enabled.

Mitigation: Keep auto_merge and push_per_round disabled unless automatic main-branch or remote changes are explicitly intended.

Risk: Passing tokens on the command line can expose credentials on shared systems.

Mitigation: Avoid --token on shared machines and prefer safer credential handling supported by the local environment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jingzhao-l/skills/iterate-skill)
- [Agent Skills Standard](https://agentskills.io/)
- [npm Package: iterate-skill-installer](https://www.npmjs.com/package/iterate-skill-installer)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline code blocks, file edits, shell commands, and configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update project onboarding files, local git branches or worktrees, and review reports depending on mode and user-approved settings.]

## Skill Version(s):

2.3.17 (source: frontmatter and pyproject.toml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
