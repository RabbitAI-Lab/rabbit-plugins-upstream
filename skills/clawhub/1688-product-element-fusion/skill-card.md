## Description:

Extracts creative elements from inspiration images or video frames, searches 1688 for real products in a user-specified category using element keywords, researches matched products, and generates practical product concept-image variants.

This skill is ready for commercial/non-commercial use.

## Publisher:

[1688aiinfra](https://clawhub.ai/user/1688aiinfra)

### License/Terms of Use:

MIT-0

## Use Case:

External product designers, sourcing teams, and commerce operators use this skill to turn visual inspiration into product-search keywords, 1688 candidate products, grounded fusion plans, and concept-image variants for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package includes unrelated executable 1688/DingTalk template code.

Mitigation: Review and remove or document unrelated executable paths before installation or release.

Risk: The package can read shared credentials from another skill's configuration.

Mitigation: Avoid shared credential fallbacks and require explicit, scoped credentials for this skill.

Risk: CLI usage telemetry may be reported without clear user-facing disclosure.

Mitigation: Clearly disclose telemetry behavior or disable it by default before deployment.

Risk: Generated images, prompts, source links, and element JSON may persist as local files.

Mitigation: Treat these artifacts as retained user data and define review, storage, and deletion practices.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/1688aiinfra/skills/1688-product-element-fusion)
- [Creative Element Six-Dimension Model](references/element-model.md)
- [Fusion Prompt Template and Variant Strategy](references/fusion-prompt.md)
- [Element Fusion Examples](references/examples.md)
- [Skill Usage Telemetry Notes](references/skill埋点说明.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance, Image generation prompts, Images]

**Output Format:** [Markdown guidance, structured JSON element cards, image-generation prompts, and generated concept images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses human review checkpoints, qualitative cost descriptions, copyright prompts, and legal disclaimers before final concept output.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
