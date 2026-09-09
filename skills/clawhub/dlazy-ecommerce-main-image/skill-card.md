## Description:

Generates and edits ecommerce main-image candidates from approved product photos, with guidance for white-background baselines, visual-difference images, content-commerce scenes, color SKU sets, and single-variable A/B test variants.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, marketplace operators, and creative teams use this skill to prepare dLazy CLI prompts and commands for product main images, SKU color sets, and controlled A/B image tests. The skill emphasizes preserving product facts, avoiding unsupported claims, and checking current channel rules before publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow relies on a third-party npm CLI and hosted dLazy API.

Mitigation: Use a normal non-admin account, prefer per-command or revocable API keys where practical, and consider a contained workspace when supply-chain risk is a concern.

Risk: Product images and prompts may be uploaded to dLazy services during generation.

Mitigation: Upload only product images the user is allowed to send to dLazy, and avoid including confidential or unauthorized assets.

Risk: Generated ecommerce images can misstate product facts, add unsupported claims, or violate channel rules if prompts are too loose.

Mitigation: Use approved product photos, explicitly preserve SKU details, exclude unsupported claims and platform marks, and check current marketplace rules before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-main-image)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples and JSON CLI output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces prompts, checklists, and dLazy banana-pro command patterns for image-generation workflows.]

## Skill Version(s):

1.0.6 (source: server release evidence; artifact frontmatter says 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
