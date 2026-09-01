## Description:

Fully automated multi-round code iteration with configurable N-dimension parallel review, onboarding/personalization, and a cross-assistant installer/update system with mandatory SHA256 checksum verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use Iterate to run multi-round AI-assisted code review, apply small fixes, coordinate approved larger changes, and re-validate a codebase until review findings converge.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and edit a full codebase and run configured validation commands.

Mitigation: Install only where that access is acceptable, review generated diffs before merging, and use review-only or dry-run mode for audits.

Risk: Opt-in merge and push settings could publish or merge unintended changes if enabled.

Mitigation: Keep git.auto_merge and git.push_per_round false unless intentionally configured, and prefer manual review before merge or push.

Risk: Installer and update flows may add a PATH-level CLI or fetch remote release artifacts.

Mitigation: Use --no-cli when a PATH-level CLI is not desired, avoid curl-to-bash install paths, and rely on checksum-verified release downloads.

Risk: GitHub tokens passed on the command line may be exposed through shell history or process listings.

Mitigation: Avoid passing GitHub tokens directly on the command line.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jingzhao-l/skills/iterate-skill)
- [README](README.md)
- [Agent Skills specification](https://agentskills.io/)
- [npm installer package](https://www.npmjs.com/package/iterate-skill-installer)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown review summaries with proposed code edits, shell commands, and configuration changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read and edit project files, run configured validation commands, and produce review-only reports when invoked in dry-run mode.]

## Skill Version(s):

2.11.1 (source: frontmatter, pyproject.toml, npm package, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
