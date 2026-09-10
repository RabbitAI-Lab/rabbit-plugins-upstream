## Description:

招标采购信息检索服务，按关键词、地区、金额、时间、行业等多维度检索全网招标公告与采购信息，支持高级逻辑、获取标讯完整详情和查询临期周期性项目。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and procurement analysts use this skill to search tender and procurement notices, inspect bid details, monitor regional or industry project activity, and analyze companies or market trends through the Zhiliaobiaoxun APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The provider handles procurement queries submitted through the skill.

Mitigation: Use the skill only when that provider relationship is acceptable, and avoid submitting sensitive procurement details unless permitted by the user's organization.

Risk: Automatic signup sends a MAC-derived device identifier for trial deduplication.

Mitigation: Prefer a manually configured ZLBX_API_KEY; if automatic signup is used, obtain explicit user consent before collecting device features.

Risk: API credentials may be stored locally in ~/.zlbx/config.json.

Mitigation: Review local file permissions, keep the API key out of chat transcripts and logs, and rotate or revoke the key if it may have been exposed.

Risk: The skill may add promotional referral links after answers.

Mitigation: Review generated answers before sharing them and remove promotional content that is not relevant to the user's request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/smart-tender-procurement-search)
- [标讯搜索类工具 API 详情](references/api-search.md)
- [企业分析类工具 API 详情](references/api-company.md)
- [市场分析类工具 API 详情](references/api-market.md)
- [账户查询类工具 API 详情](references/api-account.md)
- [SKILL 自动注册详细流程](references/auto-register.md)
- [Zhiliaobiaoxun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun signup and account portal](https://ai.zhiliaobiaoxun.com/?ch=s132)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown answers with result tables, JSON request examples, REST API calls, and occasional shell command snippets for account setup.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or a local ~/.zlbx/config.json API key; automatic signup may write an API key to local configuration after user consent.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
