## Description:

用 Cue 穿透人物的全生命周期工商与司法轨迹，剥离当前在册与历史风险、映射其商业控制版图，产出可用于 IPO 或重大交易的个人背调底稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, compliance teams, transaction teams, and recruiters use this skill to request public-record background-check drafts for key people, including company roles, investments, judicial risk, administrative penalties, and source links. The draft requires professional review before formal use, especially for employment, credit, IPO, or major transaction decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send sensitive identifying details and due-diligence questions to the external Cue service.

Mitigation: Use the skill only when sharing the subject details with Cue is acceptable, minimize identifiers in the query, and obtain subject consent for employment, credit, or similarly sensitive uses.

Risk: The workflow may create or include an externally hosted Cue share link for the report.

Mitigation: Tell the agent not to include or create a share link unless an externally hosted report URL is intended for the audience.

Risk: The skill produces a background-check draft based on public records and external data sources, not a final compliance determination.

Mitigation: Have a qualified reviewer verify source links, legal relevance, and current status before using the report in IPO, transaction, employment, credit, or other formal decisions.

Risk: A local Markdown copy of the report can contain sensitive due-diligence content.

Mitigation: Store generated report files in an access-controlled location and delete local copies when retention is not required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-person-background-check)
- [ClawHub publisher profile](https://clawhub.ai/user/panting09266-ai)
- [Cue runner source](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)
- [Cue API key page](https://cuecue.cn/hub/api-key)
- [China Judgments Online](https://wenshu.court.gov.cn)
- [China Enforcement Information Disclosure](https://zxgk.court.gov.cn)
- [National Enterprise Credit Information Publicity System](https://www.gsxt.gov.cn)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with inline shell commands, source links, a Cue report URL when available, and local file path references.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill requests a Cue-hosted report through an external service and stores a local Markdown copy when the runner succeeds.]

## Skill Version(s):

1.0.6 (source: ClawHub release evidence; artifact frontmatter states 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
