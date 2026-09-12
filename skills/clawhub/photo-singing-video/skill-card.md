## Description:

Animate one clear portrait with a short singing audio excerpt to create an expressive singing-photo clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators use this skill to animate a single inspected portrait with an approved singing-audio excerpt into a singing-photo video, then review the result for identity, mouth and facial movement, singing energy, audio presence, synchronization, and visible drift.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra device credential with broad generation, artifact, task, and wallet-spend capabilities.

Mitigation: Install only after accepting that access, keep the credential private, and revoke the device from the Beatra Console or uninstall when the skill is no longer needed.

Risk: Selected portraits and audio excerpts are uploaded to Beatra for generation.

Mitigation: Inspect local media first and upload only files the user intentionally selected for this singing-video request.

Risk: Silent package updates are enabled by default before ordinary Beatra commands.

Mitigation: Use the documented update controls to disable automatic updates with `python3 scripts/mcp_client.py update --auto off` or check available updates before applying them.

Risk: Video generation is paid work and accidental retries can create duplicate submissions.

Mitigation: Show the admission card, obtain explicit balance or top-up confirmation, freeze one `client_request_id`, submit once, and recover uncertain responses with the same unchanged request identity.

## Reference(s):

- [Singing-photo workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/photo-singing-video)
- [Beatra skill homepage](https://beatra.ai/skills/photo-singing-video)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Files]

**Output Format:** [Markdown guidance with inline shell commands, JSON MCP payloads, and returned video artifact links when generation succeeds]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses one portrait and one singing-audio excerpt per video request; reports returned task status, resolved model, dimensions, duration, usage, and net charged credits when available.]

## Skill Version(s):

0.1.4 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
