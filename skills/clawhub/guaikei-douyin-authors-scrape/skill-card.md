## Description:

Retrieves structured public Douyin data for keyword search, creator posts, video comments, and real-time trending topics for content analysis and reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, content creators, analysts, and marketers use this skill to collect structured public Douyin search results, creator posts, comments, and hot-list data for topic research, competitor monitoring, public sentiment review, and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin search terms, target URLs or IDs, limits, and the API token are sent to guaikei.com.

Mitigation: Use the skill only for public Douyin data the user is authorized to analyze, and confirm that sending these inputs to the third-party API is acceptable.

Risk: Successful search, post, and comment results may be saved locally under the skill's logs directory.

Mitigation: Protect or clear local logs when research topics or collected public data are sensitive.

Risk: The skill depends on a valid GUAIKEI_API_TOKEN and a third-party API service.

Mitigation: Store the token securely, avoid sharing it in prompts or logs, and stop execution when authentication errors occur.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-authors-scrape)
- [Guaikei Douyin Data API](https://www.guaikei.com)
- [Complete CLI Options](references/options.md)
- [Changelog](references/changelog.md)
- [Search CLI Request Schema](assets/search_cli_req.schema.json)
- [Post CLI Response Schema](assets/post_cli_resp.schema.json)
- [Comment CLI Response Schema](assets/comment_cli_resp.schema.json)
- [Hot CLI Response Schema](assets/hot_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON to stdout with stderr logs and optional local JSON log files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and Node.js 16.14.0+; documented commands return success, empty, or error JSON with exit codes.]

## Skill Version(s):

1.0.0 (source: frontmatter, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
