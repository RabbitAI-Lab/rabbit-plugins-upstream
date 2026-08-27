## Description:

Searches public Douyin content by keyword, collects creator posts and video comments, and retrieves real-time hot榜 data for content research, competitor analysis, public-opinion review, and trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and content research teams use this skill to run Douyin keyword searches, gather public creator posts, collect comments for sentiment review, and check current hot topics. It is suited to short-video planning, competitor monitoring, marketing reports, and internal research workflows that need structured Douyin JSON data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can trigger broadly during short-video research workflows and may collect public Douyin user, comment, profile-link, and IP-region data.

Mitigation: Use it only for explicit Douyin research tasks, limit collection volume to the minimum needed, and confirm legal, platform, and internal data-handling obligations before bulk comment or profile collection.

Risk: Queries and GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Install only when that service relationship is acceptable, pass the token through the environment, avoid sharing logs that could expose sensitive task context, and rotate the token if exposure is suspected.

Risk: Generated JSON logs can retain scraped identifiers, comments, profile links, and related metadata.

Mitigation: Store logs in an approved location, restrict access, redact or delete them after analysis, and avoid redistributing collected data outside authorized workflows.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-data-grabber)
- [Readme](readme.md)
- [Complete Options](references/options.md)
- [Changelog](references/changelog.md)
- [Search Response Schema](assets/search_cli_resp.schema.json)
- [Comment Response Schema](assets/comment_cli_resp.schema.json)
- [Post Response Schema](assets/post_cli_resp.schema.json)
- [Hot List Response Schema](assets/hot_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Command-line JSON responses on stdout with logs saved as JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and Node.js >=16.14; each CLI emits structured status, request, metadata, and results fields.]

## Skill Version(s):

1.0.0 (source: package.json, changelog, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
