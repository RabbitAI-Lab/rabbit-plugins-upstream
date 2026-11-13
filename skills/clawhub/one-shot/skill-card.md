## Description:

根据用户指令替换已有模特图中的模特和/或背景，并尽量保持商品本身不变。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

电商运营人员可用此技能从已有模特图或人台图生成替换模特、替换背景或两者都替换的商品图版本，以覆盖不同人群和场景。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source photos may contain identifiable faces or confidential product imagery, and the security scan reports incomplete analysis.

Mitigation: Before uploading images, verify which provider will receive them and its data handling, and authorize that transfer. Use another option if you cannot verify the intended tool access and data handling.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dlazyai/skills/one-shot)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [Model flags reference](artifact/references/model-flags.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Guidance]

**Output Format:** [JPEG image files and Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates image variants from supplied photos; review garment details, alignment, hands, and lighting in the results.]

## Skill Version(s):

1.0.31 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
