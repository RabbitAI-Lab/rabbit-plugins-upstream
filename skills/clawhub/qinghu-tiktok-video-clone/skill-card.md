## Description:

青虎AI TikTok 视频复刻从 TikTok 视频榜单和关键词搜索里找出经过市场验证的爆款视频，批量查视频详情、读视频评论，拆解它的开头钩子、内容结构、卖点表达与互动亮点，产出可直接复用的脚本模板。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and ecommerce teams use this skill to find proven TikTok video examples, analyze hooks, structure, selling points, and comments, then produce reusable shot-by-shot scripts for original recreations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask for a Qinghu API token.

Mitigation: Use only a token intended for this workflow and avoid exposing it in shared transcripts, exports, or logs.

Risk: Approved Qinghu data calls may consume Qinghu credits.

Mitigation: Confirm the planned tools before calls and report actual consumption from the returned pointCost value.

Risk: Large research results may be cached or exported to local spreadsheet files.

Mitigation: Review exported files before sharing them, especially when the research is commercially sensitive.

Risk: Recreating successful TikTok videos can create copyright or platform-policy risk if existing assets are copied directly.

Mitigation: Use the analysis to recreate structure and messaging while filming original footage and avoiding direct reuse of another creator's materials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-tiktok-video-clone)
- [Qinghu data API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Markdown analysis with structured script templates and optional spreadsheet exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include sample lists, five-part structure breakdowns, reusable scripts, comment insights, and concise export links when larger result sets are saved locally.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
