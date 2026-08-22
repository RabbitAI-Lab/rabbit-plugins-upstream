## Description:

Fully automated multi-round code iteration with configurable N-dimension parallel review, onboarding/personalization, and a cross-assistant installer/update system with mandatory SHA256 checksum verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use Iterate to run multi-round code review, fix atomic issues, coordinate approved architectural fixes, and validate changes until findings converge or the configured round limit is reached.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automated code review and fixing can modify real repositories or prepare changes for merge.

Mitigation: Review the skill before installing, keep auto_merge and push_per_round disabled unless explicitly needed, and inspect the iterate/* branch before merging.

Risk: Some installation paths described by the artifact involve remote shell execution.

Mitigation: Avoid the curl | bash harness installation path for sensitive environments and prefer checksum-verified installers.

Risk: Persistent CLI installation and token handling can broaden exposure.

Mitigation: Use --no-cli when a persistent iterate command is not needed, and pass GitHub tokens through safer environment handling instead of command-line history.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jingzhao-l/skills/iterate-skill)
- [Agent Skills standard](https://agentskills.io/)
- [iterate-skill installer package](https://www.npmjs.com/package/iterate-skill-installer)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports, code patches, configuration files, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update ITERATE.md, iterate.config.yaml, review reports, branches or worktrees, and code changes depending on mode and user approval.]

## Skill Version(s):

2.7.0 (source: SKILL.md frontmatter, CHANGELOG, pyproject.toml, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
