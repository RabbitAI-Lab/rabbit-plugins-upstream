## Description:

Creates illustrated story reels with narration or music, using picture-book frames and gentle pan-and-zoom or optional generated motion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to plan and produce illustrated slideshow stories with voiceover or music, review each stage, and assemble a finished video reel.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and generated media are sent to external Pruna or Replicate services.

Mitigation: Use only intended API keys and review sensitive content before submitting prompts or media.

Risk: Paid generation may incur costs, and final assembly can overwrite an existing MP4.

Mitigation: Observe the plan, still, audio and optional clip approval gates; confirm a safe output directory before assembly.

Risk: Installing dependencies from an untrusted source can introduce unwanted behavior.

Mitigation: Confirm the Pruna AI skill source and prefer pinned or preapproved dependencies.

## Reference(s):

- [Illustrated Story Reel on ClawHub](https://clawhub.ai/pruna-ai/skills/illustrated-story-reel)
- [Workflow and approval gates](artifact/references/illustrated-story-reel-gates.md)
- [API reference](artifact/references/illustrated-story-reel-api.md)
- [Quality gates](artifact/references/illustrated-story-reel-quality.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown beat plans, JSON story plans, and shell commands for media generation and assembly]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces reviewed stills, audio, optional motion clips, and an assembled MP4 reel.]

## Skill Version(s):

1.0.14 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
