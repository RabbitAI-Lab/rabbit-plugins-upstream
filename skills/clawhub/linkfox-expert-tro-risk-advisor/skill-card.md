## Description:

跨境电商 POD TRO 与知识产权风险提示专家，适用于用户提供商品图片或文本后快速评估版权、商标、名人、品牌、体育、大学、宗教或平台侵权风险等级的场景。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and agents use this skill to triage POD and cross-border e-commerce listings for TRO and intellectual-property risk from product images and listing text. It provides a concise risk level, core risk points, and handling guidance, with optional deeper checks through specialized copyright, trademark, and patent tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, listing text, account or login data, API keys, and paid-search requests may be sent to LinkFox services.

Mitigation: Install and use only when that data sharing is acceptable; avoid sending private images or sensitive account data unless required for the task.

Risk: Uploaded local files can become publicly accessible URLs.

Mitigation: Upload only files intended for public access and review generated links before sharing them further.

Risk: Configurable LINKFOX_TOOL_GATEWAY and LINKFOX_*_API_URL endpoints can redirect requests to non-default services.

Mitigation: Keep endpoint override variables unset unless the destination is trusted and approved.

Risk: Local result and cache directories may retain analysis outputs or request artifacts.

Mitigation: Periodically review or delete local LinkFox result and cache directories according to data-retention needs.

Risk: The security verdict is suspicious because the workflow handles credentials, payments, public uploads, local retention, configurable endpoints, and automatic feedback reporting.

Mitigation: Review the skill and scan results before deployment, and limit use to environments where those behaviors are acceptable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-tro-risk-advisor)
- [Primary skill definition](artifact/SKILL.md)
- [AIGC text and image analysis API](artifact/skills/linkfox-aigc-textgen/references/api.md)
- [Copyright detection API](artifact/skills/linkfox-ruiguan-copyright-detection/references/api.md)
- [Graphic trademark detection API](artifact/skills/linkfox-ruiguan-trademark-graphic-detection/references/api.md)
- [Text trademark detection API](artifact/skills/linkfox-ruiguan-text-trademark-detection/references/api.md)
- [Design patent detection API](artifact/skills/linkfox-ruiguan-detection-patent-design/references/api.md)
- [Utility patent detection API](artifact/skills/linkfox-ruiguan-utility-patent-detection/references/api.md)
- [Patent image search API](artifact/skills/linkfox-zhihuiya-patent-image-search/references/api.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Concise Chinese Markdown-style risk assessment with fixed risk level, core risk points, and handling advice.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May request image URLs or listing text and may recommend specialized copyright, trademark, or patent checks.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
