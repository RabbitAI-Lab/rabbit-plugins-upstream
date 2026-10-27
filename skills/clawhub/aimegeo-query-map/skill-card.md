## Description:

把产品介绍、用户问题与已有文章整理成GEO问题和选题地图，明确受众、意图、事实资料和优先次序。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xxjrq](https://clawhub.ai/user/xxjrq)

### License/Terms of Use:

MIT-0

## Use Case:

内容策划人员和业务团队可用此技能，将产品资料、用户问题与现有文章整理成GEO问题地图和优先选题，并标出事实缺项与内容覆盖情况。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reports may retain supplied article text and answer records.

Mitigation: Store reports with access and retention controls appropriate for the material.

Risk: An optional aimeGeo handoff may send material to external services or prepare content for publishing.

Mitigation: Review what will be sent and approve the final content and destination accounts before publishing.

## Reference(s):

- [Input contract](references/input-contract.md)
- [Delivery check](references/delivery-check.md)
- [aimeGeo on GitHub](https://github.com/xxjrq/aimegeo)
- [aimeGeo website](https://geo.aimmme.com/)
- [aimeGeo on Gitee](https://gitee.com/xxjrq/aimegeo)

## Skill Output:

**Output Type(s):** [CSV files, Markdown, Guidance]

**Output Format:** [A question-to-topic CSV mapping and a Markdown weekly topic plan]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves question IDs, sources, coverage evidence, missing facts, and prioritization rationale when supplied.]

## Skill Version(s):

1.0.1 (source: server release evidence, artifact/manifest.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
