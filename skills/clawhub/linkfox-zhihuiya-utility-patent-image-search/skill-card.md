## Description:

Supports image-based similarity search for utility model patents using Zhihuiya/PatSnap data, including URL-based search, optional local image upload, result summarization, and authentication or billing guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to compare a product image against utility model patent images, prioritize similar patents by score, and support prior-art or infringement-risk review before consulting a patent professional.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent-search images and local image files may be sent to LinkFox services and local images may be uploaded to a public URL.

Mitigation: Use only images that are acceptable to share with LinkFox and avoid confidential unreleased product images unless that exposure is approved.

Risk: The skill handles API keys, phone-based onboarding, and paid credit purchase flows.

Mitigation: Review shell configuration changes, protect API keys, and confirm credit costs before running additional searches or billing commands.

Risk: Search responses and summaries can be saved persistently in the workspace.

Mitigation: Review generated linkfox files before sharing the workspace and remove sensitive result logs when they are no longer needed.

Risk: Patent image similarity scores can support review but are not legal determinations.

Mitigation: Treat results as triage evidence and consult a qualified patent professional before making infringement or freedom-to-operate decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-utility-patent-image-search)
- [Zhihuiya patent image search API reference](artifact/references/api.md)
- [Authentication and billing onboarding guide](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API parameters, shell commands, and saved JSON result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write full API responses and cache files under a local linkfox directory; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
