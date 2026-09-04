## Description:

按主题检索搜狗微信文章，筛选和编码候选 URL，并分批导入指定 IMA 知识库文件夹的知识采集流水线。

This skill is ready for commercial/non-commercial use.

## Publisher:

[byrdsongstratakoslb663-ctrl](https://clawhub.ai/user/byrdsongstratakoslb663-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and knowledge-base operators use this skill to collect public WeChat article candidates for a topic, filter them for relevance, and bulk-import selected URLs into an IMA knowledge-base folder after confirming the target.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bulk imports can add many URL entries to an IMA folder, and unwanted entries may require manual cleanup in the IMA interface.

Mitigation: Confirm the target knowledge base and folder before import, keep batches small enough to inspect, and review imported titles after completion.

Risk: Sogou WeChat search or redirect pages may rate-limit requests or return captcha/interstitial pages.

Mitigation: Use the skill's low-rate search and backoff behavior, stop when redirect throttling appears, and resume later instead of retrying aggressively.

Risk: Topic filtering can still admit noisy or advertising articles.

Mitigation: Sample filtered titles before import and prepare a manual cleanup list for any irrelevant imported entries.

## Reference(s):

- [IMA MCP 工具签名与 ID 基线](references/ima_kb_api.md)
- [检索与效率复盘](references/pitfalls.md)
- [ClawHub skill page](https://clawhub.ai/byrdsongstratakoslb663-ctrl/skills/caiji-for-ima)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, JSON, Markdown]

**Output Format:** [Markdown guidance with shell commands and generated JSON batch files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local search outputs, filtered URL batches, wave files for import, and optional import reports.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
