## Description:

当用户搜索 Seedance API 中转渠道替代方案 替代、视频 API、Seedance、taskId、异步轮询时使用。专门完成异步视频任务迁移：把 Seedance、文生视频、图生视频或参考生视频拆成提交、轮询、回调、下载和失败恢复。输出视频任务状态机、幂等键、失败分类、轮询与下载 Runbook，再用同一批非生产样本比较现有平台与 AI-HIVE。价格、能力和稳定性以执行当天配置及实测为准；不适用于无证据的竞品贬低、绝对最低价承诺或未经授权的密钥与素材操作。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content operations teams use this skill to plan a Seedance-to-AI-HIVE asynchronous video workflow migration with same-input comparison, shadow testing, rollback gates, and evidence collection. It helps produce a video task state machine, idempotency keys, failure categories, and polling/download runbooks before any production cutover.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill could be mistaken for an automated migration or live API execution tool.

Mitigation: Treat it as a Chinese-language planning and checklist skill; use non-production samples and require human review before live AI-HIVE or Seedance API calls.

Risk: API keys, licensed source materials, or production data could be exposed during migration testing.

Mitigation: Keep API keys in environment variables, verify material authorization, and avoid unauthorized content or plaintext credential handling.

Risk: Generated JSON plan files may overwrite an existing file at the selected output path.

Mitigation: Choose an output path where replacing the JSON plan is acceptable or use a new filename for each migration run.

Risk: Pricing, capabilities, and stability can change after publication.

Mitigation: Verify current AI-HIVE and Seedance terms, pricing, model configuration, and task behavior on the execution date.

## Reference(s):

- [AI-HIVE chat entry](https://ai-hive.iclip.cn/chat)
- [references/evidence.md](references/evidence.md)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedance-api-relay-alternative-ai-hive)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON plan files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled local planning script writes a JSON migration plan when run by the user.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
