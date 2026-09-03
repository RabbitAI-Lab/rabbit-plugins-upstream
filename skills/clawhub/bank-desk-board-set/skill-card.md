## Description:

Turn user-supplied branch window names and board lines into a four-to-eight still bank desk board set.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and operators use this skill to plan and generate matching branch window board stills from already approved window names and board lines. It is intended for image-pack production where the agent must preserve supplied text, confirm billable work, and deliver generated stills in window order.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence reports broad Beatra account authority beyond the narrow board-image purpose, including wallet spending and other media tools.

Mitigation: Install only when that shared authorization is acceptable, keep approvals explicit before billable generation, and revoke the Beatra device connection when it is no longer needed.

Risk: Automatic updates are enabled by default for this installation.

Mitigation: Consider disabling automatic updates for review-controlled environments and use the documented update check before accepting a new package version.

Risk: Generation requests can consume credits and uncertain transport responses can create duplicate-charge risk if retried incorrectly.

Mitigation: Use one opaque request identity per approved still, retry only identical uncertain requests with the same identity, and poll existing tasks before submitting replacements.

Risk: The Beatra credential is shared locally across Beatra skills.

Mitigation: Keep the credential only in the documented user-local file, avoid exposing tokens in chat, logs, arguments, or environment variables, and use the bundled uninstall flow to decide whether the shared connection can be removed.

## Reference(s):

- [Bank desk board pack workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Installation registration](artifact/references/installation-registration.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/bank-desk-board-set)
- [Beatra skill homepage](https://beatra.ai/skills/bank-desk-board-set)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Files, Guidance]

**Output Format:** [Markdown planning and delivery notes with JSON MCP arguments, shell commands, and returned image artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a free pack plan before billable image generation; image generation is one approved still per named window.]

## Skill Version(s):

0.1.1 (source: release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
