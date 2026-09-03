## Description:

Use when someone wants a multi-part story with voiceover: episodic B-roll, chaptered promo, or several linked video scenes without on-camera dialogue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creative operators and developers use this skill to plan and generate multi-scene narrated videos, coordinating story structure, still images, narration, video clips, review gates, and final assembly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can upload user-provided frames or narration and may consume paid generation credits.

Mitigation: Use the required approval gates before still, audio, and video generation, and confirm inputs before starting paid jobs.

Risk: Audio-led clips may truncate narration if a scene line exceeds the video API duration cap.

Mitigation: Run the documented ffprobe duration check and keep each scene narration around 19 seconds or less before video generation.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces scene plans, approval checkpoints, media-generation inputs, duration checks, and ffmpeg assembly commands.]

## Skill Version(s):

1.0.10 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
