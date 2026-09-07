## Description:

Turn one used-car condition sheet into a listing hero still and a speakable walkaround script, then turn that still into one used car walkaround clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External used-car dealers and listing operators use this skill to turn a supplied condition sheet for one named vehicle into a reusable listing still, walkaround script, speech track, and short walkaround clip.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a broad Beatra bearer token under `~/.beatra`.

Mitigation: Install only when broad Beatra account access is acceptable, keep credential files user-only, and revoke the Beatra device authorization when access is no longer needed.

Risk: Silent package self-updates are enabled by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when review-before-update is required.

Risk: Selected media files may be uploaded to Beatra-provided destinations.

Mitigation: Use the workflow only with non-sensitive upload files and inspect optional listing photos before upload.

Risk: Vehicle mileage, accident, or maintenance claims could be misstated if the agent fills gaps.

Mitigation: Copy these facts only from the supplied condition sheet, leave missing facts as named gaps, and review visible and spoken claims against the condition sheet before delivery.

Risk: Billable image, speech, or video calls could be duplicated during retry or recovery.

Mitigation: Use one opaque `client_request_id` per approved paid slot, retry only byte-identical arguments with the same identity, and poll or list tasks before replaying uncertain work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/used-car-walkaround)
- [Beatra skill homepage](https://beatra.ai/skills/used-car-walkaround)
- [Used-car walkaround workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Bundled MCP Client diagnostics](artifact/references/mcp-connection.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, code]

**Output Format:** [Markdown guidance with shell commands and JSON request payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent instructions for planning, approval, Beatra MCP calls, polling, recovery, delivery, authorization, update control, and uninstall behavior.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
