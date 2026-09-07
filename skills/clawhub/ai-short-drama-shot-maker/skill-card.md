## Description:

Generate one cinematic vertical micro-drama shot from a frozen dramatic beat, actor and scene references, and camera direction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and developers use this skill to turn a single dramatic beat and optional actor or scene references into one vertical cinematic micro-drama shot. It supports text-only generation, animation from an approved opening image, interpolation between strict endpoint images, and generation from loose visual references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared Beatra account credential with broader media and wallet authority than the single-shot workflow strictly needs.

Mitigation: Install only if that account access is acceptable, keep the credential private, and revoke the Beatra device authorization from the Beatra Console when the skill is no longer needed.

Risk: The bundled client can silently replace package files through automatic updates.

Mitigation: Disable silent updates with `python3 scripts/mcp_client.py update --auto off` when reviewed files need to stay stable.

Risk: Video generation is a paid Beatra operation and duplicate submissions can create duplicate charges.

Mitigation: Use one frozen request identity per approved shot, submit exactly once, and retry only the identical payload with the same `client_request_id` after transport uncertainty.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/ai-short-drama-shot-maker)
- [Beatra Skill Homepage](https://beatra.ai/skills/ai-short-drama-shot-maker)
- [Short-drama shot workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON MCP payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces shot cards, admission summaries, Beatra MCP calls, task polling guidance, returned video artifact links, billing summaries, and continuity review notes.]

## Skill Version(s):

0.1.4 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
