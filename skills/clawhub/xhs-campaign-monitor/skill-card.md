## Description:

Xhs Campaign Monitor helps agents retrieve public Xiaohongshu notes, note details, comments, and creator posts for content research, competitor monitoring, KOL screening, and trend analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, content creators, and analysts use this skill to collect structured public Xiaohongshu data for campaign research, competitive analysis, comment insight, creator monitoring, and downstream reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests send Xiaohongshu keywords, note URLs, profile URLs, and GUAIKEI_API_TOKEN-authenticated traffic to guaikei.com.

Mitigation: Use the skill only when that third-party API data flow is acceptable and keep the API token scoped and stored as an environment variable.

Risk: Successful results are saved in the local logs directory and may include competitive research terms, public profile data, comments, and note metadata.

Mitigation: Run the skill on a trusted machine and review, retain, or delete generated log files according to the user's data-handling policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/xhs-campaign-monitor)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Structured JSON results with status, error_code, metadata, and results fields; agent-facing guidance may be returned as concise Markdown text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful command results are saved locally under the skill's logs directory.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
