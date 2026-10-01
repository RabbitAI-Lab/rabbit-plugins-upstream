## Description:

Generates confirmed knowledge-card drafts and vertical educational poster images from a user-provided topic.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaodbb](https://clawhub.ai/user/zhaodbb)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and knowledge-sharing teams use this skill to research a topic, review a structured Chinese-first content draft, and generate a 1080x1920 educational poster image after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated outputs may be uploaded to a public CDN, which can expose confidential, personal, regulated, or rights-sensitive material.

Mitigation: Use only non-sensitive content unless the publisher adds consent and access controls for uploads.

Risk: The workflow includes under-disclosed public sharing and a non-refusal instruction for sensitive or copyright-related image requests.

Mitigation: Review requests against applicable policy and decline or adapt unsafe or rights-sensitive content before image generation.

Risk: Persistent user-added styles may alter future image-generation behavior.

Mitigation: Constrain new style definitions to reviewed visual-only changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaodbb/skills/knowledge-card-generator)
- [Draft template](artifact/references/draft-template.md)
- [Style guide](artifact/references/style-guide.md)
- [Base image prompt](artifact/assets/prompts/base_prompt.md)
- [Childlike style prompt](artifact/assets/prompts/style_prompts/childlike.txt)

## Skill Output:

**Output Type(s):** [Text, Markdown, Image prompts, Images, Guidance]

**Output Format:** [Markdown draft plus image-generation prompt and PNG output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces 9:16, 1080x1920 vertical poster images after user draft confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
