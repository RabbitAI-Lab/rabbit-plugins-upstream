## Description:

Fully automated multi-round code iteration with configurable N-dimension parallel review, onboarding/personalization, and a cross-assistant installer/update system with mandatory SHA256 checksum verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use Iterate to have an AI coding assistant run multi-round code review, fix atomic issues, coordinate approved larger fixes, validate changes, and apply defensive programming gates to incremental coding tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can autonomously review and edit code, run configured validation commands, and use git workflows.

Mitigation: Review validation.commands before use and keep auto_merge and push_per_round disabled unless automatic publication is intentional.

Risk: The installer can place the iterate CLI on PATH.

Mitigation: Use --no-cli or manual copy if only the skill files should be installed.

Risk: A provided GitHub token may be used for release or API access during install or update.

Mitigation: Use a minimally scoped token and treat it as active for GitHub release/API requests.

## Reference(s):

- [ClawHub Iterate skill page](https://clawhub.ai/jingzhao-l/skills/iterate-skill)
- [iterate-skill-installer npm package](https://www.npmjs.com/package/iterate-skill-installer)
- [Agent Skills standard](https://agentskills.io/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown status reports, code edits, shell commands, and structured configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May modify workspace files, run configured validation commands, and prepare git changes when enabled by the user.]

## Skill Version(s):

3.0.1 (source: frontmatter, pyproject.toml, npm package, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
