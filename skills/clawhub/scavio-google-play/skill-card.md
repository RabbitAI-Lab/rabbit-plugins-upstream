## Description:

Searches Google Play, retrieves full Android app listings including install counts and Data safety data, and pages app reviews by cursor through Scavio's structured JSON API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, app marketers, and research agents use this skill to search Android apps, inspect complete Play Store listings, compare competitors, and retrieve review pages for ASO and market research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Google Play research queries and identifiers to Scavio using an API key.

Mitigation: Use only approved Scavio credentials and send only Google Play data that is acceptable to share with Scavio.

Risk: Every API call consumes Scavio credits, and unnecessary review pagination can increase cost.

Mitigation: Budget credit use before multi-page crawls, rely on the reviews already returned by the app endpoint when sufficient, and cap review pagination.

Risk: Incorrect app identifiers or unsupported storefront parameters can produce errors or fallback data.

Mitigation: Confirm package names with the app endpoint, keep review cursor sort values unchanged, and handle 400, 401, 404, 429, 502, and 503 responses as documented.

Risk: The agent could overstate Google Play data if it fills gaps from assumptions.

Mitigation: Return only data supplied by the Scavio API response and avoid fabricating package names, install counts, ratings, permissions, or review text.

## Reference(s):

- [Scavio Google Play Search Documentation](https://scavio.dev/docs/google-play-search)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/scavio-google-play)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API response expectations, request examples, and setup commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API calls use Scavio credits and return structured JSON envelopes.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
