## Description:

Turn seller-supplied floor-plan facts into one listing still per room. This listing still studio lays out the seller-supplied room names and layout lines as a listing still and property-page graphic. Use it for listing still sets, room listing stills, and property-page listing cards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External real estate sellers, listing teams, and their agents use this skill to turn confirmed room names and floor-plan notes into a planned set of listing stills. The skill helps the agent confirm scope, pricing, task execution, billing recovery, and delivery details for one generated still per room.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared local Beatra device token with broad media, wallet, upload, artifact, and task permissions.

Mitigation: Install and authorize only when the publisher and Beatra connection are trusted; keep the token out of chat, logs, command arguments, environment variables, and package directories, and use the documented uninstall or console revocation flow when access is no longer needed.

Risk: The bundled client silently checks for and installs package updates by default.

Mitigation: Disable automatic updates with the documented update command if the user wants review before replacement; rely on the package's checksum and package-owned-file verification when updates remain enabled.

Risk: Paid remote image tasks can create duplicate charges if uncertain responses are retried incorrectly.

Mitigation: Read the live model card before approval, use one opaque client_request_id per room, submit each task once, poll existing task IDs, and retry only byte-identical requests with the same identity.

Risk: Generated listing stills may contain unreadable text or misleading property claims if the model infers missing facts.

Mitigation: Use only seller-confirmed floor-plan facts, do not infer address, price, area, school district, or identity details, and review visible text against the confirmed fact list before delivery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/real-estate-listing-set)
- [Listing still workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, API calls, files, guidance]

**Output Format:** [Markdown guidance with JSON payload examples, shell command examples, generated image artifact files, and task/billing metadata.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normally delivers 4 to 8 room stills, one image task per room, with observed dimensions, formats, task IDs, resolved models, and net charged credits.]

## Skill Version(s):

0.1.1 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
