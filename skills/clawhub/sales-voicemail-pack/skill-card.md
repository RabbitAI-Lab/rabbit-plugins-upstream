## Description:

Turns seller-supplied sales voicemail scripts into one spoken voicemail clip per labeled slot for voicemail drops, callback messages, after-hours greetings, and follow-up voicemail reads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and sales teams use this skill to plan labeled voicemail slots from supplied copy and generate spoken MP3 clips through Beatra speech tools, with optional cloned voice handling when rights are confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects the device to Beatra with a shared bearer token and broad account scopes.

Mitigation: Review authorization behavior before installing, keep credentials local, and revoke the device from Beatra when access is no longer desired.

Risk: The skill can spend credits for speech generation and optional voice cloning.

Mitigation: Require the documented confirmation card before each paid stage, use live pricing and balance reads, and retry uncertain paid requests only with the same request identity and unchanged arguments.

Risk: The skill can upload authorized voice samples for cloning.

Mitigation: Confirm voice and likeness rights before upload, inspect the intended sample, and upload only through the bundled Beatra client.

Risk: The bundled client silently checks for and installs package updates by default.

Mitigation: Consider disabling automatic updates with the documented update --auto off command when silent package replacement is not acceptable.

Risk: Uninstall may revoke or delete shared Beatra state when the package believes it is the last Beatra skill.

Mitigation: Use the bundled uninstall workflow and review its decision output before deleting package files or assuming shared access has been revoked.

## Reference(s):

- [Sales voicemail workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/sales-voicemail-pack)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON payload examples and shell command snippets; task results may reference generated MP3 audio artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires seller-provided voicemail copy; paid clone and speech work uses separate request identities and live Beatra task results.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
