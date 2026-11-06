## Description:

Turns a selfie into a satirical set of AI-generated profile images, animated tiles, and a shareable collage, with optional video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

For people who want to create a satirical, shareable profile set from their own selfie or a photo they have permission to use. It supports image generation through varg or applying the included prompts in ChatGPT.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Animation rendering may delete an existing `_frames` folder and its contents.

Mitigation: Use a fresh, dedicated output folder for animation rendering and check the cleanup target before running it.

Risk: The photo and personal prompt details are sent for external processing, and image URLs remain in local logs; provider retention was not verified.

Mitigation: Use only a photo you own or have permission to use, review provider terms, and protect local run logs.

Risk: Generation incurs credits and depends on external packages whose behavior was not verified.

Mitigation: Check the dry-run cost and review installer and dependency versions before generating.

## Reference(s):

- [Prompt collection and source links](artifact/references/prompts.md)
- [varg how-to guide](https://varg.ai/how-to)
- [ClawHub release page](https://clawhub.ai/vargai/skills/make-a-woke-profile-with-chatgpt)

## Skill Output:

**Output Type(s):** [Images, Animated GIFs, Video, Shell commands, Guidance]

**Output Format:** [PNG and JPEG images, GIF animations, MP4 video, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces 11 themed image tiles and a 4:5 collage, with optional animations and presenter video.]

## Skill Version(s):

1.0.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
