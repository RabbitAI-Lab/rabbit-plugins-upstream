## Description:

Turn user-supplied unit outline points into one still per unit mind map page.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Educators, instructional designers, and agents assisting them use this skill to turn user-confirmed unit or lesson points into page-by-page classroom mind-map stills, with a free page list before paid image generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports broad shared Beatra account access covering media, wallet, artifact, and task permissions.

Mitigation: Install only in accounts where Beatra credit spending and artifact access are intended, and review the authorization before use.

Risk: The security evidence reports silent package self-updates.

Mitigation: Disable automatic updates with `scripts/mcp_client.py update --auto off` when the environment requires manual update review.

Risk: Billable image generation can spend credits and retry mistakes can create duplicate work.

Mitigation: Confirm the live model price before submitting, keep one request identity per approved page, and retry only unchanged payloads after transport uncertainty.

## Reference(s):

- [Unit Map Page on ClawHub](https://clawhub.ai/beatra-ai/skills/unit-map-set)
- [Unit-map workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown guidance plus generated image artifacts, task IDs, model details, and billing details when returned]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One generated still per confirmed page; retries and corrections use distinct request identity rules.]

## Skill Version(s):

0.1.2 (source: server release and manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
