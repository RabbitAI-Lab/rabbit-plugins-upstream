## Description:

Helps short-drama and manga-drama production teams turn scripts, character and scene assets, episode goals, budget, and schedule into batch production plans, shot tasks, AI-HIVE generation commands, continuity checks, and delivery records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External content teams, studios, marketers, and developers use this skill to plan and operate batch short-drama or manga-drama production workflows. It produces production briefs, reusable asset tables, shot-level generation tasks, quality checklists, and runnable commands for AI-HIVE image, video, and deterministic video-editing helpers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an AI-HIVE API key and can upload selected media assets to AI-HIVE.

Mitigation: Use environment variables or the 0600 local config path for credentials, keep keys out of chats and logs, and upload only media the user is authorized to process.

Risk: Image and video generation can be billable and may run in batches.

Mitigation: Review prompts, routing mode, model settings, and pricing snapshots before submission; start with a sample episode or shot before scaling batch work.

Risk: Short-drama production may accidentally copy protected expression or imply unsupported endorsements, product claims, or testimonials.

Mitigation: Require authorization for reference materials, keep only abstract structure from references when rights are unclear, and avoid false claims, impersonation, or fabricated testimonials.

Risk: Generated production guidance can become stale when model availability, pricing, platform rules, or business facts change.

Mitigation: Query current model configuration and pricing before generation, label externally provided business claims by source, and route uncertain claims to human review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/short-drama-batch-production-ai-hive)
- [AI-HIVE chat and API access](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown with structured checklists, JSON-oriented production briefs, and inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include local JSON blueprints and downloaded media outputs when the user runs the provided scripts.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
