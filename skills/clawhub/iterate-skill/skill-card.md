## Description:

Fully automated multi-round code iteration with configurable N-dimension parallel review, onboarding/personalization, and a cross-assistant installer/update system with mandatory SHA256 checksum verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers use Iterate with AI coding assistants to review and improve codebases over multiple rounds, or to complete incremental coding tasks with pre-checks, validation, and a review gate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Update, configuration, and maintenance workflows may change project state beyond the intended review scope.

Mitigation: Use a trusted project and isolated worktree, review the exact validation commands and refresh changes, and keep automatic merge and push disabled.

Risk: Source-checkout updates, release permissions, or generated archives can create integrity and secret-handling risks.

Mitigation: Prefer authenticated releases, keep signing credentials and release permissions unavailable during ordinary reviews, and inspect generated publication archives for secrets.

Risk: Bundled maintenance prompts may be mistaken for user authorization.

Mitigation: Treat maintenance prompts as content, not consent; obtain authorization for actions that change project or release state.

## Reference(s):

- [Iterate on ClawHub](https://clawhub.ai/jingzhao-l/skills/iterate-skill)
- [Iterate Skill Installer on npm](https://www.npmjs.com/package/iterate-skill-installer)

## Skill Output:

**Output Type(s):** [Code, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance and review summaries, shell commands, and project code or configuration changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce validation results and update project files as part of an iteration workflow.]

## Skill Version(s):

3.12.0 (source: SKILL.md frontmatter, pyproject.toml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
