## Description:

Turn already-written short sleep stories into one spoken clip per labeled story. This sleep story voice studio records each short sleep-story voice from the pages the producer already wrote. Use it for sleep stories, bedtime story reads, bedtime narration, and short sleep-story voice packs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External producers use this skill to turn already-written short sleep stories into labeled spoken clips for import into a player. It supports catalog or authorized cloned voices while requiring live cost checks and explicit approval before paid clone or speech stages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a shared local Beatra credential with spending-capable media permissions.

Mitigation: Install only when that access is acceptable, keep the credential private, and revoke the Beatra device from the console when the skill is no longer needed.

Risk: The bundled client can silently update executable package files.

Mitigation: Use the documented auto-update control to turn automatic updates off when review is required before code changes.

Risk: Voice cloning can create rights and consent risk if a sample is merely accessible but not authorized.

Mitigation: Use cloning only with clear rights to the voice sample and inspect the authorized sample before upload.

Risk: Paid clone and speech calls can consume Beatra credits.

Mitigation: Read live cost cards, get explicit approval for each paid stage, use opaque request IDs, and avoid retrying until recovery guidance confirms the same request can be reused.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/sleep-story-voice)
- [Beatra skill homepage](https://beatra.ai/skills/sleep-story-voice)
- [Sleep story workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Bundled MCP Client diagnostics](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands, JSON payload examples, task results, audio metadata, and billing summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce one remote spoken audio clip per labeled story; final media is retrieved through Beatra task results.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
