## Description:

Collects structured JSON from public Xiaohongshu content, including keyword note search, note details, comments, and creator post lists for trend, competitor, KOL, and sentiment analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Content, marketing, and data-analysis teams use this skill to research public Xiaohongshu notes, comments, and creator activity for topic discovery, competitor monitoring, KOL screening, and trend or sentiment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, note or profile URLs, requested limits, and GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Use only where that third-party API use is approved; protect the token and avoid sending sensitive research terms or links.

Risk: Full results, including comments and identifiers, may be saved under the skill's logs directory.

Mitigation: Restrict access to logs and delete or retain them according to the team's data-handling policy.

Risk: The skill is intended for public Xiaohongshu data and may return data subject to platform terms or privacy obligations.

Mitigation: Use it only for public-data analysis and review authorization before external sharing or redistribution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xiaohongshu-search-detail-comment-post)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Structured JSON from Node.js CLI commands, with status and error fields and optional local log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; retrieves public Xiaohongshu data through guaikei.com and may save full results under logs/.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
