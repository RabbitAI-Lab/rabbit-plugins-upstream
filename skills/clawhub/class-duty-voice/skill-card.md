## Description:

Turn a written class duty roster into one class duty voice clip per labeled cue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers and education staff use this skill to convert an existing class duty roster into 8 to 20 labeled roster reminder voice clips. The skill also guides optional staff voice cloning only when the user provides an authorized sample and consent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses broad Beatra account authority, including wallet spending, artifact and task access, non-speech generation scopes, and task cancellation.

Mitigation: Review before installation, especially in school or shared-device environments, and install only when that shared full-scope authority is acceptable.

Risk: A reusable Device Token is stored locally and shared by Beatra skill packages on the device.

Mitigation: Keep the local credential files private, avoid exposing tokens in chat, logs, arguments, or environment variables, and revoke the connected agent when access is no longer needed.

Risk: The bundled client sends installation metadata and checks for package updates silently by default.

Mitigation: Review the automatic update behavior before installing and disable silent checks with `python3 scripts/mcp_client.py update --auto off` when automatic updates are not acceptable.

Risk: Voice cloning can misuse likeness rights if a staff voice sample is only found rather than authorized.

Mitigation: Clone only from an inspected, authorized sample with explicit likeness and voice rights; file access alone is not consent.

Risk: Paid clone and speech tasks can create duplicate or unintended charges if retried incorrectly after transport uncertainty.

Mitigation: Use one opaque `client_request_id` per paid request, poll existing tasks for recovery, and retry only byte-identical arguments with the same request identity.

## Reference(s):

- [Class Duty Voice on ClawHub](https://clawhub.ai/beatra-ai/skills/class-duty-voice)
- [Beatra Class Duty Voice homepage](https://beatra.ai/skills/class-duty-voice)
- [Class duty voice workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with JSON payload examples, Beatra task and artifact references, and generated MP3 audio files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces 8 to 20 labeled voice clips from the supplied roster; clone and speech stages may spend Beatra wallet credits.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
