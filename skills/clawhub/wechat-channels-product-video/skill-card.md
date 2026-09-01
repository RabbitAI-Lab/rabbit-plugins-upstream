## Description:

Create a vertical WeChat Channels product-display video from a real product photo and confirmed product information. Shape a clear product opening, one detail or use moment, and a clean ending, then prepare the finished product video with a title and publishing copy for WeChat Channels product content, including a new-product showcase video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to turn an inspectable product photo and confirmed product facts into a concise vertical WeChat Channels product showcase video, title, and publishing copy. It supports free planning before any paid Beatra image or video generation stage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared local Beatra Device Token with broad account authority for media generation, task access, artifact access, and wallet spending.

Mitigation: Install only after reviewing the Beatra scopes, keep the credential private in `~/.beatra/credentials.json`, and revoke the connected agent from the Beatra Console if access should end.

Risk: Paid image and video stages can spend Beatra credits after user-approved actions.

Mitigation: Require a live admission card and explicit user confirmation before each paid stage, submit each frozen payload once, and report returned usage and `billing.net_charged_credits` from the terminal task result.

Risk: The bundled client silently checks for and installs newer package files by default.

Mitigation: Run `python3 scripts/mcp_client.py update --auto off` after installation if silent replacement is not desired; use `python3 scripts/mcp_client.py update --check` to inspect available updates without replacing files.

Risk: The package records non-secret installation metadata and shares the Beatra connection across installed Beatra skills.

Mitigation: Use the bundled uninstall workflow so the shared connection is removed only when no other installed Beatra skill still depends on it.

## Reference(s):

- [Video Channels product-display planning](references/video-channel-planning.md)
- [WeChat Channels product-display video workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown prose with title and publishing copy, shell command snippets, JSON payload examples, and Beatra task result fields such as artifact IDs or URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an inspectable product photo and user-confirmed product facts; paid generation stages require explicit confirmation and Beatra credits.]

## Skill Version(s):

0.1.7 (source: release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
