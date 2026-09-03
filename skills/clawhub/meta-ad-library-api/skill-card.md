## Description:

Search the Meta Ad Library by keyword or Facebook Page id and walk full cursor pagination through every ad, with creative, run dates, platforms and political spend. 3 endpoints, 1 credit per page.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and research agents use this skill to search public Facebook and Instagram ad-library data through Scavio, retrieve ad creative and run metadata, and paginate keyword or advertiser result sets into structured datasets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries are sent to Scavio as an external API provider.

Mitigation: Install only if external API use is acceptable for the workspace and keep SCAVIO_API_KEY in the environment or a secret store.

Risk: Broad paginated searches can consume paid credits.

Mitigation: Set a page limit and confirm the expected credit budget before walking full cursor pagination.

Risk: Ad Library totals and spend fields can be misread.

Mitigation: Do not treat capped totals as exact, and do not report null commercial spend or reach as zero.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/meta-ad-library-api)
- [Scavio Meta Ads Search documentation](https://scavio.dev/docs/meta-ads-search)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration, text, markdown]

**Output Format:** [Markdown guidance with JSON API request examples and inline shell/Python/JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to call Scavio endpoints that return structured JSON responses for public Meta ad-library searches.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
