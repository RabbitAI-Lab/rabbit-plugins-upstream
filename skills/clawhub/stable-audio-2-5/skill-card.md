## Description:

Helps an agent generate light instrumental background music, such as ambient beds under dialogue or underscore for reels and explainers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and content teams use this skill to guide agents through creating short instrumental music beds with Replicate's stability-ai/stable-audio-2.5 model, including prompt intake, generation settings, polling, download, and mix preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned third-party prerequisite installs with automatic confirmation can change behavior without review.

Mitigation: Review the external skills and installer first, prefer pinned versions or verified commits, and install only the specific prerequisite skills needed.

Risk: Credential exposure could occur if REPLICATE_API_TOKEN is available while running unreviewed installers or helper commands.

Mitigation: Keep REPLICATE_API_TOKEN out of the environment during installation and expose it only when making the intended Replicate API request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/stable-audio-2-5)
- [Replicate Stable Audio 2.5 predictions endpoint](https://api.replicate.com/v1/models/stability-ai/stable-audio-2.5/predictions)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration instructions]

**Output Format:** [Markdown with inline bash and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides prompt, duration, steps, cfg_scale, optional seed, polling, MP3 download, and ffmpeg-based mix preparation.]

## Skill Version(s):

1.0.12 (source: release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
