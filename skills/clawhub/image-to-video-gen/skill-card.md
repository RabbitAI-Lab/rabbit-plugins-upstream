## Description:

Generates videos from supplied images by using Gemini Vision to analyze the image and Google's Veo 3.0 async API to create an MP4 video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and media creators use this skill to turn an input image into a short cinematic MP4 video. It is suited for agent-assisted media generation workflows that can use Google API access and local workspace outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images and generated prompt text are sent to Google APIs, and source and output files are stored in the OpenClaw workspace.

Mitigation: Use only imagery permitted by your policies, avoid sensitive or regulated content unless approved, and review local output files before sharing or retaining them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j3ffyang/skills/image-to-video-gen)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown with inline Python and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GOOGLE_API_KEY and may save the input image, Gemini analysis, enhanced prompt text, API response JSON, and MP4 video under ~/.openclaw/workspace/tibetanProc/.]

## Skill Version(s):

3.0.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
