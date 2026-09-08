## Description:

Turns a written census schedule into labeled spoken notice clips, producing a census notice voice pack from the office's supplied schedule.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents supporting a street office use this skill to turn an already written census schedule into a labeled 8 to 20 clip voice pack. It plans each cue from supplied text, then guides optional staff voice cloning and paid speech generation through Beatra when authorized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Beatra Device Token grants broad shared account-level access and is stored under ~/.beatra.

Mitigation: Install only in environments where that shared authorization is acceptable; keep the credential file private and use Beatra revocation or the bundled uninstall workflow when disconnecting.

Risk: The bundled client performs package telemetry and silent automatic update checks by default.

Mitigation: Review the update behavior before use in sensitive environments and disable silent updates with python3 scripts/mcp_client.py update --auto off when required.

Risk: Voice cloning and speech generation can upload selected voice samples and spend Beatra credits.

Mitigation: Use only authorized voice samples, confirm each paid clone or speech stage before submission, and report live pricing and billing fields from Beatra rather than remembered estimates.

Risk: Retrying changed or uncertain paid requests can create duplicate work or charges.

Mitigation: Reuse the same client_request_id only for byte-identical retries, poll existing task IDs before replay, and create a new request identity whenever generation inputs change.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/census-notice-voice)
- [Beatra skill homepage](https://beatra.ai/skills/census-notice-voice)
- [Census notice voice workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API calls, Files, Guidance]

**Output Format:** [Markdown planning text with JSON payload examples, shell commands, Beatra task results, and generated audio file references.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces 8 to 20 MP3 speech clips when paid Beatra speech tasks complete; optional voice cloning can produce a reusable voice_id.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
