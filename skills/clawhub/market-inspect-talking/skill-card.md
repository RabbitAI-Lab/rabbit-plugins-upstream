## Description:

Turns user-supplied merchant inspection notices and authorized still images into short, individually delivered talking clips that read the supplied notices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Market-supervision offices use this skill to plan and create short merchant-notice talking clips from their own inspection notices and authorized stills, with separate approvals for paid voice, speech, and video stages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting an account stores a reusable device token with broad account access.

Mitigation: Review the requested access before connecting, protect the device credential, and revoke the connection when no longer needed.

Risk: Remote voice, speech, and video generation may incur charges.

Mitigation: Check live prices and require separate approval before each paid stage; review billing after completion.

Risk: The package may update itself automatically without a separate confirmation.

Mitigation: Review the update setting before use and disable automatic updates if changes require prior approval.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/market-inspect-talking)
- [Merchant notice talking workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)

## Skill Output:

**Output Type(s):** [Text, Video clips]

**Output Format:** [Labeled Markdown slot list and separate short video files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically 2–8 unstitched clips, each planned for 2–15 seconds; final files depend on approvals and paid generation.]

## Skill Version(s):

0.1.8 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
