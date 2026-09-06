## Description:

Turn a written class duty roster into one class duty voice clip per labeled cue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers and education staff use this skill to turn an existing class duty roster into labeled spoken reminder clips. It helps plan 8 to 20 roster cues, confirm live Beatra costs, and produce voice clips with a catalog voice or an authorized cloned staff voice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests a shared Beatra device credential with broad media, wallet, task, artifact, and voice permissions.

Mitigation: Review the requested authority before installing and only authorize the Beatra connection when that level of access is acceptable.

Risk: The bundled client silently updates package files by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when silent replacement is not acceptable.

Risk: Voice cloning can misuse voice samples without clear rights or consent.

Mitigation: Upload voice samples only when explicit rights and consent for the sample are available.

## Reference(s):

- [Class Duty Voice Pack on ClawHub](https://clawhub.ai/beatra-ai/skills/class-duty-voice)
- [Beatra Class Duty Voice Pack](https://beatra.ai/skills/class-duty-voice)
- [Class duty voice workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with JSON payload examples, shell commands, and generated audio artifact references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a labeled slot list and normally 8 to 20 class duty voice clips; paid Beatra operations use live pricing and explicit request identities.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
