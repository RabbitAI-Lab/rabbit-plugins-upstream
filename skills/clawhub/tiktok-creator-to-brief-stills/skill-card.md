## Description:

Turn a TikTok creator homepage and recent posts into a collaboration brief still set.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Media buyers and creator marketing operators use this skill to turn one selected TikTok creator profile, recent public work, and already-written collaboration terms into a brief still pack for handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security summary says the skill asks for broad Beatra account powers through a shared local credential.

Mitigation: Review the requested Beatra authorization before installation and authorize paid lookup or image stages only after checking the displayed live credit cost and exact operation.

Risk: The server security summary says the bundled client silently self-updates executable files by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when silent code replacement is not acceptable.

Risk: The artifact workflow uses billable lookup and image-generation stages that can incur Beatra credits.

Mitigation: Keep lookup, generation, transform, and edit approvals separate; use one opaque request identity per paid call and avoid retrying changed arguments under the same identity.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/tiktok-creator-to-brief-stills)
- [Beatra Skill Homepage](https://beatra.ai/skills/tiktok-creator-to-brief-stills)
- [Workflow](references/workflow.md)
- [Creator Lookup](references/creator-lookup.md)
- [Installation and Authentication](references/installation-and-auth.md)
- [Billing, Errors, and Recovery](references/billing-errors-and-recovery.md)
- [Automatic Updates and Safety](references/automatic-updates-and-safety.md)
- [Tasks and Results](references/tasks-and-results.md)
- [MCP Connection](references/mcp-connection.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON tool arguments, task metadata, and generated image artifact references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated stills are delivered as image files or artifact references with MIME type, dimensions, size, task status, and net charged credits when available.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
