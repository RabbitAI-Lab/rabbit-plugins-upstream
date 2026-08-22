## Description:

Extract a SaaS-style storyboard with local reference frames, timestamps, scripts, scene descriptions, and recreation prompts from one local video or remote URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fuyunzhishang](https://clawhub.ai/user/fuyunzhishang)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to convert a local video or remote video URL into a storyboard with timestamps, scene descriptions, reference frames, and recreation prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Analyzing a local video uploads the selected file to Pixmind and consumes paid credits after approval.

Mitigation: Require explicit approval before submission, state the 100 credits per started minute billing rule, and resume existing task IDs instead of creating duplicate paid tasks.

Risk: The Pixmind API key is required for submissions and should not be exposed in chat.

Mitigation: Configure PIXMIND_API_KEY in the environment or provider settings and avoid requesting or displaying the key in conversation.

Risk: On Windows x64, FFmpeg may be downloaded automatically when no local executable is available.

Mitigation: Review the auto-download behavior in restricted environments or provide an approved FFmpeg path with --ffmpeg or PIXMIND_FFMPEG_PATH.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fuyunzhishang/skills/pixmind-video-to-prompt)
- [Pixmind API endpoint](https://aihub-admin.aimix.pro)
- [Pixmind FFmpeg manifest](https://cdn.pixmind.io/pixmind-builder/dependencies/ffmpeg/windows/x64/manifest.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files]

**Output Format:** [JSON result with presentation data, local image attachments, and a Markdown storyboard table fallback]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PIXMIND_API_KEY, explicit approval before paid submission, one video source per request, and a maximum of 100 scenes.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
