## Description:

Turns a user's selfie into a satirical profile set with AI image prompts, a collage, and optional animated outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use the skill to turn their own or a consented selfie into satirical profile imagery and a shareable collage or video, using its command-line workflow or prompts in ChatGPT.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads a recognizable selfie and personal details to external services.

Mitigation: Use your own photo or get clear consent, and review the external services' privacy terms before uploading.

Risk: The animation workflow removes and recreates an existing `_frames` directory in its output folder.

Mitigation: Use a dedicated output folder or preserve any `_frames` contents you need before running animation.

Risk: Security analysis was incomplete because one script was only partially inspected.

Mitigation: Review the full script and skill files before running them.

## Reference(s):

- [Prompt pack](references/prompts.md)
- [VARG how-to](https://varg.ai/how-to)
- [ChatGPT animated GIF example](https://x.com/op7418/status/2118184315507118272)

## Skill Output:

**Output Type(s):** [Images, GIFs, Video, Markdown prompts, Python code]

**Output Format:** [PNG or JPG images, looping GIFs, MP4 video, Markdown prompts, and Python scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A 4:5 collage and optional presenter video can be assembled from the generated tiles.]

## Skill Version(s):

1.0.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
