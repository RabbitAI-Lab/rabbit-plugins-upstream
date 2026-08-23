## Description:

Create a short visual clip guided by a song's mood, rhythm, and visual concept.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to turn a short music excerpt and visual direction into a cinematic music promo clip, animated cover-art clip, transition between approved frames, or mood-driven visual concept.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a persistent shared Beatra device credential with broad media-generation scopes.

Mitigation: Install only in environments that accept the shared credential model, protect the local credential files, and review whether the requested scopes are appropriate before authorization.

Risk: The package silently checks for and installs updates by default.

Mitigation: Use `python3 scripts/mcp_client.py update --auto off` when administrator-managed updates are required, and rely on the documented verified update path for manual checks.

Risk: The authoritative security verdict is suspicious because of the broad shared credential and default self-update behavior.

Mitigation: Review the package before installation and scan it before deployment, especially in managed or high-trust environments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/ai-music-video-clip-maker)
- [Beatra Skill Homepage](https://beatra.ai/skills/ai-music-video-clip-maker)
- [Music Video Clip Workflow](references/workflow.md)
- [Billing, Errors, and Recovery](references/billing-errors-and-recovery.md)
- [Tasks and Results](references/tasks-and-results.md)
- [Installation and Authentication](references/installation-and-auth.md)
- [MCP Connection](references/mcp-connection.md)
- [Automatic Updates and Safety](references/automatic-updates-and-safety.md)
- [Uninstall and Disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides Beatra media-generation calls, task polling, billing reporting, and delivery of returned video artifacts or links.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
