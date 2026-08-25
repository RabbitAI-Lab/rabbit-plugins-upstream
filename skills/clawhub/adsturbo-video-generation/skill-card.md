## Description:

Create video from scratch: text-to-video, image-to-video, first/last-frame interpolation, multi-reference generation, plus extending and locally editing existing videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate videos from prompts, public image or media URLs, first and last frames, or multiple reference assets, and to extend or locally edit existing videos through AdsTurbo workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-selected local media uploaded through the workflow is sent to AdsTurbo and converted into public URLs.

Mitigation: Upload only media that is appropriate to share with AdsTurbo and safe to expose through public URLs.

Risk: Overriding the default AdsTurbo base URL can send API keys and media workflow data to an unintended endpoint.

Mitigation: Use the default base URL unless a trusted AdsTurbo-compatible endpoint is explicitly required.

Risk: Dependencies are declared with a minimum version only, which can reduce reproducibility.

Mitigation: Pin dependencies in deployment environments that require stricter reproducibility.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/adsturbo/skills/adsturbo-video-generation)
- [Video Generation](references/video_generation.md)
- [Upload](references/upload.md)
- [Work Status](references/work.md)
- [AdsTurbo](https://www.adsturbo.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and concise user-facing status or result text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AdsTurbo result URLs, workspace IDs, polling guidance, and configuration notes for API keys or public media URLs.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
