## Description:

Pull Douyin videos, user profiles and feeds, comments, hashtags, music, live rooms, the hot-search board, and keyword search across videos, users, music, live and hashtags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to retrieve structured Douyin public social data for creator analysis, trend spotting, comments, profiles, videos, music, live rooms, feeds, and keyword search.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin lookup requests and API credentials are sent to Scavio.

Mitigation: Use the skill only when that data flow is acceptable, store SCAVIO_API_KEY outside source control, and avoid exposing the key in prompts or logs.

Risk: Search endpoints cost 10 credits and repeated calls can consume credits quickly.

Mitigation: Check credits_used on responses, avoid tight search loops, and prefer narrower endpoint calls when possible.

Risk: Returned comments, profiles, counts, and trend rankings can be sensitive, user-generated, or time-dependent.

Mitigation: Summarize responsibly, do not fabricate missing values, avoid profiling individuals, and re-fetch time-sensitive boards before relying on them.

## Reference(s):

- [Scavio Documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=douyin-scraper-api)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=douyin-scraper-api)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/scavio-douyin)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration, json]

**Output Format:** [Markdown guidance with Python and curl examples; API responses are structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; endpoint calls consume credits, with search endpoints costing more than other Douyin endpoints.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
