## Description: <br>
Helps agents produce high-quality AI image prompt packages for reference-guided image generation, product photography, portrait realism, e-commerce visuals, style matching, and safer prompt rewrites. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aolio516125-spec](https://clawhub.ai/user/aolio516125-spec) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, designers, marketers, and e-commerce teams use this skill to turn product, portrait, model, style, and reference-image requirements into complete Chinese and English prompt bundles. It is intended for commercial image-prompt drafting with human review for consent, policy, and platform-safety concerns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can encourage rewriting blocked sensitive image requests so generation platforms are more likely to accept them. <br>
Mitigation: Use it only for clearly allowed commercial product or apparel prompting, and do not use it to recover prompts that a platform has already refused. <br>
Risk: Reference-guided person or model prompting can affect likeness, consent, and identity rights. <br>
Mitigation: Require explicit consent for real-person likeness matching and avoid underage, sexualized, or otherwise sensitive contexts. <br>
Risk: Broad triggers and policy-rewrite guidance may increase misuse risk in image-generation workflows. <br>
Mitigation: Review the policy-rewrite behavior before installation and consider removing broad triggers or policy-evasion rewrite references before deployment. <br>


## Reference(s): <br>
- [Brand Tone Map](references/brand-tone-map.md) <br>
- [E-commerce Deliverables Guide](references/ecommerce-deliverables.md) <br>
- [E-commerce Product Polish System](references/ecommerce-product-polish-system.md) <br>
- [Natural Human System](references/natural-human-system.md) <br>
- [Platform-Safe Generation Rewrite Rules](references/policy-safe-generation.md) <br>
- [Portrait Realism System](references/portrait-realism-system.md) <br>
- [Prompt Output Package](references/prompt-output-package.md) <br>
- [Prompt Quality System](references/prompt-quality-system.md) <br>
- [Reference Fidelity System](references/reference-fidelity-system.md) <br>
- [Spatial Control](references/spatial-control.md) <br>
- [Shopify Product Photography Guide](https://www.shopify.com/au/blog/12206313-the-ultimate-diy-guide-to-beautiful-product-photography) <br>
- [Amazon Main Image Guidance](https://sell.amazon.com/blog/amazon-image-requirements) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown prompt package with optional structured JSON] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Chinese and English prompts, negative prompts, fidelity notes, safety rewrites, generation notes, quality checks, assumptions, and task-specific prompt sections.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
