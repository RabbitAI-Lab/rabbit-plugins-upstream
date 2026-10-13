## Description:

帮助电商运营人员设计单变量商品主图 A/B 实验，生成对照图片和实验假设，并提供后续转化复盘模板。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

电商运营人员利用此技能规划商品主图的单变量 A/B 测试，生成候选图片并记录预先设定的假设；投放后自行填入曝光、点击和转化数据进行复盘。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and brand guidance may be sent to an external image-generation provider.

Mitigation: Inspect requests with --dry-run, explicitly choose an approved provider, and avoid sensitive unreleased assets unless provider policy permits them.

Risk: Automated image compliance checks can miss platform requirements or change as platform rules evolve.

Mitigation: Treat checks as preflight aids and confirm current platform requirements before publishing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/listing-optimizer)
- [Platform image specifications](artifact/references/platform-specs.md)
- [Image provider and data-flow reference](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Image files]

**Output Format:** [Markdown experiment plan and review table, generation commands, and JPEG image variants]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Metrics must be supplied by the user; compliance checks are preliminary, not platform approval.]

## Skill Version(s):

1.0.16 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
