## Description:

Use when someone wants the same person hosting several clips - multi-segment UGC, comparison reels, or mixed speaking and animated scenes with continuity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative operators use this skill to plan and generate coherent multi-scene avatar reels, combining talking-head clips, motion-transfer scenes, comparison sliders, and final ffmpeg assembly while preserving character continuity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Floating install commands can resolve changing third-party tooling.

Mitigation: Install only from trusted PrunaAI skill sources and prefer pinned or verified tooling where possible.

Risk: Reference images, scripts, approved stills, and generated clips may be saved locally or uploaded to Pruna services during generation.

Mitigation: Confirm rights, sensitivity, and user approval before uploading media or running generation.

Risk: Poor motion-template alignment or repeated scene framing can produce weak or misleading avatar and comparison clips.

Mitigation: Use the skill's approval gates, slop checks, and motion-template alignment review before video generation.

## Reference(s):

- [avatar-multi-scene on ClawHub](https://clawhub.ai/pruna-ai/skills/avatar-multi-scene)
- [Prompt templates](artifact/prompt-templates.md)
- [Animate beats](artifact/animate-beats.md)
- [Examples](artifact/examples.md)
- [Batch template](artifact/templates/batch.template.json)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration, Shell commands]

**Output Format:** [Markdown guidance with JSON templates and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses staged approval gates for planning, stills, clips, and assembly before generation proceeds.]

## Skill Version(s):

1.0.13 (source: evidence release.version and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
