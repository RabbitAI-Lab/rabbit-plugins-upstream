## Description:

中越翻译质量提升工作流（南宁市悦迅翻译有限公司 · 回译派 · 15 年中越实战）。以「反思回译法」10 阶段为父方法，叠加中越专项检查清单、假一致加固、可选回译前接地三层工程加固。专攻越南语翻译 QA、双模型反思流水线、回译派课程落地。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yanaiwen-star](https://clawhub.ai/user/yanaiwen-star)

### License/Terms of Use:

MIT-0

## Use Case:

External users and translation teams use this skill to improve Chinese-Vietnamese translation quality with terminology extraction, model-separated translation and back-translation, Vietnamese-specific QA checks, and human delivery gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confidential, legal, or customer-sensitive translation text may be exposed to selected models or public terminology search.

Mitigation: Use approved private models and search sources, redact sensitive text where possible, and confirm authorization before processing regulated or customer data.

Risk: Back-translation can falsely agree with the source when the target-language text is unnatural or pragmatically wrong.

Mitigation: Use separate models for translation and blind back-translation, then add target-language native self-checks, the Chinese-Vietnamese QA checklist, and human delivery review.

Risk: Single-model fallback can hide translation errors because the same model may repeat or normalize its own mistakes.

Mitigation: Label single-model outputs as not cross-model validated and require stronger human review before delivery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yanaiwen-star/skills/back-translate-reflect)
- [Publisher profile](https://clawhub.ai/user/yanaiwen-star)
- [Server-resolved GitHub source](https://github.com/yanaiwen-star/back-translate-reflect)
- [Yuexun Translation](https://yuexunfanyi.com)
- [DUAL-REFLECT paper](https://arxiv.org/abs/2406.07232)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance, configuration]

**Output Format:** [Markdown guidance with prompt templates, QA checklists, and structured JSON examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workflow expects separate models for forward translation, reflection, and blind back-translation when available.]

## Skill Version(s):

0.1.0 (source: server release evidence; artifact frontmatter states 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
