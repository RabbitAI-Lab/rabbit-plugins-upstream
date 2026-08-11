## Description:

Search the Apple App Store, read a full app listing by App Store id or bundle id, and pull user reviews as structured JSON. 3 endpoints, 1 credit each, any Apple storefront.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, product teams, and App Store Optimization practitioners use this skill to search App Store listings, retrieve app metadata, and analyze user reviews across Apple storefronts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests send App Store search terms, app IDs, and review queries to Scavio.

Mitigation: Use the skill only when those query details are appropriate to share with Scavio.

Risk: API calls require SCAVIO_API_KEY and may spend Scavio credits.

Mitigation: Set the API key in the environment, monitor remaining credits, and cap high-volume review collection by storefront and page count.

## Reference(s):

- [Scavio App Store Search Documentation](https://scavio.dev/docs/app-store-search)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/scavio-app-store)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration]

**Output Format:** [Markdown guidance with JSON request details and Python or JavaScript code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API calls may spend Scavio credits and return structured JSON.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
