## Description:

Use when someone wants the same person hosting several clips - multi-segment UGC, comparison reels, or mixed speaking and animated scenes with continuity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and developers use this skill to plan and generate coherent multi-scene avatar or motion-transfer reels with consistent cast identity, approved stills, Pruna video calls, slider comparisons, and ffmpeg assembly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads portraits, scripts, motion templates, and related media to Pruna services.

Mitigation: Confirm the user trusts the PrunaAI skill dependencies and has rights to upload all selected media before generation.

Risk: ffmpeg examples use overwrite behavior that can replace existing output files.

Mitigation: Use unique output filenames or remove the overwrite flag when preserving prior renders matters.

Risk: Poor pose, framing, or proportion alignment between reference images and motion templates can produce weak motion-transfer clips.

Mitigation: Review alignment before running paid video jobs, repose references with p-image-edit, or choose a closer motion template.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/avatar-multi-scene)
- [Animate beats guide](artifact/animate-beats.md)
- [Prompt templates](artifact/prompt-templates.md)
- [Examples](artifact/examples.md)
- [Batch template](artifact/templates/batch.template.json)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with JSON manifests, API call fields, and ffmpeg command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include scene plans, cast ledgers, prompt templates, Pruna request payload fields, file paths, comparison-render commands, and assembly instructions.]

## Skill Version(s):

1.0.10 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
