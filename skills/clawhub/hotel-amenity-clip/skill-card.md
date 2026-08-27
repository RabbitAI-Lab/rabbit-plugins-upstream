## Description:

Turn hotel amenity stills the property already took into one hotel amenity video per labeled still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External hotel sellers, property teams, and their agents use this skill to turn already supplied and named amenity photos into one short video clip per still, after a visible shot list and price confirmation step.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected hotel amenity images are uploaded to Beatra for generation.

Mitigation: Use only images the property supplied for this amenity set and avoid including sensitive or unrelated material.

Risk: The shared Beatra Device Token grants broad account authority and can spend credits across several media tools.

Mitigation: Keep the token in the local credential file only, confirm live price and request count before paid calls, and revoke the connection in the Beatra Console when it is no longer needed.

Risk: The bundled client silently self-updates unless automatic updates are disabled.

Mitigation: Review the update behavior before installation and disable automatic updates with `python3 scripts/mcp_client.py update --auto off` if silent updates are not acceptable.

Risk: Billable video generation can consume credits, and unsafe retry handling can duplicate work.

Mitigation: Use one opaque `client_request_id` per approved still, retry only byte-identical arguments with the same ID, and report actual charged credits from terminal task billing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/hotel-amenity-clip)
- [Beatra Skill Homepage](https://beatra.ai/skills/hotel-amenity-clip)
- [Hotel Amenity Clip Workflow](references/workflow.md)
- [Installation and Authentication](references/installation-and-auth.md)
- [Billing, Errors, and Recovery](references/billing-errors-and-recovery.md)
- [Tasks and Results](references/tasks-and-results.md)
- [Bundled MCP Client Diagnostics](references/mcp-connection.md)
- [Automatic Updates and Safety](references/automatic-updates-and-safety.md)
- [Uninstall and Disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, API Calls, Files]

**Output Format:** [Markdown guidance with shell command and JSON payload blocks; generated video artifacts are returned through Beatra tasks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a free shot list before billable generation; one video task is submitted per labeled amenity still after user confirmation.]

## Skill Version(s):

0.1.1 (source: server release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
