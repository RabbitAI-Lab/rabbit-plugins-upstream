## Description:

Creates short product videos from product photos, using storyboards and product references to preserve packaging details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce teams and marketers use the skill to turn one to three product photos into short social or listing videos, with the packaging and label checked against the source photos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos and related details are sent to an external service for processing.

Mitigation: Tell users which service will process the images, get approval, and avoid confidential or personal images unless its data handling is acceptable.

Risk: AI-generated shots may alter packaging, labels, or product behavior and could misrepresent the item.

Mitigation: Check labels and product details against the source photos, composite the real packshot where needed, and remove unsupported product claims.

Risk: The installer is reported as unpinned and the security scan was partial.

Mitigation: Review the release source and version before installation, and treat the scan as incomplete.

## Reference(s):

- [Product photo to video guide](https://varg.ai/how-to/turn-a-product-photo-into-a-video)
- [Prompt templates](references/prompts.md)
- [Common failures and fixes](references/failures.md)
- [OpenAI image prompting cookbook](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

## Skill Output:

**Output Type(s):** [Video files, Guidance, Shell commands]

**Output Format:** [MP4 video, typically 9:16; 1:1 or 16:9 formats are also described]

**Output Parameters:** [One product video, typically 10–15 seconds]

**Other Properties Related to Output:** [A storyboard may be produced during the workflow; final framing and resolution depend on the requested format.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
