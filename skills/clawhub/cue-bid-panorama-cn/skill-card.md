## Description:

将一份中国招投标披露整理为八项带逐字引文和来源锚点的摘要卡，并标出缺失信息及需人工判断的结论。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

采购、投标与合规团队可用它核对单个工程项目招标及中标披露中的主体、时间、评标方式、金额、履约和异议渠道。它逐字保留引文与定位，不提供投标建议或中标预测。

### Deployment Geography for Use:

中国大陆

## Known Risks and Mitigations:

Risk: Sending confidential attachments to optional Cue parsing may expose document contents to an external provider.

Mitigation: Authorize external processing first and review the provider's terms; use supplied text when external processing is not approved.

Risk: A CUE_API_KEY may be exposed or sent to an unintended routing destination.

Mitigation: Keep the key out of chat and verify the routing destination before authenticating.

Risk: Live services and companion skills were not evaluated in the release security review.

Mitigation: Use reviewed, pinned installation sources and assess companion skills separately.

## Reference(s):

- [披露环节链与三要素记法](artifact/references/bid-chain.md)
- [招投标披露全景（ClawHub release）](https://clawhub.ai/huhoo/skills/cue-bid-panorama-cn)
- [Cue data channel configuration](https://cuecue.cn/hub/mcp)
- [Cue attachment parsing configuration](https://cuecue.cn/hub/omni-reader)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Five-section Markdown disclosure card]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Eight named items preserve source quotes and anchors; missing items are marked 未检索到 and judgment calls remain [待人工].]

## Skill Version(s):

0.1.2 (source: release evidence and CHANGELOG, released 2026-11-04)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
