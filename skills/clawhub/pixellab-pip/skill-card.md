## Description:

Guides agents through PixelLab setup, authentication, documented MCP and REST routing, asset generation, editing, animation, cost-aware execution, and output reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shilo](https://clawhub.ai/user/shilo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external creators use this skill to configure PixelLab access and route agent work through supported PixelLab surfaces for sprites, characters, portraits, tilesets, animations, UI assets, cost questions, and reproducible generation records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live PixelLab use can spend generations or credits.

Mitigation: Require explicit user approval for paid generation, respect stated budgets, and keep automatic execution off unless the user has approved that posture.

Risk: PixelLab credentials could be exposed if pasted into chat or written into outputs.

Mitigation: Keep PIXELLAB_SECRET in local environment or MCP client secret storage, use it only as an auth header, and never print, store, or ask the user to paste the token in chat.

Risk: Remote PixelLab assets may be created or modified during live workflows.

Mitigation: Treat destructive remote changes as approval-gated actions, list the affected assets before proceeding, and prefer read-only inspection when state is unclear.

## Reference(s):

- [ClawHub PixelLab Pip skill page](https://clawhub.ai/shilo/skills/pixellab-pip)
- [Official PixelLab Documentation](artifact/references/official-pixellab-documentation.md)
- [PixelLab REST v2 API docs](https://api.pixellab.ai/v2/docs)
- [PixelLab REST v2 OpenAPI schema](https://api.pixellab.ai/v2/openapi.json)
- [PixelLab MCP tool guide](https://api.pixellab.ai/mcp/docs)
- [PixelLab MCP setup](https://www.pixellab.ai/mcp)
- [Setup](artifact/references/setup.md)
- [Credentials](artifact/references/credentials.md)
- [Cost Routing](artifact/references/cost-routing.md)
- [Job Lifecycle](artifact/references/job-lifecycle.md)
- [Blueprint](artifact/references/blueprint.md)
- [Usage Reporting](artifact/references/usage-reporting.md)
- [Aseprite CLI Integration](artifact/references/aseprite-cli.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown with inline shell commands, code, JSON, file paths, and concise status or final reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local PixelLab output folders, manifests, blueprint JSON, preview assets, and integration snippets when a user-approved workflow calls for them.]

## Skill Version(s):

1.8.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
