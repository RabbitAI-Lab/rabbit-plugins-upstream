## Description:

Turn authorized stills and seller-supplied step facts into one assembly step video per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, listing teams, and their agents use this skill to turn authorized assembly-step stills and seller-supplied facts into one short image-to-video clip per step, with live pricing and confirmation before billable generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared Beatra device token with broad media, task, artifact, and wallet-related scopes.

Mitigation: Install only for Beatra accounts and still images the user intends to use with Beatra, keep the token in the documented local credential file, and revoke or reconnect access when the account should no longer be available to the skill.

Risk: Silent automatic updates are enabled by default for the bundled client.

Mitigation: Use the documented update controls to disable automatic checks with `python3 scripts/mcp_client.py update --auto off` or manually check updates before accepting replacement files.

Risk: Video generation is billable and transport uncertainty can create duplicate-work risk if requests are replayed incorrectly.

Mitigation: Require live pricing and explicit user confirmation before paid generation, then reuse the same `client_request_id` only for byte-identical recovery of an uncertain request.

Risk: Assembly stills and seller-provided facts are sent to Beatra for media generation.

Mitigation: Use only authorized stills and provided step facts, and do not infer missing instructions, tool lists, warnings, or steps from unrelated sources.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/assembly-one-step-clip)
- [Beatra skill homepage](https://beatra.ai/skills/assembly-one-step-clip)
- [Assembly one-step workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Bundled MCP Client diagnostics](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API Calls, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with JSON MCP payloads and generated video artifact references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one generated clip per authorized still; billable video calls require live pricing, user confirmation, and per-still request identity.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
