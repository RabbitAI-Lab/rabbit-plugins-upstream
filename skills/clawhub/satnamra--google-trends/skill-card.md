## Description:

Monitor Google Trends - get trending searches, compare keywords, and track interest over time.

This skill is ready for commercial/non-commercial use.

## Publisher:

[satnamra](https://clawhub.ai/user/satnamra)

### License/Terms of Use:

MIT

## Use Case:

Developers, marketers, and content teams use this skill to monitor daily trending searches, compare keyword interest, and track search interest over time for market research, content planning, SEO, and trend analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill fetches public Google Trends pages and RSS feeds, and automated schedules can repeatedly run that workflow.

Mitigation: Install only when that network access is acceptable, and review scheduled country codes and keywords before using the workflow in shared or automated environments.

Risk: Google Trends data is relative, may be rate limited, and may not provide complete historical detail.

Mitigation: Treat trend results as directional signals and verify important decisions against additional sources before acting.

## Reference(s):

- [Google Trends Daily Trending Searches RSS](https://trends.google.com/trending/rss?geo=US)
- [Google Trends Explore](https://trends.google.com/trends/explore?q=bitcoin&geo=US)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and concise trend summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Google Trends URLs, RSS-derived trend lists, comparison guidance, and scheduling examples; results depend on public Google Trends availability and rate limits.]

## Skill Version(s):

1.0.0 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
