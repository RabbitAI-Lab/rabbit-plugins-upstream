## Description:

Generates publication-ready infographics by analyzing content, recommending layout and style, expanding prompts when needed, and ranking generated images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn textual or structured requests into professional infographics. It supports prompt evaluation, prompt expansion, image generation rounds, and quality-ranked results for visual summaries and data explanations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Infographic requests and generated images may be processed through the configured sn-image-base model services.

Mitigation: Avoid submitting secrets or confidential business data unless the configured Sensenova or internal model service is approved for that data.

Risk: Inferred layout or style choices may be unsuitable for brand-sensitive or culturally specific material.

Mitigation: Specify required style, brand, or cultural representation constraints explicitly in the user request.

Risk: Generated infographics can contain inaccurate, misleading, or poorly ranked visual content.

Mitigation: Review generated images and verbose quality rankings before publication or external use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sensenova-skills/skills/sn-infographic)
- [Analysis framework](references/analysis-framework.md)
- [Runtime parameters](references/runtime-parameters.md)
- [Evaluation standard](references/evaluation-standard.md)
- [Layout and style selection rules](references/layout-style-selection.md)
- [Prompt expansion system prompt](references/prompts-expand-system.md)
- [Prompt critic system prompt](references/prompts-critic-system.md)

## Skill Output:

**Output Type(s):** [Text, Images, JSON, Guidance]

**Output Format:** [Text summary with generated image output; verbose mode includes Markdown-style ranking and timing details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Friendly mode returns the top-ranked image; verbose mode returns all generated images ordered by quality. Generation rounds are bounded by max_rounds from 1 to 8.]

## Skill Version(s):

2026.8.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
