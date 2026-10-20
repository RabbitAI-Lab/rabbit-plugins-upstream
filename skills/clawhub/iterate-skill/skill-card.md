## Description:

Fully automated multi-round code iteration with configurable N-dimension parallel review, onboarding/personalization, and a cross-assistant installer/update system with mandatory SHA256 checksum verification. v3.0 adds a dual-mode (the original iterate mode plus a defensive-programming mode via /iterate defensive) that performs normal incremental coding tasks with defensive discipline end-to-end.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jingzhao-l](https://clawhub.ai/user/jingzhao-l)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use Iterate with an AI coding assistant to review a project across configured dimensions, make and validate iterative code changes, and maintain project onboarding and decision context. Its defensive mode guides ordinary coding tasks through incremental checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can make code changes and run configured validation commands.

Mitigation: Review the generated iterate.config.yaml and keep auto_merge and push_per_round disabled unless you deliberately want automatic Git actions.

Risk: An optional companion-harness installation path uses curl-to-bash.

Mitigation: Avoid that optional path and prefer verified release or source installs.

## Reference(s):

- [Iterate on ClawHub](https://clawhub.ai/jingzhao-l/skills/iterate-skill)

## Skill Output:

**Output Type(s):** [Code, Markdown, Configuration, Shell commands, Guidance]

**Output Format:** [Repository code changes, Markdown reports, YAML configuration, and validation commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Iterative, project-scoped output validated using configured project commands]

## Skill Version(s):

3.6.0 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
