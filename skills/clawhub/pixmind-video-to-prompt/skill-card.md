## Description:

Extract a SaaS-style storyboard with local reference frames, timestamps, scripts, scene descriptions, and recreation prompts from one local video or remote URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fuyunzhishang](https://clawhub.ai/user/fuyunzhishang)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze a single local video or remote video URL, receive a structured storyboard with reference frames, and turn scenes into recreation prompts or shot-list material.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected videos are sent to Pixmind and the analysis consumes Pixmind credits.

Mitigation: Confirm the video source, output language, requested scene limit, billing rule, and any duration-based credit estimate before starting a paid submission.

Risk: FFmpeg resolution can be affected by custom paths, manifests, cache directories, or the Windows-only automatic download path.

Mitigation: Prefer a trusted FFmpeg binary through --ffmpeg or PIXMIND_FFMPEG_PATH, and avoid setting PIXMIND_API_BASE, PIXMIND_FFMPEG_MANIFEST, or PIXMIND_CACHE_DIR to untrusted locations.

## Reference(s):

- [Pixmind Video to Prompt on ClawHub](https://clawhub.ai/fuyunzhishang/skills/pixmind-video-to-prompt)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [JSON stdout with storyboard data, local JPEG attachments, and a Markdown table fallback.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PIXMIND_API_KEY; paid Pixmind analysis requires explicit approval and local screenshots are extracted with FFmpeg.]

## Skill Version(s):

1.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
