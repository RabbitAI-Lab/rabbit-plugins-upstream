## Description:

Turn user-supplied public policy digest points into one policy digest still per page.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to convert user-confirmed public policy digest points into page-by-page still images, with a free page plan before billable Beatra image generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra device token with permissions beyond still-image generation.

Mitigation: Install only if the Beatra approval scope and account billing implications are acceptable; keep the token in the documented local credential file and do not expose it in chat, logs, arguments, or environment variables.

Risk: The bundled client silently self-updates package code by default.

Mitigation: Review the automatic update behavior before use and disable silent update checks with `python3 scripts/mcp_client.py update --auto off` when change control is required.

Risk: Billable generation requests can create duplicate charges if recovery is handled with changed inputs or a new request identity.

Mitigation: Use one opaque `client_request_id` per approved page, retry only identical payloads with the same request identity after uncertain delivery, and poll existing tasks before resubmitting.

Risk: Generated policy digest stills may contain unreadable or incorrect small text.

Mitigation: Review visible printed lines against the confirmed page list and treat unreadable small type as a review item, not as a certified official notice.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/policy-digest-set)
- [Beatra Skill Homepage](https://beatra.ai/skills/policy-digest-set)
- [Policy-Digest Workflow](references/workflow.md)
- [Installation and Authentication](references/installation-and-auth.md)
- [Installation Registration](references/installation-registration.md)
- [MCP Connection](references/mcp-connection.md)
- [Tasks and Results](references/tasks-and-results.md)
- [Billing, Errors, and Recovery](references/billing-errors-and-recovery.md)
- [Automatic Updates and Safety](references/automatic-updates-and-safety.md)
- [Uninstall and Disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown with inline shell commands, JSON payload examples, and generated image artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans one still per named page, uses one Beatra task per approved generation, and reports task IDs, resolved models, dimensions, formats, and net charged credits when returned.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
