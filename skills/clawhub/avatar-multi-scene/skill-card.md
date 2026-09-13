## Description:

Use when someone wants the same person hosting several clips - multi-segment UGC, comparison reels, or mixed speaking and animated scenes with continuity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and developers use this skill to plan and generate coherent multi-scene avatar videos, UGC reels, comparison demos, and mixed speaking or motion-transfer segments with a consistent host identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned npx install commands can resolve mutable external package or skill content.

Mitigation: Use trusted PrunaAI sources, prefer pinned CLI versions or immutable references, inspect installs before using -y, and limit the runtime environment to the credentials and media required for the project.

Risk: The workflow can spend generation credits or process user media before the requester has confirmed scope, cast, rights, and scene plan.

Mitigation: Follow the documented approve plan, approve stills, and approve clips gates before uploads, predictions, video generation, or final assembly.

Risk: Motion-transfer rows can produce poor or misleading clips when source videos and reference stills have mismatched pose, scale, facing direction, or limb visibility.

Mitigation: Perform the documented pre-flight alignment check, repose near-matches with p-image-edit, and choose closer motion templates before running p-video-animate.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/pruna-ai/skills/avatar-multi-scene)
- [Prompt templates](artifact/prompt-templates.md)
- [Animate beats in multi-scene reels](artifact/animate-beats.md)
- [Examples](artifact/examples.md)
- [Batch template](artifact/templates/batch.template.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON snippets and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides staged approval, Pruna media generation, ffmpeg slider rendering, and final video assembly; generated media depends on approved inputs and external Pruna services.]

## Skill Version(s):

1.0.12 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
