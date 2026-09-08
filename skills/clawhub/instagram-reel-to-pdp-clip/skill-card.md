## Description:

Instagram product video is one product detail video per product still after reading a competitor Reel. Use this Instagram PDP clip studio for a product page video and a Reel-to-PDP clip from the same still list.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and their agents use this skill to turn inspected product stills into one short product-detail clip per still, guided by either written composition notes or a confirmed public Instagram Reel lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package asks for a shared Beatra device connection with broad media, wallet, task, artifact, and credential-management authority.

Mitigation: Install only when that access is acceptable, keep the device token private, and use the bundled uninstall workflow or Beatra Console revocation when disconnecting.

Risk: The bundled client silently checks for and installs newer package releases by default.

Mitigation: Review update behavior before use and disable silent updates with `python3 scripts/mcp_client.py update --auto off` when automatic replacement is not desired.

Risk: Public Reel lookups and video generation can consume Beatra credits.

Mitigation: Approve only production cards whose lookup or video cost and count are understood, and preserve the same client request identity when recovering uncertain paid submissions.

Risk: Local product images are uploaded to Beatra as workflow inputs.

Mitigation: Use only product images the seller is comfortable uploading for this product-video task, and inspect files before submission.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/instagram-reel-to-pdp-clip)
- [Beatra skill homepage](https://beatra.ai/skills/instagram-reel-to-pdp-clip)
- [Product-detail clip workflow](references/workflow.md)
- [Reel lookup](references/reel-lookup.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands, JSON MCP payloads, task status summaries, billing facts, and returned video artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one product-detail clip per inspected product still; supported durations are 2-15 seconds, with 5 seconds as the default when the user allows it.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
