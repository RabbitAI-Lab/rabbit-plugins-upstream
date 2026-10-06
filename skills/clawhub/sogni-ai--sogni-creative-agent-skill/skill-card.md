## Description:

Helps agents generate and edit images, videos, music, and other creative media through Sogni AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sogni-ai](https://clawhub.ai/user/sogni-ai)

### License/Terms of Use:

MIT

## Use Case:

Creators and developers use this skill with an agent to produce or revise images, video, music, speech, and 3D assets through Sogni, and to manage repeatable creative workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI accesses a Sogni API key and may send selected media to Sogni for hosted generation.

Mitigation: Provide the key only when authorized and review media before using hosted workflows; use direct CLI mode for media that must remain local.

Risk: Renders can consume credits or subscription capacity, especially with automatic cost confirmation disabled.

Mitigation: Check expected costs and billing settings; approve --no-confirm-cost only when intended.

Risk: Personas and memories persist locally; purging on uninstall can remove user data.

Mitigation: Review stored data and backups before uninstalling with --purge.

Risk: Self-updating changes the installed CLI.

Mitigation: Approve self-update only when an update is intended.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/sogni-ai/skills/sogni-creative-agent-skill)
- [Sogni AI](https://sogni.ai)
- [Sogni dashboard and API key](https://dashboard.sogni.ai)
- [Model and feature reference](references/models.md)
- [Hosted API reference](references/hosted-api.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Media files, Configuration guidance]

**Output Format:** [Agent guidance and CLI commands; generated media files and optional JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media generation requires a Sogni API key and may consume credits or subscription capacity.]

## Skill Version(s):

3.54.5 (source: skill metadata, CHANGELOG, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
