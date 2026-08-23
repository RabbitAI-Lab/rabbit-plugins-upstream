## Description:

Fully automated multi-round code iteration with configurable N-dimension parallel review, onboarding/personalization, and a cross-assistant installer/update system with mandatory SHA256 checksum verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use Iterate to run multi-round AI-assisted code review, apply approved fixes, validate changes, and manage onboarding and configuration across supported coding assistants.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automated git merge or per-round push can publish or merge changes before adequate human review.

Mitigation: Keep git.auto_merge and git.push_per_round set to false, review the iterate branch before merging, and use branch protection or pull requests for final integration.

Risk: Installer flows can place a persistent iterate command on PATH.

Mitigation: Use --no-cli for a skill-only install, or install the CLI with an isolated and trusted package workflow when the command is needed.

Risk: Shell-based install snippets and direct token arguments can increase supply-chain and secret-handling exposure.

Mitigation: Avoid curl-to-shell installation patterns, prefer packaged or checksum-verified installs, and pass GitHub credentials through environment variables or a safer secret mechanism instead of --token.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jingzhao-l/skills/iterate-skill)
- [ClawHub publisher profile](https://clawhub.ai/user/jingzhao-l)
- [Project repository listed in artifact README](https://github.com/jingzhao-l/iterate-skill)
- [npm installer package listed in artifact README](https://www.npmjs.com/package/iterate-skill-installer)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with inline code, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May modify files and produce git branch or worktree changes unless review-only or dry-run mode is used.]

## Skill Version(s):

2.8.0 (source: server release metadata, SKILL.md frontmatter, pyproject.toml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
