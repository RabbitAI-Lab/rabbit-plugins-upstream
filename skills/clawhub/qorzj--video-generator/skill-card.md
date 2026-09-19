## Description:

Creates AI-generated videos with dialogue and ambient sound from text, first and last frame images, or image, video, and audio reference materials through a cost-estimate and confirmation workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qorzj](https://clawhub.ai/user/qorzj)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to convert text prompts or approved media references into short generated MP4 videos with synchronized visuals, dialogue, soundscape, and music. It helps an agent gather required video settings, estimate credits, request explicit user confirmation, submit generation, and save the completed result locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected prompts and media are sent to Deep Code Plus, and local uploads are exposed through a public plaintext HTTP URL path.

Mitigation: Use only non-sensitive prompts and media unless the publisher moves uploads to HTTPS/private signed URLs with cleanup controls.

Risk: Dependencies are declared without exact pinned versions.

Mitigation: Install dependencies in an isolated environment and pin reviewed versions before deployment.

Risk: Video generation can consume platform credits and may take longer than the minimum estimate.

Mitigation: Keep the documented cost-estimate step and require explicit user confirmation of credits, duration, mode, and output path before submitting generation.

## Reference(s):

- [Video Prompt Writing Guide](references/video-prompt-writing-guide.md)
- [ClawHub Skill Page](https://clawhub.ai/qorzj/skills/video-generator)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Plain text or Markdown guidance with bash commands; script output is JSON and successful generation saves an MP4 file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user confirmation before paid generation and uses PLUS_API_KEY from local configuration for submission and status checks.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
