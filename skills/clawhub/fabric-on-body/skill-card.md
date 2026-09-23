## Description:

一键替换服装面料。版式图 + 面料图 → 换上新面料的样衣图，垂坠与光泽随材质变。当用户说「换面料」「换材质」「试布料」「面料上身」「同款不同料」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce and fashion users use this skill to generate visual previews of a garment pattern rendered in a different fabric before physical sampling. Developers and agents can use it to prepare prompts, provider settings, and shell commands for fabric-on-garment image generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment photos, fabric references, prompts, and design details may be sent to dLazy or another configured cloud image provider.

Mitigation: Use --dry-run before execution, choose the provider deliberately, and avoid uploading confidential or customer-identifying images unless the selected account and data policy allow it.

Risk: Generated outputs are visual previews and may not represent real fabric hand feel, weight, construction feasibility, or exact production behavior.

Mitigation: Treat generated images as pre-sampling references and validate final materials through normal physical sampling and production review.

Risk: Poor source images or weak prompts can shift the garment silhouette, color, texture, or construction details.

Mitigation: Use clear garment and fabric references, neutral lighting, fabric-specific physical descriptors, and explicit prompt constraints that preserve cut, length, seams, camera angle, and construction details.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/fabric-on-body)
- [Provider CLI Reference](references/provider-cli.md)
- [gpt-image-2 Parameters](references/model-flags.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with bash commands and generated JPEG image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses garment reference images, fabric reference images, prompts, provider credentials, and save paths; generated images are visual previews rather than physical fabric samples.]

## Skill Version(s):

1.0.12 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
