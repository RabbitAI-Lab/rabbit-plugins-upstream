## Description:

查询澍脉 AI 投放驾驶舱的只读广告诊断数据，帮助用户查看投放表现、账户余额、止损或优化建议，以及品牌在 AI 大模型中的 GEO 可见度与排名。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dexun-inc](https://clawhub.ai/user/dexun-inc)

### License/Terms of Use:

MIT-0

## Use Case:

External operators and advertising teams use this skill to query Shumai for account overviews, campaign alerts, optimization guidance, and GEO visibility reports. It returns read-only diagnostics and instructs users to make any budget or campaign changes in the relevant media platform.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can retrieve sensitive advertising account metrics and recommendations through SHUMAI_API_KEY.

Mitigation: Install it only where Shumai advertising diagnostics are intended, keep the API key scoped appropriately, and protect the key as a credential.

Risk: Broad advertising-performance questions may trigger this integration and send a read-only query to Shumai.

Mitigation: Use it in agent environments where external Shumai diagnostic queries are expected and authorized.

Risk: Returned recommendations may influence budget or campaign decisions even though the skill cannot change settings directly.

Mitigation: Review the diagnostic context before acting and make any budget or campaign changes manually in the relevant media platform.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dexun-inc/skills/shumai-ads)
- [Publisher profile](https://clawhub.ai/user/dexun-inc)
- [Shumai dashboard API key setup](https://www.shumai.com.cn/admin/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Concise Chinese Markdown or plain text with preserved source metrics and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Shumai diagnostics; numeric values and returned recommendations should be preserved without estimation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
