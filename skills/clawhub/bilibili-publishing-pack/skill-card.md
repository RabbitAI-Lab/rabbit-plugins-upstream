## Description:

Create Bilibili upload copy from a video topic, title, outline, or finished script, including title options, a description, chapter timestamps when supplied, tags, a pinned-comment prompt, a thumbnail brief, and one matching landscape 16:9 thumbnail.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and publishing teams use this skill to turn a Bilibili video topic, outline, or script into Simplified Chinese upload copy, including title options, a primary title, description, tags, chapter text when timestamps are supplied, a pinned comment, and a thumbnail brief. After the copy is settled, the skill can prepare and, with explicit paid approval, request one matching 16:9 thumbnail.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared Beatra device connection with broad account capabilities for remote tools.

Mitigation: Install only when that account-level access is acceptable, keep the credential in the documented user-only file, and avoid generic tool or upload commands outside the approved thumbnail workflow.

Risk: The package includes local upload capability and generic remote tool access that exceed the narrow publishing-copy use case.

Mitigation: Use the bundled workflow boundaries: do not upload local files, do not call unrelated tools, and keep thumbnail generation to the documented text-to-image path after explicit approval.

Risk: Silent automatic updates are enabled by default.

Mitigation: Disable automatic updates with the documented command before use if release changes require review before execution.

Risk: Billable thumbnail generation can create charges if submitted more than once or without a frozen plan.

Mitigation: Show the paid plan, price estimate, and stable client_request_id before approval, then submit exactly one generation request and recover uncertain responses with the same request identity.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/bilibili-publishing-pack)
- [Beatra skill homepage](https://beatra.ai/skills/bilibili-publishing-pack)
- [Bilibili publishing workflow](references/workflow.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Bundled MCP Client diagnostics](references/mcp-connection.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with structured publishing copy, command examples, and thumbnail task result details when generation is approved]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default copy is Simplified Chinese; thumbnail generation is a separate paid step requiring explicit approval.]

## Skill Version(s):

0.1.5 (source: evidence.release.version and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
