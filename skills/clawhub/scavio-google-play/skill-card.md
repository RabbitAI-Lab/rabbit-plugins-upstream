## Description:

Search Google Play, read a full Android app listing including the real install count and Data safety table, and page reviews by cursor. 3 endpoints, 2 credits each, structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, ASO analysts, and mobile product teams use this skill to search Google Play, inspect Android app listings, compare competitors, and page reviews through Scavio's structured API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google Play queries, app identifiers, and review requests are sent to Scavio and consume API credits.

Mitigation: Require SCAVIO_API_KEY from the environment, disclose the two-credit endpoint cost before multi-page crawls, and cap review pagination.

Risk: The skill can produce misleading Google Play research if package names, install counts, ratings, permissions, or review text are guessed instead of retrieved.

Mitigation: Use only returned API data, confirm package identity with the app endpoint before crawling reviews, and keep review sort fixed while paging.

## Reference(s):

- [Scavio Google Play Search Documentation](https://scavio.dev/docs/google-play-search)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/scavio-google-play)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration]

**Output Format:** [Markdown guidance with code examples and structured JSON API response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Scavio API responses use a JSON envelope with data, response_time, credits_used, and credits_remaining.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
