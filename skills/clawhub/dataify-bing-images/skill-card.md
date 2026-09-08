## Description:

Searches Bing Images for image results, not Bing web, news, shopping, map, or video results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Bing Images through Dataify, apply image filters, and receive compact image result summaries with source links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends image search queries to Dataify and requires access to a Dataify API token.

Mitigation: Use a session-scoped DATAIFY_API_TOKEN, avoid placing tokens in chat or project files, and verify only token presence when troubleshooting.

Risk: Returned image licensing may be unsuitable for reuse when no license filter is requested.

Mitigation: Tell users that licensing is unverified by default, apply a license filter when requested, and preserve source links for rights review.

Risk: High-volume, multi-page, or no-cache searches can materially increase account credit usage.

Mitigation: Ask for confirmation before high-volume, multi-page, or cost-changing searches and show only user-facing scope and cost drivers.

## Reference(s):

- [Dataify Bing Images API Reference](artifact/references/api.md)
- [Dataify Bing Images ClawHub Release](https://clawhub.ai/dataify-server/skills/dataify-bing-images)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown result summaries with image URLs, titles, dimensions, and source links; optional raw JSON or HTML when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Dataify API token for live calls. Image licensing is unverified unless the user requests a license filter.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
