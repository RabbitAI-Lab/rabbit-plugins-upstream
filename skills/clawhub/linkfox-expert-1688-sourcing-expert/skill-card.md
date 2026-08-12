## Description:

面向亚马逊卖家的 1688 找货源与利润分析专家。适用于用户提供 ASIN 后，需要匹配 1688 供应商、以图验证货源、核算 FBA 成本，或按预期净利润对货源排序的场景。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers use this skill to start from an ASIN, find candidate 1688 suppliers, verify product similarity, calculate FBA-based cost and profit, and rank sourcing options by expected monthly net profit. It is designed for US Amazon FBA sourcing workflows and requires an ASIN as input.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: The skill uses LinkFox API keys and external services for sourcing and product research.

Mitigation: Install only when LinkFox is trusted, scope API keys appropriately, and avoid overriding LinkFox gateway environment variables unless the endpoint is controlled.

Risk: The workflow may send ASINs, product research, local files, phone/SMS login details, or paid-plan onboarding data to external services.

Mitigation: Use non-sensitive inputs where possible, share one-time codes only when intentionally completing onboarding, and do not upload private files.

Risk: Generated reports and selected files can be saved locally or published through public URLs.

Mitigation: Review generated artifacts before sharing and upload only files that are intended to be public.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-1688-sourcing-expert)
- [ClawHub publisher profile](https://clawhub.ai/user/linkfox-ai)
- [1688 source profiler workflow](skills/linkfox-1688-source-profiler/SKILL.md)
- [AIGC prompt templates](skills/linkfox-1688-source-profiler/references/aigc-prompt-templates.md)
- [FBA fee table](skills/linkfox-1688-source-profiler/references/fba-fee-table.md)
- [Report generator layouts](skills/linkfox-report-generator/references/analysis-layouts.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Concise chat responses, saved JSON data, shell command invocations, and generated HTML report paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Long reports are generated as local HTML files; selected files may be uploaded to public URLs when requested.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
