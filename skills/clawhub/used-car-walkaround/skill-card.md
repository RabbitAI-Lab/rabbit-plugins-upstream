## Description:

Turn one used-car condition sheet into a listing hero still and a speakable walkaround script, then turn that still into one used car walkaround clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External used-car dealers and inventory teams use this skill to turn a dealer-supplied condition sheet for one named vehicle into a listing hero still, a speakable walkaround script, and an approved walkaround clip.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation grants a shared Beatra device token with broader account capabilities than this single used-car workflow needs.

Mitigation: Review the authorization before installation, keep the token only in the documented local credential file, and revoke access from the Beatra Console or uninstall when the skill is no longer needed.

Risk: Executable package files silently self-update by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when explicit review is required before running newer package code.

Risk: Condition sheets and optional listing photos may contain data the user does not want sent to Beatra.

Mitigation: Submit only vehicle facts and images intended for Beatra processing, and leave sensitive or unrelated data out of the condition sheet and uploaded photos.

Risk: Paid image, speech, and video generation can create duplicate charges if uncertain requests are replayed with changed arguments.

Mitigation: Use the documented approval cards, live prices, and opaque `client_request_id` values; retry uncertain paid work only with byte-identical arguments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/used-car-walkaround)
- [Beatra skill homepage](https://beatra.ai/skills/used-car-walkaround)
- [Used-car walkaround workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Bundled MCP Client diagnostics](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command blocks and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a listing still plan, a speakable script, approval cards, and Beatra task/result handling; approved remote calls produce media artifacts through Beatra.]

## Skill Version(s):

0.1.1 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
