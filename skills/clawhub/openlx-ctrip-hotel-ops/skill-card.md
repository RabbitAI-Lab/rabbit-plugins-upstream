## Description:

为携程酒店、民宿商家执行经营体检、点评分流与回复、价格房态和订单提案、竞品分析及笔记内容生产；读取真实门店数据或用户导出，生成离线 HTML 报告，并通过独立 Chrome 和经实测的账户适配执行已授权动作。

This skill is ready for commercial/non-commercial use.

## Publisher:

[openlxcn](https://clawhub.ai/user/openlxcn)

### License/Terms of Use:

MIT-0

## Use Case:

External hotel, guesthouse, and homestay operators use this skill to inspect Ctrip operating data, prepare review replies, pricing and inventory proposals, competitor comparisons, content drafts, and local evidence-backed reports. Authorized account actions should be limited to verified mappings and confirmed policies.

### Deployment Geography for Use:

Global, for users operating supported Ctrip hotel accounts.

## Known Risks and Mitigations:

Risk: The skill can automate live Ctrip hotel-account actions and public content submission.

Mitigation: Use a dedicated workspace and isolated Chrome profile, verify account mappings, and require explicit authorization plus readback records before relying on pricing, publishing, review, or order actions.

Risk: A custom installer target can move an arbitrary directory if misused.

Mitigation: Use the default install target where possible; verify any custom --target path before running installation commands.

Risk: Sensitive guest, credential, or business data could be exposed to optional model endpoints.

Mitigation: Send only verified facts and necessary persona fields to model calls, and keep guest identities, credentials, cookies, raw pages, and unnecessary review text out of prompts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/openlxcn/skills/openlx-ctrip-hotel-ops)
- [Product Website](https://ctrip.openlx.cn)
- [Report Examples](https://ctrip.openlx.cn/reports)
- [Publication Status](https://ctrip.openlx.cn/status.json)
- [GitHub Release v0.1.1](https://github.com/openlxcn/openlx-ctrip-hotel-ops/releases/tag/v0.1.1)
- [Runtime and Account Adaptation](references/runtime.md)
- [Version Status](references/status.json)
- [Capability Matrix](references/capability-matrix.json)
- [Product Catalog](references/catalog.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance, shell commands, JSON workspace records, generated drafts, action ledgers, and offline HTML reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a dedicated local hotel workspace and isolated Chrome profile; live account actions require verified mappings, authorization, and readback records.]

## Skill Version(s):

0.1.1 (source: package.json and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
