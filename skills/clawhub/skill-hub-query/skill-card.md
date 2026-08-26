## Description:

skill-hub-query helps agents query, install, update, and edit AI agent skills on compatible Skill Hub services, using authenticated APIs when tokens are configured and public fallback paths otherwise.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songhonglei](https://clawhub.ai/user/songhonglei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to discover compatible Hub skills, inspect version history, install or update releases, and edit owned skill-card metadata with review and rollback safeguards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Network requests and tokens can be exposed to an untrusted or incorrectly configured Hub endpoint.

Mitigation: Configure SKILL_HUB_URL and credentials only for trusted compatible Hubs, keep credential files protected, and avoid echoing or committing full tokens.

Risk: Install and edit flows can replace local skill files or modify owned Hub card metadata.

Mitigation: Review proposed installs, edit diffs, backups, and confirmation prompts before allowing write actions.

Risk: doctor.sh performs real connectivity checks against the configured Hub, including the optional edit probe.

Mitigation: Run diagnostics only when contacting the configured Hub is acceptable, and disable edit probing where the Hub does not support it.

## Reference(s):

- [Skill Hub API Reference](references/api.md)
- [README](README.md)
- [Changelog](CHANGELOG.md)
- [skillhub.cn](https://skillhub.cn)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown prose with command invocations, user-readable tables, and JSON from Hub API queries when useful.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include local cache status, diagnostic results, installation guidance, and edit diffs; write actions require explicit user confirmation.]

## Skill Version(s):

1.3.0 (source: evidence.release, SKILL.md, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
