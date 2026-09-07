## Description:

Turn seller-supplied floor-plan facts, an already-written walk-in script, and authorized stills into short talking clips for rental or listing walk-throughs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External listing sellers, rental operators, and their agents use this skill to plan and generate one short talking clip per authorized still from seller-supplied room facts and spoken lines, with separate approval steps for voice clone, speech, and video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared Beatra Device Token that can spend credits and access more media tools than this workflow needs.

Mitigation: Install only when that access is acceptable, keep the token in the private credential file, monitor wallet activity, and revoke the Beatra device authorization when the workflow is no longer needed.

Risk: The bundled client silently checks for and installs package updates by default.

Mitigation: Turn automatic updates off before normal use when review control is required, and use the explicit update check path before accepting a new release.

Risk: Clone, speech, and video generation are paid stages and retry mistakes can create duplicate tasks or charges.

Mitigation: Review each confirmation card carefully, use one opaque request identity per approved task, poll existing tasks before replay, and retry only byte-identical requests with the same request identity after transport uncertainty.

Risk: The workflow sends authorized property media and optional likeness or voice material to Beatra.

Mitigation: Use only media, likenesses, and voice samples the seller has rights to provide; do not treat file access as consent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/rental-walkin-avatar)
- [Beatra skill homepage](https://beatra.ai/skills/rental-walkin-avatar)
- [Walk-in talking-clip workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON payload examples and shell commands for Beatra task submission, polling, recovery, and delivery reporting.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can also guide an agent to deliver generated media artifacts and report returned MIME type, duration, size, task status, usage, and billing fields when present.]

## Skill Version(s):

0.1.2 (source: server release evidence and artifact/manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
