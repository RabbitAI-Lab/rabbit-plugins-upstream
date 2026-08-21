## Description:

Make a photo sing by animating one clear portrait with a short singing audio excerpt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creative agents use this skill to turn one inspected portrait and one approved singing-audio excerpt into a singing-photo video, then review the result for identity, mouth and facial motion, audio presence, synchronization, and delivery quality.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared local Beatra bearer token for paid generation operations.

Mitigation: Keep the credential in the documented local file only, avoid exposing tokens in chat or command arguments, and revoke the device from the Beatra Console when it is no longer needed.

Risk: Paid video generation can charge Beatra credits or require a top-up before submission.

Mitigation: Show the admission card, live estimate, and top-up requirement before the paid call, then submit only after explicit balance or top-up confirmation.

Risk: Silent automatic updates are enabled by default for local package code.

Mitigation: Use the documented update controls to disable automatic checks when that behavior is not acceptable, and rely on the package checksum and archive verification described by the artifact.

Risk: Media generation may drift from the source identity or have imperfect mouth and audio synchronization.

Mitigation: Inspect the returned video for identity, mouth and facial movement, audio presence, synchronization, stable framing, ending quality, and actual duration before presenting conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/photo-singing-video)
- [Beatra skill page](https://beatra.ai/skills/photo-singing-video)
- [Singing-photo workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Installation registration](artifact/references/installation-registration.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Markdown]

**Output Format:** [Markdown guidance with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Beatra video artifacts or links, task status, resolved model details, usage, billing facts, and post-generation review notes.]

## Skill Version(s):

0.1.3 (source: server evidence release.version and artifact manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
