## Description:

Turn user-supplied insurance policy clauses and authorized stills into one insurance clause talking clip per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External insurance advisors and wealth educators use this skill to turn supplied policy clause text, authorized still images, and optional approved voice material into short one-still-per-clip clause explanation videos. It is intended for clause-reading packs that stay within the supplied insurance wording and avoid invented coverage or payout claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared Beatra device token with broad media and billing-related authority.

Mitigation: Authorize only from a trusted account and device, keep the token out of chat, logs, command arguments, and diffs, and review account permissions and spending exposure before use.

Risk: The bundled client silently self-updates installed package code by default.

Mitigation: Disable automatic updates after installation when tighter control is required, and review package changes before re-enabling updates.

Risk: The workflow can upload sensitive policy clauses, still images, voice samples, and generated media to Beatra.

Mitigation: Use only user-authorized materials, confirm likeness and voice rights before clone or video stages, and avoid exposing sensitive prompt or credential content in recovery messages.

Risk: Clone, speech, and video operations are paid stages where duplicate or changed submissions can create extra work and charges.

Mitigation: Confirm each paid stage separately, use one opaque client_request_id per logical request, poll existing task IDs before replaying work, and create a new request ID only for user-approved changed inputs.

## Reference(s):

- [Clause talking-clip workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/insurance-clause-talking)
- [Beatra skill homepage](https://beatra.ai/skills/insurance-clause-talking)
- [Beatra MCP endpoint](https://mcp.beatra.ai/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown guidance with JSON payloads and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a free slot list before paid stages, then guides voice clone, speech synthesis, video animation, task polling, billing review, and recovery.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
