## Description:

一键替换服装面料。版式图 + 面料图 → 换上新面料的样衣图，垂坠与光泽随材质变。当用户说「换面料」「换材质」「试布料」「面料上身」「同款不同料」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Fashion designers and apparel teams can preview how a garment style may look in different fabrics before making physical samples, using a garment reference image and a fabric swatch.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment or fabric images may be sent to external image-generation services, which could expose confidential designs.

Mitigation: Avoid submitting confidential designs unless external processing is acceptable, and review the chosen provider's data-handling terms.

Risk: ClawScan reports only 55.6% coverage, so some artifact behavior was only partially analyzed.

Mitigation: Review the skill before installing and use non-sensitive sample images while assessing it.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dlazyai/skills/fabric-on-body)
- [Provider CLI reference](references/provider-cli.md)
- [Model flags reference](references/model-flags.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, Prompt text, Shell commands]

**Output Format:** [Generated JPEG image previews with prompt text and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Visual previews only; they do not establish real fabric feel, weight, or sample quality.]

## Skill Version(s):

1.0.32 (source: SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
