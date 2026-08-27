## Description:

Search Google Play, read a full Android app listing including the real install count and Data safety table, and page reviews by cursor. 3 endpoints, 2 credits each, structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, ASO researchers, and mobile product teams use this skill to search Google Play, retrieve full Android app listings, and page reviews for competitor research, app metadata checks, and review analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and app IDs are sent to Scavio using the user's SCAVIO_API_KEY.

Mitigation: Use only data appropriate for the service and avoid submitting sensitive identifiers unless the lookup requires them.

Risk: Every endpoint call costs credits, and multi-page review crawls can spend credits quickly.

Mitigation: Confirm the crawl budget before paging reviews, use the listing's included 20 reviews first, and cap page counts.

Risk: Changing review sort while paging or treating cursor-end 404s as failures can waste calls or produce incomplete review sets.

Mitigation: Keep sort fixed for a cursor sequence and treat a 404 after cursor pagination as the documented stop signal.

## Reference(s):

- [Scavio Google Play Search Documentation](https://scavio.dev/docs/google-play-search)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/google-play-store-api)

## Skill Output:

**Output Type(s):** [JSON, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON request details and Python or JavaScript code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; requests send searches or app IDs to Scavio and each endpoint costs 2 credits.]

## Skill Version(s):

1.0.0 (source: server release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
