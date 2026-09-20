## Description:

ClawSecCheck audits a user's local OpenClaw setup for configuration, prompt-injection, installed skill and plugin, MCP, credential-surface, and host-security risks while keeping reports local.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gl0di](https://clawhub.ai/user/gl0di)

### License/Terms of Use:

MIT

## Use Case:

Developers, security reviewers, and OpenClaw users use this skill to inspect their own OpenClaw setup, surface security findings, monitor drift, and vet local skills or plugins before installation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scanner reads OpenClaw configuration, logs, installed skill and plugin text, and limited credential-related artifacts.

Mitigation: Install only when that local read scope is acceptable, review the documented scope before running, and avoid sharing raw reports that may describe local configuration.

Risk: The skill can write local audit history, monitor state, and requested report files; some opt-in modes can write inside the audited OpenClaw home.

Mitigation: Use --no-history when local audit history is not desired, and review opt-in modes such as --monitor, --watch, --apply-ignore-proposals, and report export paths before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gl0di/skills/clawseccheck)
- [Security model](SECURITY_MODEL.md)
- [Security policy](SECURITY.md)
- [Output schema](docs/OUTPUT_SCHEMA.md)
- [User guide](docs/USAGE.md)
- [Check catalog reference](docs/CHECKS.md)
- [CLI flags](references/cli-flags.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, SARIF, files, shell commands, configuration, guidance]

**Output Format:** [Conversational summaries and reports, with optional JSON, SARIF, HTML, SVG badge, PDF, and saved text outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are local by default; grading is emitted only when the documented audit layers have enough evidence.]

## Skill Version(s):

4.2.1 (source: SKILL.md frontmatter, CHANGELOG, pyproject.toml, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
