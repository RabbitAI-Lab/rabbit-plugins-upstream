## Description:

Turn seller-supplied restock facts and an already-written restock script into one talking clip per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and their agents use this skill to plan and produce short restock announcement talking clips from authorized stills, confirmed restock facts, and already-written spoken lines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a broad shared Beatra device authorization and stores local credential state under ~/.beatra.

Mitigation: Install only if that authorization scope is acceptable, keep credential files private, and never expose the Device Token in chat, logs, command arguments, or copied files.

Risk: The workflow can upload selected user media to Beatra and may process likeness or voice material.

Mitigation: Inspect every asset first and require explicit likeness, voice, and media rights before upload, cloning, speech synthesis, or video generation.

Risk: The bundled client silently checks for and installs verified package updates unless automatic updates are disabled.

Mitigation: Use the documented update controls to disable automatic checks when silent updates are not acceptable, and rely only on verified official package updates.

Risk: Clone, speech, and video operations are paid stages where uncertain retries could duplicate work or charges.

Mitigation: Confirm each paid stage separately, read live pricing and balance before submission, and recover uncertain responses only with the same client_request_id and unchanged arguments.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/beatra-ai/skills/restock-drop-talking)
- [Beatra skill homepage](https://beatra.ai/skills/restock-drop-talking)
- [Restock talking workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Installation registration](artifact/references/installation-registration.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions, API Calls, Files]

**Output Format:** [Markdown guidance with shell commands and JSON MCP payloads; completed workflows may return generated media file artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paid clone, speech, and video stages require explicit confirmation, live price checks, and idempotent request IDs.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
