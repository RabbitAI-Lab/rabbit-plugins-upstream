## Description:

Fetches read-only Kuaishou / Kwai creator video lists through SocialDataX for creator research, recent publishing review, benchmarking, account tracking, and content analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Kuaishou creator video lists, summarize recent posts, review content style, benchmark creators, and support account tracking workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Data calls send the user's SOCIALDATAX_API_KEY and requested Kuaishou profile or user identifiers to SocialDataX.

Mitigation: Use a scoped API key where possible, avoid submitting unnecessary identifiers, and confirm the user understands the third-party data call before use.

Risk: Pagination options such as --all can increase credit use and network activity.

Mitigation: Prefer --max-items or --pages for bounded retrieval unless the user explicitly needs all available creator videos.

Risk: Examples install the npm package with @latest, so future package updates can change behavior.

Mitigation: Review package updates before deployment and pin a known package version in controlled environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-kuaishou-creator-videos)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses returned SocialDataX JSON fields such as platform, tool, arguments, data.items, page_count, item_count, and next_page_token when available.]

## Skill Version(s):

0.1.17 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
