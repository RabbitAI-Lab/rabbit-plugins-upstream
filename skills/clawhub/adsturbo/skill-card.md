## Description:

Helps creators combine AdsTurbo's AI spokesperson, video, ad-cloning, image, and editing capabilities into multi-step creative workflows using an AdsTurbo API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketers use this skill to chain AdsTurbo media tasks, such as recreating an authorized ad, adding a spokesperson, and translating the result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploading private or third-party images, audio, and video may expose sensitive material, including through public links.

Mitigation: Upload only media you have rights and consent to use; avoid confidential or regulated material and treat shared links as potentially exposed.

Risk: Cloning voices or likenesses and removing watermarks can misuse others' identity or creative work.

Mitigation: Obtain consent and rights for portraits, voices, ads, and branded assets; review the intended use before generating or altering media.

Risk: An AdsTurbo API key can submit paid jobs, and draft submissions may charge credits.

Mitigation: Keep the key private and manually confirm the quoted price before submitting a draft or repeating a paid request.

Risk: Deleting a remote persona may remove the wrong account asset.

Mitigation: Verify the exact actor ID and intended persona before deletion.

## Reference(s):

- [AdsTurbo skill release](https://clawhub.ai/adsturbo/skills/adsturbo)
- [AdsTurbo API key](https://adsturbo.ai/iris/api)
- [AdsTurbo pricing](https://adsturbo.ai/pricing)
- [Ad cloning guide](artifact/references/ad_clone.md)
- [Digital human guide](artifact/references/digital_human.md)
- [Asset upload guide](artifact/references/upload.md)

## Skill Output:

**Output Type(s):** [Text, Media links, Guidance]

**Output Format:** [Markdown with links to generated media]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media jobs may consume credits and return links after processing.]

## Skill Version(s):

1.2.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
