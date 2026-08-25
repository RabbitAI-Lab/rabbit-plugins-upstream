## Description:

Fully automated multi-round code iteration with configurable N-dimension parallel review, onboarding/personalization, and a cross-assistant installer/update system with mandatory SHA256 checksum verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use Iterate to run multi-round code review and repair loops across a repository, with configurable review dimensions, onboarding, validation, and opt-in git merge/push behavior. Review-only mode supports read-only audit reports for pre-release checks and code quality audits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-autonomy repository changes and validation-command execution can alter code or run project commands.

Mitigation: Install only where file write, shell, git, and validation-command authority is acceptable; keep work on the iterate branch or worktree and review changes before merging.

Risk: Automatic merge or push could publish unreviewed changes if enabled.

Mitigation: Keep auto_merge and push_per_round disabled unless intentionally needed; review the iterate branch and use normal branch protection or PR review before publishing.

Risk: Installer and update paths download release assets and may install a persistent CLI.

Mitigation: Use verified release downloads, prefer the normal installer over curl pipe bash install paths, pass --no-cli if a persistent CLI is not wanted, and avoid passing GitHub tokens on the command line.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jingzhao-l/skills/iterate-skill)
- [Project repository](https://github.com/jingzhao-l/iterate-skill)
- [README](README.md)
- [Changelog](CHANGELOG.md)
- [npm installer](https://www.npmjs.com/package/iterate-skill-installer)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown summaries, code edits, shell command proposals, and configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write files and run validation commands when not in review-only mode.]

## Skill Version(s):

2.8.1 (source: SKILL.md frontmatter, pyproject.toml, CHANGELOG, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
