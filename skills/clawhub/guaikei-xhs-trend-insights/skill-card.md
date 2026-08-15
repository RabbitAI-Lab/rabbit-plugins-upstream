## Description:

小红书趋势洞察 helps agents collect public Xiaohongshu search results, note details, comments, and creator posts as structured JSON for trend, competitor, KOL, and sentiment analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, creators, analysts, and agents use this skill to collect public Xiaohongshu data for topic research, competitor monitoring, KOL screening, trend tracking, and comment sentiment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords, links, and GUAIKEI_API_TOKEN to guaikei.com.

Mitigation: Use only approved public-data queries and an authorized token, and avoid submitting sensitive internal information.

Risk: Returned Xiaohongshu results may be saved locally in logs.

Mitigation: Review local retention requirements and remove logs that are no longer needed.

Risk: The top-level description can understate the skill's broader search, note-detail, profile-post, and local-retention behavior.

Mitigation: Review and approve the skill as a broad Xiaohongshu public-data collection tool before enabling it in workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-trend-insights)
- [Guaikei API service](https://www.guaikei.com)
- [Parameter and usage reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Structured JSON from Node.js CLI commands with concise Markdown summaries when useful]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and may save returned results under logs/.]

## Skill Version(s):

1.0.0 (source: server release metadata and release changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
