## Description:

Fully automated multi-round code iteration with configurable N-dimension parallel review, onboarding/personalization, and a cross-assistant installer/update system with mandatory SHA256 checksum verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use Iterate to run multi-round code review, fix atomic issues, coordinate approved architectural changes, and validate a project until findings converge or the configured round limit is reached.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-autonomy code review and fixing can edit project files, run configured validation commands, and use git.

Mitigation: Review validation.commands before use, inspect changes before accepting architectural fixes, and keep auto_merge and push_per_round disabled unless automatic integration is intended.

Risk: Installer behavior can add a PATH-level CLI or use optional remote shell installation flows.

Mitigation: Use --no-cli or manual copy when a PATH-level CLI is not desired, and avoid curl-to-bash installation unless the script has been reviewed.

Risk: Broad file and shell permissions increase impact if the skill is run on an unsuitable project or with unsafe configuration.

Mitigation: Use review-only or dry-run mode for audits, avoid sensitive files, and run in an isolated branch or worktree for normal iteration.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jingzhao-l/skills/iterate-skill)
- [README](README.md)
- [Skill Instructions](SKILL.md)
- [Configuration Schema](config/config.schema.json)
- [Agent Skills](https://agentskills.io/)
- [npm Installer](https://www.npmjs.com/package/iterate-skill-installer)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with proposed code edits, shell commands, configuration files, and review summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can run in review-only mode; normal mode may modify files, run configured validation commands, and use git under user-controlled settings.]

## Skill Version(s):

2.11.2 (source: SKILL.md frontmatter, pyproject.toml, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
