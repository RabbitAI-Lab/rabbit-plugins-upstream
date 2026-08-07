## Description:

电商知识产权与合规检测一站式 AI 工具集，整合睿观知产合规检测（版权/商标/外观专利/实用新型专利/图片政策）与智慧芽专利数据查询（著录/权利要求/说明书/附图/法律状态/家族/引用/以图搜图/PDF）共 2 类底层工具、22 项子能力。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce sellers, compliance analysts, and agent users use this skill to check product images and listing text for copyright, trademark, patent, TRO, policy, and patent-data risks before publication or review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send product images, listing text, patent identifiers, phone/login data during onboarding, and billing actions to LinkFox-related services.

Mitigation: Install and run it only when the user accepts that data transfer, and obtain explicit consent before using any feedback endpoint.

Risk: The LINKFOX_TOOL_GATEWAY environment variable can redirect tool traffic to another gateway.

Mitigation: Leave LINKFOX_TOOL_GATEWAY unset unless the destination is trusted and expected for the deployment.

Risk: Tool responses may be stored in local linkfox output directories, including fallback locations.

Mitigation: Run from a private writable project directory and review or remove local linkfox output directories after use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-ecommerce-compliance-detection)
- [Skill Source Overview](artifact/SKILL.md)
- [Onboarding Reference](artifact/references/onboarding.md)
- [Ruiguan Copyright Detection](artifact/references/linkfox-ruiguan-copyright-detection.md)
- [Ruiguan Graphic Trademark Detection](artifact/references/linkfox-ruiguan-trademark-graphic-detection.md)
- [Ruiguan Text Trademark Detection](artifact/references/linkfox-ruiguan-text-trademark-detection.md)
- [Ruiguan Design Patent Detection](artifact/references/linkfox-ruiguan-detection-patent-design.md)
- [Ruiguan Utility Patent Detection](artifact/references/linkfox-ruiguan-utility-patent-detection.md)
- [Ruiguan Image Policy Compliance Search](artifact/references/linkfox-ruiguan-gun-parts-search.md)
- [Zhihuiya Patent Image Search](artifact/references/linkfox-zhihuiya-patent-image-search.md)
- [Zhihuiya Utility Patent Image Search](artifact/references/linkfox-zhihuiya-utility-patent-image-search.md)
- [Zhihuiya Bibliography](artifact/references/linkfox-zhihuiya-bibliography.md)
- [Zhihuiya Patent Claims](artifact/references/linkfox-zhihuiya-claim-data.md)
- [Zhihuiya Legal Status](artifact/references/linkfox-zhihuiya-legal-status.md)
- [Zhihuiya Patent Family](artifact/references/linkfox-zhihuiya-patent-family.md)
- [Zhihuiya Patent Citations](artifact/references/linkfox-zhihuiya-patent-cited.md)
- [Zhihuiya Forward Citation](artifact/references/linkfox-zhihuiya-patent-forward-citation.md)
- [Zhihuiya PDF Data](artifact/references/linkfox-zhihuiya-pdf-data.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API responses and saved result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a LinkFox API key; tools may write response JSON under local linkfox output directories and may summarize large responses.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
