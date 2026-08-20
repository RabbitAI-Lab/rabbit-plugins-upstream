## Description:

青虎AI 抖音爆款视频跟卖与铺货：从抖音关键词视频数据和热搜榜发现正在起量的带货视频，转换短链拿到正式链接与视频数据，用 1688 以图搜款采集同款货源，再经晓风 ERP 选模板一键铺货到抖店，打通「爆款发现-链接采集-极速上架」链路。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External commerce operators and agents use this skill to identify rising Douyin product videos, find matching 1688 supply, select Xiaofeng ERP distribution templates, and distribute listings to Douyin stores after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Qinghu API tokens and commerce account workflows.

Mitigation: Confirm the user is comfortable granting token access and use environment variables or explicit user-provided credentials only.

Risk: Product distribution can change store listings and may use the wrong account, template, or links if inputs are not checked.

Mitigation: Before distribution, restate the target links, authorized account, and template, prefer preview mode first, and require user confirmation before execution.

Risk: Exported local files from broad searches may retain commercial or sensitive result data on the machine.

Mitigation: Avoid broad or sensitive searches when retention is unwanted, and share concise previews rather than copying large result sets into chat.

Risk: Following trending products or reusing another seller's video material may create brand, patent, or content infringement exposure.

Mitigation: Have the user verify brand authorization and patent risk, and recommend creating original product media rather than directly copying videos.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/qinghu-douyin-video-distribute)
- [Qinghu API Endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API Key Dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Xiaofeng ERP Console](https://xfdyorder.zzbtool.com/zzb_super_goods_xf/index.html#/index)

## Skill Output:

**Output Type(s):** [guidance, API calls, text, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with JSON-RPC examples, concise result summaries, and optional exported table files for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Qinghu API token or configured Qinghu tools; paid tool calls require user authorization and store distribution requires user confirmation.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
