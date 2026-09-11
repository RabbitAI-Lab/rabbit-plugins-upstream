## Description:

Build dated store PA announcement reads for one campaign window: open, promo, flash, and close.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External retail teams use this skill to create dated in-store PA campaign reads for opening, promotion, flash-sale, and closing slots, using one consistent store voice across the campaign window.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill grants broad Beatra account access and stores a shared bearer token in ~/.beatra.

Mitigation: Review the Beatra approval screen before authorization, keep the token out of chat, logs, environment variables, and command arguments, and revoke the device in the Beatra Console when access is no longer needed.

Risk: Silent automatic package updates are enabled by default.

Mitigation: Use the documented update controls to disable silent checks when review-before-update is required, and rely on the bundled verification and rollback behavior for package updates.

Risk: Paid voice cloning or text-to-speech calls can consume Beatra credits.

Mitigation: Confirm consent for any voice clone, confirm the voice and live campaign estimate before paid synthesis, submit each frozen request once, and recover uncertain paid calls only with the same client request identity.

## Reference(s):

- [Store PA broadcast workflow](references/workflow.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/store-pa-broadcast-pack)
- [Publisher profile](https://clawhub.ai/user/beatra-ai)
- [Beatra skill homepage](https://beatra.ai/skills/store-pa-broadcast-pack)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Files]

**Output Format:** [Markdown guidance with JSON payloads, shell commands, and generated audio file references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces dated, labeled PA read outputs and reports duration, MIME type, resolved model, artifact or URL, and net charged credits when generation succeeds.]

## Skill Version(s):

0.1.2 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
