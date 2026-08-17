## Description:

用 Cue 跑「全球宏观」场景的深度研究，追踪全球主要经济体的通胀、GDP、就业、对外贸易、央行利率与汇率等公开官方数据，并横向对比各国宏观表现。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangxiaoxu](https://clawhub.ai/user/wangxiaoxu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, developers, and business teams use this skill to run Cue deep-research workflows for global macroeconomic monitoring, cross-country comparison, and market context gathering from public data with source links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may clone, update, and execute the Cue runner repository.

Mitigation: Install only after confirming that the referenced Cue runner repository is trusted.

Risk: The runner uses Cue account credentials from local configuration and can consume account credits.

Mitigation: Require explicit user confirmation before any credit-consuming research run.

Risk: Macroeconomic research output may be incomplete, stale, or unsuitable as a sole basis for regulated decisions.

Mitigation: Preserve source links, avoid fabricating missing results, and treat reports as research support rather than legal, underwriting, or diligence advice.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wangxiaoxu/skills/cue-global-macro)
- [Cue Playbook API](https://cuecue.cn/api/playbook)
- [Cue Runner Repository](https://github.com/sensedeal/cue-skills)
- [Cue Runner Mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown report with source links and inline shell commands when setup or execution is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Cue playbook data, requires explicit user confirmation before credit-consuming runs, and should preserve source links in returned reports.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
