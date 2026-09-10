## Description:

青虎AI TikTok 视频复刻帮助用户从 TikTok 视频榜单、关键词搜索和商品关联视频中找到经过市场验证的样本，并拆解钩子、内容结构、卖点表达和评论洞察来产出可复用的拍摄脚本模板。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and marketing teams use this skill to analyze TikTok video samples and produce reusable short-video scripts, shot plans, and comment-driven content ideas. The skill is intended for script and template generation, not for generating finished videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a user-provided Qinghu API token.

Mitigation: Request the token only when needed, prefer environment variables when already configured, and avoid exposing the token in outputs or exported files.

Risk: Qinghu API calls may consume credits.

Mitigation: Get user confirmation before data calls and report credit consumption from the response envelope when calls occur.

Risk: Larger result sets may be exported to local files.

Mitigation: Share only the export link and a short preview, and avoid copying large raw datasets into chat output.

Risk: Video cloning guidance can be misused to copy another creator's finished content.

Mitigation: Use the skill to learn structure and produce original scripts, and remind users to reshoot original material instead of reusing third-party assets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-tiktok-video-clone)
- [Publisher profile](https://clawhub.ai/user/autoagc)
- [Qinghu API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Markdown, Files, Guidance]

**Output Format:** [Markdown responses with structured tables, reusable script templates, API-call guidance, and optional exported table files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill asks for user confirmation before Qinghu API calls, reports Qinghu credit consumption when calls occur, and exports larger result sets to local files when available.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
