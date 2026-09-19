## Description:

Collects public Douyin search results, creator posts, video or image comments, and hot-list data as structured JSON for content planning, competitor monitoring, and comment insight workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External users, product teams, customer support teams, marketers, and content operators use this skill to collect public Douyin content, creator posts, comments, and hot-list data. The structured results support topic research, competitor monitoring, sentiment review, trend tracking, and downstream reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Douyin keywords, profile links, video IDs, and comment targets to www.guaikei.com.

Mitigation: Use it only when that third-party transfer is acceptable, avoid sensitive monitoring targets, and comply with platform terms and applicable privacy rules.

Risk: Successful search, post, and comment results may be saved locally in plaintext.

Mitigation: Manage access to generated logs and delete them when they are no longer needed.

Risk: The authoritative security summary flags a mismatch between the no-write claim in the main instructions and automatic local result saving.

Mitigation: Review the behavior before installation and confirm local logging is acceptable for the deployment environment.

## Reference(s):

- [Server-resolved GitHub repository](https://github.com/why20261/douyin-comments-insight-analysis)
- [ClawHub skill page](https://clawhub.ai/why20261/skills/douyin-comments-insight-analysis)
- [GUAIKEI API token and support](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search request schema](assets/search_cli_req.schema.json)
- [Search response schema](assets/search_cli_resp.schema.json)
- [Post response schema](assets/post_cli_resp.schema.json)
- [Comment response schema](assets/comment_cli_resp.schema.json)
- [Hot-list response schema](assets/hot_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Structured JSON result envelopes, with concise Markdown summaries or command guidance when the agent reports outcomes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN. Successful search, post, and comment runs may save plaintext JSON logs locally.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact frontmatter, package.json, and changelog report implementation version 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
