## Description:

Query, install, update, and edit AI agent skills on compatible Skill Hubs, using authenticated API access when configured and public fallback behavior otherwise.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songhonglei](https://clawhub.ai/user/songhonglei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to discover, inspect, install, and update skills on compatible or self-hosted Skill Hubs. Owners can also manage card metadata through a guarded edit flow when their Hub supports it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent may install or update the wrong skill, version, author, or Hub target.

Mitigation: Confirm the exact slug, version, author, and Hub before state-changing install or update actions.

Risk: Hub tokens can expose private skill access or account capabilities if handled carelessly.

Mitigation: Use tokens with the minimum needed scope, keep credentials private, and avoid echoing or committing full tokens.

Risk: Remote card metadata edits can unintentionally change an owned skill's public presentation.

Mitigation: Use the guarded GET, diff, backup, confirm, PUT, verify, and rollback flow; set SKILL_HUB_DISABLE_EDIT=1 when editing is not needed.

Risk: Downloaded skill archives can write files during installation.

Mitigation: Review and scan skills before deployment; rely on the included slug validation and ZIP path checks before extraction.

## Reference(s):

- [Skill Hub API Reference](references/api.md)
- [README](README.md)
- [Changelog](CHANGELOG.md)
- [ClawHub skill page](https://clawhub.ai/songhonglei/skills/skill-hub-query)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with shell command invocations and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute local scripts that call configured Hub APIs and write cache, backup, or installed skill files.]

## Skill Version(s):

1.3.0 (source: evidence.release.version and artifact CHANGELOG.md, released 2026-08-23)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
