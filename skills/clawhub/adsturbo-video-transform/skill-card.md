## Description:

Transforms videos by replacing an on-screen person, animating a portrait from reference motion, or translating speech with lip sync.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to replace a video spokesperson, animate a portrait using a reference clip, or re-dub a video in another language.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User media is uploaded to publicly accessible third-party URLs and may contain personal, confidential, or regulated material.

Mitigation: Review before installation and upload only media authorized for public sharing with AdsTurbo.

Risk: Person-swap, portrait animation, and lip-sync translation can be used without the depicted person's consent.

Mitigation: Confirm authorization and consent before transforming a person's likeness or voice.

Risk: Unpinned Python dependencies can change between installations.

Mitigation: Consider a pinned dependency set in controlled environments.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/adsturbo/skills/adsturbo-video-transform)
- [Video transform reference](artifact/references/video_transform.md)
- [Media upload reference](artifact/references/upload.md)
- [Async task reference](artifact/references/work.md)
- [AdsTurbo API key portal](https://adsturbo.ai/iris/api)

## Skill Output:

**Output Type(s):** [Text, Guidance, Video links]

**Output Format:** [Markdown with a link to the transformed video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include an estimated processing time while an asynchronous task runs.]

## Skill Version(s):

1.2.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
