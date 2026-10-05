## Description:

面向学术论文、深度长文和行业分析的多代理写作流程，涵盖资料检索、写作、审计、同行评审及发布渠道建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT

## Use Case:

研究人员、作者和分析师使用该技能组织长篇论文或行业分析的证据检索、起草、审计和同行评审，并在关键阶段确认方向与外部服务使用。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow creates or modifies multiple project files in the workspace.

Mitigation: Review the proposed project path and file list, and explicitly approve the work before it starts.

Risk: Research requests can send search terms and URLs to external services.

Mitigation: Choose the no-external-services path for sensitive topics and avoid including secrets in project materials.

Risk: Documentation inconsistencies may affect strict workflow reproducibility.

Mitigation: Review the workflow instructions and intermediate outputs when deterministic execution matters.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zuoyunlai/skills/lunheng-article-pipeline)
- [Quickstart](QUICKSTART.md)
- [Pipeline overview](references/_shared/真源/pipeline-overview.md)
- [External services and consent](references/_shared/真源/external-services.md)
- [Coordinator fallback protocol](references/_shared/真源/model_fallback_takeover_protocol.md)

## Skill Output:

**Output Type(s):** [Markdown, Text, Guidance]

**Output Format:** [Markdown documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces drafts, research notes, audit reports and a final long-form article in the workspace.]

## Skill Version(s):

2.15.10 (source: SKILL.md metadata and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
