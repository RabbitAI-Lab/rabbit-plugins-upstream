## Description:

腾讯地图 JavaScript GL（JSAPIGL）开发指南，帮助 agents 编写、审查和调试地图初始化、覆盖物、图层、事件、控件、可视化、检索、路线规划、地理编码、行政区划、IP 定位、几何计算和 3D 模型相关代码。

This skill is ready for commercial/non-commercial use.

## Publisher:

[tencent-adm](https://clawhub.ai/user/tencent-adm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to answer Tencent Map JSAPI GL questions and produce implementation guidance grounded in bundled API documentation and demo code. It is suited for building and troubleshooting web map features that use Tencent Map keys and optional visualization libraries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The no-key flow can ask the assistant to handle a phone number, SMS code, temporary tokens, and Tencent Map key values during account-linked provisioning.

Mitigation: Prefer setting TMAP_JSAPI_KEY manually; use the no-key flow only after reviewing the Tencent agreements and accepting that account-linked values may pass through the conversation.

Risk: The temporary-key flow can store phone-linked key data locally in plaintext under ~/.tencentmap/tempkey.json.

Mitigation: Avoid the temporary-key flow on shared machines, remove the local file when it is no longer needed, or provide a pre-created key through the environment instead.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tencent-adm/skills/tencentmap-webservice-skill)
- [Tencent Map JSAPI GL overview](https://lbs.qq.com/webApi/javascriptGL/glGuide/glOverview)
- [Skill entry and workflow](artifact/SKILL.md)
- [Tencent Map API reference](artifact/tencentmap-jsapi-gl-skill/references/api_reference.md)
- [JSAPI GL documentation](artifact/tencentmap-jsapi-gl-skill/references/jsapigl/docs/)
- [Visualization documentation](artifact/tencentmap-jsapi-gl-skill/references/visualization/docs/)
- [Temporary key guide](artifact/tencentmap-jsapi-gl-skill/tempkey-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with code snippets, command examples, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference TMAP_JSAPI_KEY and Tencent Map temporary-key setup when a user lacks an API key.]

## Skill Version(s):

1.0.4 (source: server release metadata; artifact frontmatter reports 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
