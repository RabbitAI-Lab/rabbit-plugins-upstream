## Description:

帮助电商运营人员生成单变量商品主图 A/B 对照方案、记录测试假设，并提供合规检查和转化复盘模板。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

电商运营人员和商家使用此技能规划商品主图的单变量 A/B 测试，生成对照图片、事先记录假设，并在自行收集平台数据后复盘点击和转化表现。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Listing prompts and reference product images are sent to the selected cloud image provider.

Mitigation: Review the selected provider and its credential settings, inspect the request with --dry-run, and avoid confidential or unreleased images unless the provider policy permits them.

Risk: The example brand configuration may introduce an inaccurate model or visual description into generated listings.

Mitigation: Customize examples/brand.yaml for the actual brand and product before generation.

Risk: Generated images may fail platform requirements or produce misleading experimental conclusions when sample sizes are small.

Mitigation: Review current platform rules and each image before publishing; record hypotheses before testing and wait for adequate exposure before drawing conclusions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/listing-optimizer)
- [Platform image specifications](references/platform-specs.md)
- [Image provider usage and data flow](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown experiment plan, generation and compliance commands, and fill-in review table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provider execution can create image files; platform performance data must be supplied by the user.]

## Skill Version(s):

1.0.20 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
