## Description: <br>
Turns plain product shots or text briefs into studio, lifestyle, or hero product imagery guidance for e-commerce and advertising workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runware](https://clawhub.ai/user/runware) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creative operators, and commerce teams use this skill to route product-image requests through generation, cleanup, background removal, relighting, and brand-safe review steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Product images and prompts may be sent to external image-generation tools. <br>
Mitigation: Use the skill only with product assets and prompts that are acceptable to share with the selected provider. <br>
Risk: Generated imagery may alter brand details, product appearance, logos, claims, or on-pack text. <br>
Mitigation: Review outputs for brand accuracy and only render supplied text verbatim. <br>
Risk: Multi-stage generation, cutout, and relighting workflows may incur per-image costs. <br>
Mitigation: Check cost before batch runs and validate a single image before scaling. <br>


## Reference(s): <br>
- [Product Photography worked recipes](references/examples.md) <br>
- [Product Photography on ClawHub](https://clawhub.ai/runware/skills/product-photography) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON request examples and model-routing instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include staged image-generation, background-removal, relighting, color, aspect-ratio, seed, and cost-check guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
