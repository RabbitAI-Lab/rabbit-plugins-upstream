## Description:

Build an original livestream BGM playlist of 10 to 20 instrumental tracks for a room, store, or live-commerce shift.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, store operators, and live-commerce teams use this skill to plan, generate, and review a labeled pack of original instrumental background tracks for livestream rooms, stores, waiting screens, and product segments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses broad Beatra account authority through a shared local device authorization.

Mitigation: Install only when that authorization scope is acceptable, keep the Beatra credential local, review account and device permissions, and revoke the device from the Beatra Console if access is no longer needed.

Risk: Billable music generation can spend Beatra credits, and initial estimates may differ from settled usage.

Mitigation: Confirm playlist size, prompts, model, and live pack estimate before the first paid call; submit each slot once with a stable request ID and report settled net charged credits.

Risk: Automatic package updates are enabled by default and can replace installed package code after verification.

Mitigation: Use the provided update controls to disable silent checks when desired, and rely on checksum and manifest verification before accepting updates.

## Reference(s):

- [Livestream playlist workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Bundled MCP Client diagnostics](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/livestream-bgm-pack)
- [Beatra skill homepage](https://beatra.ai/skills/livestream-bgm-pack)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown guidance with command examples, JSON tool payloads, task results, artifact links, and billing details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a labeled playlist plan and reports actual returned durations, MIME types, sizes, URLs or artifact IDs, resolved model, and net charged credits.]

## Skill Version(s):

0.1.1 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
