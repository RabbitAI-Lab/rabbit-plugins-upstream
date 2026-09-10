## Description:

Beatra Universal helps agents create and manage AI images, videos, music, narration, reusable voices, and public social data lookups through Beatra.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route media creation, media editing, voice, upload, billing, task recovery, and public social lookup requests through Beatra while preserving paid-operation boundaries and returned task details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a broad persistent Beatra Device Token stored locally.

Mitigation: Authorize only when comfortable granting the connection, keep the credential private, and review credential-storage policy before use in enterprise or regulated environments.

Risk: Selected local media may be uploaded to Beatra for generation or editing.

Mitigation: Upload only intended files through the bundled upload command and confirm voice-owner permission before any voice cloning workflow.

Risk: Some operations consume Beatra credits.

Mitigation: Use live model, wallet, and ledger reads for estimates and charges, and require explicit approval before video generation, voice cloning, and other confirmation-gated paid work.

Risk: Installed code can silently self-update by default.

Mitigation: Disable automatic updates for lower-risk operation and rely on explicit verified package updates where review is required.

Risk: Installation and platform metadata may be reported automatically.

Mitigation: Review egress, telemetry, and installation metadata policy before deployment in sensitive environments.

## Reference(s):

- [Beatra Universal on ClawHub](https://clawhub.ai/beatra-ai/skills/beatra)
- [Beatra installation page](https://beatra.ai/install)
- [Installation and authentication](references/installation-and-auth.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Models](references/models.md)
- [Tasks and results](references/tasks-and-results.md)
- [Uploads](references/uploads.md)
- [Public social data](references/social.md)
- [Speech and voices](references/speech-and-voices.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Files, Guidance]

**Output Format:** [Markdown responses with command snippets, task status, returned artifact links or IDs, usage details, and JSON for public social results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated media files, narration audio, cloned voice identifiers, rewritten prompts, public social data, and billing or task metadata.]

## Skill Version(s):

2.8.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
