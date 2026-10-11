## Description:

Analyzes videos into a structured scene and dialogue index, visual observations, a fused timeline, and a narration brief for downstream agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

Video creators and agents use this skill to prepare timestamped scene, speech, and visual evidence for video summaries, indexing, and later narration planning. It produces an understanding brief rather than finished narration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video, extracted audio, frames, prompts, and background context are sent to the configured MiMo-compatible API provider.

Mitigation: Use only content approved for that provider and review its data-handling terms before enabling model calls.

Risk: Runs create, overwrite, or delete generated artifacts in the work directory; skipping ASR can replace an existing transcript with an empty one.

Mitigation: Use a dedicated work directory, preserve important outputs, and review options before rerunning.

Risk: Chinese-oriented prompts and outputs may not meet other language requirements by default.

Mitigation: Review language settings and generated analysis before using it downstream.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/worldwonderer/skills/video-understanding)
- [Data schema](artifact/references/data-schema.md)
- [Research guide](artifact/references/research-guide.md)
- [Prompt templates](artifact/references/prompt-templates.md)

## Skill Output:

**Output Type(s):** [Analysis, Files, Markdown]

**Output Format:** [JSON analysis files, storyboard images, and a Markdown narration brief]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes scene and dialogue timestamps; ASR timing is approximate, not word-aligned.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
