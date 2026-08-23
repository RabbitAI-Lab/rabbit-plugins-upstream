## Description:

Generate one short directed transition from an approved first frame to an approved last frame, turning two images into one clip that begins and ends on those images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to plan and submit a single first-frame-to-last-frame video transition for transformations, product reveals, before-and-after stories, scene changes, and cinematic endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra device authorization with broad media and spending-related authority and stores the token under ~/.beatra.

Mitigation: Install only when that account access is acceptable, keep ~/.beatra private, avoid exposing tokens in logs or prompts, and revoke or disconnect access when the skill is no longer needed.

Risk: The workflow can upload selected local media to Beatra for generation.

Mitigation: Inspect endpoint images before upload and avoid submitting private or sensitive media unless the user has approved that transfer.

Risk: Video generation is paid work and may consume Beatra credits.

Mitigation: Show the admission card and require explicit top-up or balance confirmation before submission; recover uncertain paid calls with the same client request identity.

Risk: Package-owned automatic updates are enabled by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when manual change control is required.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/first-last-frame-video)
- [Beatra Skill Page](https://beatra.ai/skills/first-last-frame-video)
- [First-and-last-frame workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON MCP call payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one transition workflow per run, including admission guidance, task polling guidance, returned video artifacts or links, billing facts, and result review notes.]

## Skill Version(s):

0.1.4 (source: release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
