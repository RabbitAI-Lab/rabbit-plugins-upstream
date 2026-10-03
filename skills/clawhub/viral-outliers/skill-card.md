## Description:

Helps agents research viral posts and creator performance on TikTok, Instagram, and YouTube, including transcripts, video analysis, competitor watchlists, and profile crawls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[matsclaes2](https://clawhub.ai/user/matsclaes2)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and content creators use this skill to identify unusually successful posts, compare creators, analyze videos, and monitor competitors across social platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries and API credentials are sent to Viral Outliers.

Mitigation: Use a secrets manager or environment variable for the key, and avoid sending sensitive research queries.

Risk: Paid requests consume prepaid credits.

Mitigation: Check pricing and balance, and confirm before making paid requests or adding credits.

Risk: Tracking, watchlist, and alert actions change stored account settings.

Mitigation: Confirm with the account owner before creating or changing tracked profiles, watchlists, or alerts.

Risk: The optional npx/npm CLI downloads executable packages.

Mitigation: Pin an approved package version or use MCP or REST instead if supply-chain control is required.

## Reference(s):

- [Viral Outliers documentation](https://viraloutliers.com/docs)
- [Getting started with Viral Outliers](https://viraloutliers.com/docs/getting-started)
- [Viral Outliers API specification](https://viraloutliers.com/openapi.json)
- [Getting started reference](references/getting-started.md)
- [Skills and API reference](references/skills.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with research summaries, API examples, and setup instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Research may include creator metrics, transcripts, video breakdowns, and watchlist results.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
