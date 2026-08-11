## Description:

基于 Alexa 提示词的亚马逊选品研究专家。适用于需要结合市场数据生成 Alexa 购物提示词、COSMO 关系提示词、战略选品问题、自动化执行和提示词驱动选品报告的场景。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers, product analysts, listing optimization specialists, and brand operators use this skill to generate data-grounded Alexa for Shopping prompts, run product research workflows, and produce selection insight reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release bundles broader LinkFox automation behavior than a narrow Alexa prompt helper, including account, billing, scheduling, upload, feedback, and cross-skill workflows.

Mitigation: Review the bundled workflows before installation and enable the skill only where those broader LinkFox behaviors are expected.

Risk: Endpoint override environment variables can redirect requests away from the expected service path.

Mitigation: Avoid setting endpoint override variables unless the destination is controlled and approved.

Risk: Upload and scheduling workflows can expose or repeatedly process sensitive content if used without clear intent.

Mitigation: Confirm content can be public before upload and avoid scheduling sensitive prompts or files unless explicitly intended.

Risk: Product research prompts and generated reports may influence commercial decisions based on incomplete or misleading source data.

Mitigation: Review market evidence, Alexa responses, and final reports before using recommendations for sourcing, listing, pricing, or brand decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-alexa-prompt-product-selection)
- [LinkFox Skills](https://skill.linkfox.com/)
- [Amazon Alexa Search API reference](skills/linkfox-amazon-alexa-search/references/api.md)
- [Amazon Product Detail API reference](skills/linkfox-amazon-product-detail/references/api.md)
- [AI Text Generation API reference](skills/linkfox-aigc-textgen/references/api.md)
- [Report Generator layout reference](skills/linkfox-report-generator/references/analysis-layouts.md)
- [Task Scheduler API reference](skills/linkfox-task-scheduler/references/api.md)
- [File Upload API reference](skills/linkfox-file-upload/references/api.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with structured prompt blocks, shell command examples, and generated HTML report files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are data-grounded product research prompts and report paths; full reports are written as HTML by the bundled report generator.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
