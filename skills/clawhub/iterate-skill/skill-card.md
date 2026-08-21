## Description:

Fully automated multi-round code iteration with configurable N-dimension parallel review, onboarding/personalization, and a cross-assistant installer/update system with mandatory SHA256 checksum verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers and software engineering teams use Iterate to run multi-round code review, bug fixing, security hardening, validation, and project onboarding across AI coding assistants. It can also run in review-only mode to produce read-only health-check reports without changing files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use broad repository read/write access, shell validation, and git operations during normal iteration.

Mitigation: Install only when that access is acceptable, keep work on isolated branches or worktrees, and review generated changes before merging.

Risk: Automatic merge or push could publish unintended changes if explicitly enabled.

Mitigation: Keep auto_merge and push_per_round disabled unless the repository has appropriate review and branch protection controls.

Risk: Installer and update flows can place a PATH command and download release assets.

Mitigation: Use --no-cli if a PATH command is not desired, prefer verified installer paths, and avoid curl-pipe-shell installation flows.

Risk: Passing GitHub tokens on a command line can expose credentials through shell history or process listings.

Mitigation: Do not pass GitHub tokens on the command line; use safer credential handling and remove unnecessary tokens.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jingzhao-l/skills/iterate-skill)
- [Publisher Profile](https://clawhub.ai/user/jingzhao-l)
- [Project Repository](https://github.com/jingzhao-l/iterate-skill)
- [npm Installer](https://www.npmjs.com/package/iterate-skill-installer)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports with code edits, shell command plans, and configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normal mode may modify repository files and git state; review-only mode produces read-only reports.]

## Skill Version(s):

2.5.0 (source: frontmatter, pyproject.toml, changelog, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
