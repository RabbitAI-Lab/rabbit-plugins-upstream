## Description:

Turns seller-supplied sales voicemail scripts into one spoken voicemail clip per labeled slot.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and sales teams use this skill to turn already-written voicemail copy into a reviewed slot list and generated spoken voicemail clips for phone or dialer workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared Beatra device authorization with broad media, voice, wallet, task, and artifact permissions.

Mitigation: Install only when those permissions are acceptable, keep the credential in the private Beatra credential file, and revoke the device from the Beatra Console or uninstall flow when access is no longer wanted.

Risk: Automatic package updates are enabled by default.

Mitigation: Review the update behavior before use and run `python3 scripts/mcp_client.py update --auto off` when silent updates are not acceptable.

Risk: Clone and speech generation are paid operations and duplicate submissions can create duplicate work or charges.

Mitigation: Use the documented approval cards and unique request IDs, then recover uncertain requests with the same `client_request_id` and byte-identical arguments.

Risk: Voice cloning can misuse a person's likeness if consent is not verified.

Mitigation: Confirm the sample is authorized by the voice owner before cloning and do not treat file access as consent.

## Reference(s):

- [Sales voicemail workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/sales-voicemail-pack)
- [Beatra skill homepage](https://beatra.ai/skills/sales-voicemail-pack)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with command examples and JSON payloads; generated speech tasks return MP3 audio artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a free labeled slot list before paid generation; typical packs contain 8 to 20 voicemail clips.]

## Skill Version(s):

0.1.1 (source: manifest.json and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
