## Description:

Fully automated multi-round code iteration with configurable N-dimension parallel review, onboarding/personalization, and a cross-assistant installer/update system with mandatory SHA256 checksum verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use Iterate to ask an AI coding assistant to review, fix, validate, and re-review a codebase across multiple quality dimensions until findings converge or a configured round limit is reached. It also supports defensive-programming mode for ordinary coding tasks such as feature work, bug fixes, refactors, API integration, and test additions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can edit files, run configured validation commands, and perform Git operations.

Mitigation: Use it only in repositories where that autonomy is acceptable, review validation.commands before use, and keep auto_merge and push_per_round disabled unless remote writes are explicitly intended.

Risk: Installer and update flows can download release artifacts or install a CLI onto PATH.

Mitigation: Prefer pinned, inspectable installers; rely on the documented SHA256 verification path; and avoid curl-piped shell installation paths when reviewing a release.

Risk: Architectural fixes may involve broader multi-file changes.

Mitigation: Require explicit approval for architectural work and review changes on the isolated iterate branch or worktree before merging.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jingzhao-l/skills/iterate-skill)
- [Project README](https://github.com/jingzhao-l/iterate-skill)
- [GitHub Releases](https://github.com/jingzhao-l/iterate-skill/releases)
- [npm Installer Package](https://www.npmjs.com/package/iterate-skill-installer)
- [Agent Skills Placeholder Standard](https://agentskills.io/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown progress reports, code edits, shell commands, configuration files, validation summaries, and final review reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May edit files, run configured validation commands, and perform Git operations according to skill configuration and user approval gates.]

## Skill Version(s):

3.2.3 (source: SKILL.md frontmatter, pyproject.toml, npm package, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
