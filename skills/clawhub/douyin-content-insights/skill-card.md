## Description:

Provides command-line access to Douyin public content data for keyword search, creator post collection, video or image-text comment collection, and real-time trending lists, returning structured JSON for content research, competitor monitoring, topic discovery, sentiment analysis, and trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External users, content operators, marketers, analysts, and developers use this skill to collect public Douyin search results, creator posts, comments, and hot-list data for content planning, competitor/account monitoring, public-comment analysis, reports, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin keywords, Douyin links, and the Guaikei API token are sent to the Guaikei service during skill execution.

Mitigation: Use the skill only when that data transfer is acceptable, keep GUAIKEI_API_TOKEN protected, and avoid submitting sensitive or unauthorized queries.

Risk: Successful search, creator-post, and comment results can be written to local JSON log files under the skill logs directory.

Mitigation: Review and clear generated logs after use, especially in shared machines, shared workspaces, or workflows that process sensitive research topics.

Risk: Security evidence reports a suspicious verdict because the skill documentation claims no write operations while implementation saves full query results locally.

Mitigation: Treat the log-writing behavior as expected operational behavior during review and deployment, and disclose it to users before running collection commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/why20261/skills/douyin-content-insights)
- [Server-resolved GitHub provenance](https://github.com/why20261/douyin-content-insights)
- [Guaikei API token and support site](https://www.guaikei.com)
- [Complete option reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search request schema](assets/search_cli_req.schema.json)
- [Search response schema](assets/search_cli_resp.schema.json)
- [Creator posts response schema](assets/post_cli_resp.schema.json)
- [Comments response schema](assets/comment_cli_resp.schema.json)
- [Hot-list response schema](assets/hot_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Files, Guidance]

**Output Format:** [Structured JSON envelope from CLI stdout; search, post, and comment tasks may also save JSON result files under the skill logs directory.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; commands send Douyin keywords or links to the Guaikei service and return public Douyin content metadata, engagement counts, tags, links, and comments where applicable.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter, package.json, and changelog report 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
