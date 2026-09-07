## Description:

Turn a written shift handoff checklist into one shift handoff voice clip per labeled cue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External operators and desk teams use this skill to turn an existing written shift-handoff checklist into a labeled voice pack. It plans 8 to 20 cue clips, can use a catalog or authorized cloned voice, and submits speech generation through Beatra after user-visible cost confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared Beatra device credential with broad account capabilities.

Mitigation: Install only for trusted Beatra work, keep ~/.beatra private, and revoke or reauthorize the device when account access should change.

Risk: The bundled client can dispatch arbitrary Beatra MCP tools using the shared credential.

Mitigation: Review the planned tool calls and cost cards before execution, and submit paid clone or speech requests only after user confirmation.

Risk: Silent package updates are enabled by default and can replace executable package files.

Mitigation: For sensitive environments, disable automatic updates with python3 scripts/mcp_client.py update --auto off and review updates before running them.

Risk: The package may send stable installation, platform, and device attribution to Beatra.

Mitigation: Review the local ~/.beatra state and the installation-registration behavior before deploying where device attribution is sensitive.

Risk: Voice cloning can create likeness and consent concerns if a staff sample is used without authorization.

Mitigation: Use cloned voices only after confirming likeness and voice rights, and treat file access alone as insufficient consent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/shift-handoff-voice)
- [Beatra skill homepage](https://beatra.ai/skills/shift-handoff-voice)
- [Shift handoff voice workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples; generated audio artifacts are returned through Beatra task results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans a free labeled slot list before paid clone or speech calls; typical speech output is one MP3 clip per shift-handoff cue.]

## Skill Version(s):

0.1.2 (source: server release evidence, manifest, bundled script constants)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
