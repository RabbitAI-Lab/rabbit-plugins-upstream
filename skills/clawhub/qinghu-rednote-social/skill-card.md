## Description:

青虎AI 小红书社媒运营把小红书热搜、关键词笔记搜索、笔记与评论分析、达人主页与作品数据结合起来，帮助用户拆解爆款笔记、提取种草痛点、筛选 KOC/KOL，并生成小红书种草方案或种草码。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

社媒运营者、品牌增长团队和代理商用它分析小红书热点、爆款笔记、评论痛点和达人表现，从而制定种草选题、笔记结构、KOC/KOL 分层名单与投放节奏。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Qinghu API key and makes external Qinghu data calls.

Mitigation: Use a dedicated, limited-scope token when available, store it in the documented environment variables, and review requested calls before sharing sensitive data.

Risk: The skill may export larger result sets or reuse locally cached data files.

Mitigation: Review exported files before sharing them and ask the agent not to export or reuse cached files when local persistence is not desired.

Risk: Marketing recommendations can be misleading if based on limited notes, comments, rankings, or time windows.

Mitigation: Require the agent to state sample size, site, period, and data source for metrics, and treat recommendations as decision support rather than final compliance or campaign approval.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/qinghu-rednote-social)
- [Qinghu MCP API Endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API Key Dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with JSON-RPC examples, API-call instructions, and optional exported spreadsheet files for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should summarize conclusions first, include sample-size and period context for metrics, and export result arrays of 10 or more records instead of pasting large tables into chat.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
