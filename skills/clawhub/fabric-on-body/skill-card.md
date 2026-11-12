## Description:

一键替换服装面料。版式图 + 面料图 → 换上新面料的样衣图，垂坠与光泽随材质变。当用户说「换面料」「换材质」「试布料」「面料上身」「同款不同料」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Fashion designers and e-commerce teams use this skill to preview how a garment pattern may look in a selected fabric before physical sampling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts and images to external image-generation providers.

Mitigation: Before use, review the selected provider's data handling and decide whether you are comfortable sending the images and prompts to that service.

Risk: The security scan was partial, so some code behavior remains unverified.

Mitigation: Consider waiting for a more complete review if unverified behavior is a concern.

## Reference(s):

- [Provider and CLI reference](references/provider-cli.md)
- [Image model flags](references/model-flags.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, Files]

**Output Format:** [Generated garment preview image files (JPEG, PNG, or WebP)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Visual preview only; it does not represent a physical sample or guarantee fabric hand-feel or weight.]

## Skill Version(s):

1.0.31 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
