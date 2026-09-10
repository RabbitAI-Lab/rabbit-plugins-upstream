## Description:

Turn user-supplied assignment names and points into a four-to-eight still lab cover set. This lab report cover studio lays out each named assignment as its own still. Use it for assignment covers, experiment covers, lab report stills, and a matching cover pack.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to turn confirmed assignment names and points into a coordinated set of lab report cover stills. The skill guides planning, approval, generation, task recovery, billing reporting, and delivery for one still per named assignment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared Beatra device credential with broad media and spending-related permissions.

Mitigation: Review the Beatra approval scopes before connecting, keep the credential private, and revoke the device authorization from the Beatra Console when the skill is no longer needed.

Risk: Silent package updates are enabled by default.

Mitigation: Consider disabling automatic updates immediately after installation with the bundled update control and use explicit update checks when reviewing changes.

Risk: Billable image generation can spend Beatra credits.

Mitigation: Require the production approval card before generation, use one opaque client_request_id per still, and retry only unchanged requests with the same identity after transport uncertainty.

Risk: Installation metadata is sent to Beatra.

Mitigation: Install only if that metadata sharing is acceptable for the deployment, and disconnect or uninstall the package when the workflow is complete.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/lab-cover-set)
- [Beatra Skill Homepage](https://beatra.ai/skills/lab-cover-set)
- [Lab cover pack workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [Beatra MCP endpoint](https://mcp.beatra.ai/mcp)
- [Beatra API origin](https://api.beatra.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and text guidance with JSON payload examples and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Beatra image-generation task references, returned artifact details, resolved model names, observed dimensions and formats, and billing.net_charged_credits when remote tasks complete.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
