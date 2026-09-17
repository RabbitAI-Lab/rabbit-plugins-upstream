## Description:

Collects public Douyin keyword, hot-list, creator-post, and comment data as structured JSON so agents can support product research, competitor monitoring, trend tracking, and content analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External operators, analysts, and developers use this skill to retrieve public Douyin search results, hot-list items, creator posts, and comments for product research, competitor monitoring, trend tracking, and downstream analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party Douyin data API and the security summary notes that API tokens are sent in URL query parameters.

Mitigation: Use a dedicated, revocable GUAIKEI token with limited quota, avoid exposing terminal sessions or logs, and rotate the token if exposure is suspected.

Risk: Collected public user, post, and comment data may be saved as plaintext JSON logs.

Mitigation: Run the skill outside shared or synced workspaces, protect or delete generated logs, and sanitize personal fields before sharing results.

Risk: The skill is intended for public Douyin data and is not suitable for private, hidden, or login-gated content.

Mitigation: Use only public links, keywords, or IDs, and confirm authorization before public redistribution or commercial reuse of collected data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/why20261/skills/douyin-bluesea-collector)
- [Server-resolved source repository](https://github.com/why20261/douyin-bluesea-collector)
- [GUAIKEI API service](https://www.guaikei.com)
- [Complete CLI options](artifact/references/options.md)
- [Release changelog](artifact/references/changelog.md)
- [Search CLI request schema](artifact/assets/search_cli_req.schema.json)
- [Search CLI response schema](artifact/assets/search_cli_resp.schema.json)
- [Creator posts CLI request schema](artifact/assets/post_cli_req.schema.json)
- [Creator posts CLI response schema](artifact/assets/post_cli_resp.schema.json)
- [Hot list CLI response schema](artifact/assets/hot_cli_resp.schema.json)
- [Comment CLI request schema](artifact/assets/comment_cli_req.schema.json)
- [Comment CLI response schema](artifact/assets/comment_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; executed commands return JSON on stdout and may write JSON log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; retrieved public Douyin data may include public user, post, and comment fields.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact package/frontmatter report 1.0.0 and artifact changelog top entry reports 1.2.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
