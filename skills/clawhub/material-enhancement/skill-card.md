## Description:

材质质感增强与纹理重建。糊掉的图 + 高清商品图 → 纹理清晰可信的图。当用户说「增强质感」「图糊了」「补纹理」「提清晰度」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Fashion e-commerce image editors use this skill to restore fabric texture in an on-model product photo using a high-resolution reference of the same item, while preserving the model, garment shape and color, framing, and background.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports possible external image transmission without a privacy notice.

Mitigation: Confirm the selected provider and its data handling terms, and submit only images approved for external processing.

Risk: The scan is incomplete and reports a mismatch between the promised enhancement and behavior shown in the inspected material.

Mitigation: Review the skill and its scripts, then verify the result on non-sensitive images before relying on it.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/material-enhancement)
- [Model flags reference](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image files, Guidance, Shell commands]

**Output Format:** [Edited image files (JPEG, PNG, or WebP) with prompt and command examples in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an on-model image and a high-resolution reference of the same item; intended to improve fabric surface detail while preserving composition, garment shape, and color.]

## Skill Version(s):

1.0.33 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
