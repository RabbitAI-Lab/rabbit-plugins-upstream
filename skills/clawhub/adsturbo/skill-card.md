## Description:

Helps creators combine AdsTurbo's AI video, digital human, image, ad cloning, and media editing tools in end-to-end creative workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to generate and edit advertising images and videos, create digital-human narration, and chain media tasks into complete campaigns using an AdsTurbo API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, faces, voices, and other media are sent to AdsTurbo; local uploads may become publicly accessible URLs.

Mitigation: Upload only material approved for this service and public URL access; keep the API key private.

Risk: Watermark removal, ad cloning, and identity or voice manipulation can misuse someone else's content or likeness.

Mitigation: Use only media, likenesses, voices, logos, subtitles, and watermarks you own or are authorized to modify.

Risk: Generation and draft submission can spend account credits without adequate confirmation.

Mitigation: Check current pricing and obtain explicit approval of the quote before submitting a billed task; query timed-out tasks instead of resubmitting.

## Reference(s):

- [AdsTurbo skill on ClawHub](https://clawhub.ai/adsturbo/skills/adsturbo)
- [Digital human guide](references/digital_human.md)
- [Video generation guide](references/video_generation.md)
- [Ad cloning guide](references/ad_clone.md)
- [Video enhancement guide](references/video_enhance.md)
- [Video transformation guide](references/video_transform.md)
- [Image creation guide](references/image.md)
- [Asset upload guide](references/upload.md)
- [Task status and retry guide](references/work.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Media result links]

**Output Format:** [Markdown text with links to generated or edited media and task status updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some media tasks run asynchronously; API usage consumes account credits.]

## Skill Version(s):

1.2.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
