## Description:

Fully automated multi-round code iteration with configurable N-dimension parallel review, onboarding/personalization, and a cross-assistant installer/update system with mandatory SHA256 checksum verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use Iterate to have an AI coding assistant run multi-round code review, fix eligible issues, verify changes, and converge a project before delivery. It also supports a defensive-programming mode for normal incremental coding tasks that need pre-checks, post-checks, invariants, and final review gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can grant a coding agent broad project access, including file edits, configured local commands, and git operations.

Mitigation: Use it only on repositories where that access is acceptable, inspect iterate.config.yaml first, and keep changes on an isolated branch or worktree for review.

Risk: Automatic merge or push settings can make agent-produced changes affect shared repository history or remote branches.

Mitigation: Keep git.auto_merge and git.push_per_round disabled unless explicitly needed, and review changes before merging or pushing.

Risk: Configured validation commands execute locally and can be unsafe if the project configuration is not trusted.

Mitigation: Review validation.commands and command_whitelist before use, and configure only commands that are appropriate for the target project.

Risk: Installer paths that download and run remote content, command-line GitHub tokens, or curl-piped shell commands increase supply-chain and credential exposure.

Mitigation: Prefer the verified installer flow, use --no-cli when only skill files are needed, avoid curl | bash harness installation, and avoid passing GitHub tokens on the command line.

## Reference(s):

- [ClawHub Iterate Skill Page](https://clawhub.ai/jingzhao-l/skills/iterate-skill)
- [README.md](README.md)
- [SKILL.md](SKILL.md)
- [CHANGELOG.md](CHANGELOG.md)
- [Default Configuration](config/iterate.config.yaml)
- [Agent Skills Placeholder Standard](https://agentskills.io/)
- [npm Installer Package](https://www.npmjs.com/package/iterate-skill-installer)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with inline code blocks, project file edits, shell command invocations, configuration snippets, and optional JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review-only mode produces reports without file edits; edit modes can run configured local validation commands and git operations.]

## Skill Version(s):

3.1.0 (source: SKILL.md frontmatter, CHANGELOG.md, pyproject.toml, npm-installer/package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
