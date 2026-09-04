## Description:

Creates Bilibili upload copy from a video topic, title, outline, or finished script, then can turn the selected title and thumbnail brief into one matching 16:9 landscape thumbnail.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and publishing-support agents use this skill to draft Bilibili-ready titles, descriptions, tags, chapter text, pinned comments, and a thumbnail brief from a supplied video topic, outline, or script. After approval of a priced plan, it can request one matching 16:9 thumbnail through Beatra.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses broad Beatra device authorization that can spend credits and access multiple media-generation capabilities, not just Bilibili thumbnails.

Mitigation: Install only where that shared authorization is acceptable, review the Beatra connection before approving it, and use Beatra Console or the uninstall flow to revoke access when needed.

Risk: The bundled client silently checks for and installs package updates by default.

Mitigation: In managed or sensitive environments, disable silent updates with `python3 scripts/mcp_client.py update --auto off` and review update behavior before use.

Risk: Thumbnail generation is paid work, and duplicate or changed submissions can spend additional credits.

Mitigation: Require the priced plan and stable `client_request_id` before any generation call, and retry uncertain submissions only with identical arguments and the same request ID.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/bilibili-publishing-pack)
- [Beatra skill homepage](https://beatra.ai/skills/bilibili-publishing-pack)
- [Bilibili publishing workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with structured Bilibili upload copy, thumbnail planning details, inline shell commands, and optional task result fields.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include one generated 16:9 thumbnail artifact link, returned dimensions, task ID, resolved model, and billing.net_charged_credits after user approval of a paid Beatra image task.]

## Skill Version(s):

0.1.4 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
