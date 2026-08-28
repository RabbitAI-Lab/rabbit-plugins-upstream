## Description:

Use when someone wants light instrumental background music - an ambient bed under dialogue or underscore for reels and explainers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to guide an agent through generating light instrumental background music with the Replicate-hosted stability-ai/stable-audio-2.5 model.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and generation settings are sent to Replicate, and use may consume paid API credits.

Mitigation: Confirm the Replicate API token, review prompt content before requests, and verify expected cost or credit usage before generation.

Risk: The skill depends on local ffmpeg and ffprobe availability for the mix step.

Mitigation: Verify ffmpeg and ffprobe are installed and on PATH before using the generated audio in a mix workflow.

Risk: Recommended prerequisite skills are not included in this artifact.

Mitigation: Review and install the referenced Pruna prerequisite skills separately before following their guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/stable-audio-2-5)
- [Replicate Stable Audio 2.5 predictions endpoint](https://api.replicate.com/v1/models/stability-ai/stable-audio-2.5/predictions)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with inline bash and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides prompt, duration, generation settings, polling, MP3 download, and ffmpeg-based mix preparation.]

## Skill Version(s):

1.0.10 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
