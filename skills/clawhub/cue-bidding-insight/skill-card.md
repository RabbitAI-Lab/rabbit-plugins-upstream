## Description:

Uses Cue to scan public procurement and bidding sources, separate active tenders from closed projects, enrich public contact details, and summarize bidding opportunities and competitor awards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

B2B sales, business development, procurement, market intelligence, and competitive analysis teams use this skill to find public tender opportunities, review recent awards, monitor competitors, and prepare outreach from publicly available procurement information.

### Deployment Geography for Use:

Global; intended data coverage is focused on public Chinese procurement and bidding sources.

## Known Risks and Mitigations:

Risk: The skill uses Cue's external service for procurement research, which can expose query content to an external provider.

Mitigation: Use the skill only when external processing is acceptable, and keep sensitive internal strategy, credentials, customer information, and unnecessary personal data out of queries.

Risk: Returned contact details may be regulated business or personal data.

Mitigation: Handle contact details under applicable privacy, outreach, procurement, and anti-spam rules before using them for sales or bidding activity.

Risk: Public procurement sources can be incomplete, delayed, rate-limited, or temporarily unavailable.

Mitigation: Verify important deadlines, amounts, and eligibility details against official project pages before acting, and treat partial-source results as incomplete.

Risk: Broad searches can take longer, time out, or return overly large result sets.

Mitigation: Constrain keywords, region, and time window for operational use, and follow the documented retry and health-check guidance when Cue or source platforms are unavailable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/panting09266-ai/skills/cue-bidding-insight)
- [Cue API Key](https://cuecue.cn/hub/api-key)
- [企查查](https://www.qcc.com)
- [知了标讯](https://www.zhiliaobiaoxun.com)
- [中国招标投标公共服务平台](https://www.cebpubservice.com)
- [中国政府采购网](https://www.ccgp.gov.cn)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown procurement intelligence report with structured sections and optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include active tenders, closed awards, public contact details, source platforms, project amounts, deadlines, regional trends, and competitor summaries.]

## Skill Version(s):

1.0.0 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
