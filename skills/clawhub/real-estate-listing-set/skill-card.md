## Description:

Turn seller-supplied floor-plan facts into one listing still per room. This listing still studio lays out the seller-supplied room names and layout lines as a listing still and property-page graphic. Use it for listing still sets, room listing stills, and property-page listing cards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External real estate sellers, listing teams, and their agents use this skill to plan and generate room-by-room listing stills from confirmed floor-plan notes. It supports free planning before billable Beatra image calls and returns the generated stills with task, model, dimension, and billing details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad shared Beatra account permissions beyond listing-image creation.

Mitigation: Review the Beatra approval page carefully and install only if those account-level permissions are acceptable.

Risk: Automatic package updates are enabled by default.

Mitigation: Use the documented update setting to disable automatic updates when change control is required.

Risk: Sensitive local files may be uploaded to Beatra-controlled upload infrastructure if selected as references.

Mitigation: Inspect local files first and upload only files the user explicitly intends to send to Beatra.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/real-estate-listing-set)
- [Beatra skill homepage](https://beatra.ai/skills/real-estate-listing-set)
- [Listing still workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Installation registration](artifact/references/installation-registration.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Bundled MCP Client diagnostics](artifact/references/mcp-connection.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads; generated stills are returned as image files or artifact references.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a free labeled room card list before billable image calls; billable work returns task IDs, resolved models, observed dimensions and formats, and billing.net_charged_credits.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
