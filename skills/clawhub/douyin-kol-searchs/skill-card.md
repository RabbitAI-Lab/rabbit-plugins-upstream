## Description:

Queries public Douyin KOL and content data through keyword search, hot rankings, creator work lists, and comment retrieval for content planning, competitor monitoring, sentiment review, and trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External marketers, content operators, analysts, and developers use this skill to fetch structured public Douyin search, hot-list, creator-post, and comment data before summarizing trends, comparing creators, or preparing marketing reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends GUAIKEI_API_TOKEN in request URLs, and the token may have paid quota or account value.

Mitigation: Use a restricted, revocable token, avoid exposing terminal sessions or logs, and rotate the token if it may have been disclosed.

Risk: Fetched Douyin data is automatically saved locally and may include sensitive research targets or user-generated comment data.

Mitigation: Run the skill on trusted machines, avoid shared workspaces for sensitive searches, remove unneeded logs, and anonymize personal identifiers before sharing results.

Risk: The authoritative security summary marks the release as suspicious because token handling and local data retention deserve review before installation.

Mitigation: Review the security guidance before use, confirm the intended data handling policy, and limit execution to public Douyin data that the user is authorized to analyze.

## Reference(s):

- [Server-resolved source repository](https://github.com/why20261/douyin-kol-searchs)
- [ClawHub skill page](https://clawhub.ai/why20261/skills/douyin-kol-searchs)
- [Douyin data API site](https://www.guaikei.com)
- [Complete option reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search request schema](assets/search_cli_req.schema.json)
- [Search response schema](assets/search_cli_resp.schema.json)
- [Creator works request schema](assets/post_cli_req.schema.json)
- [Creator works response schema](assets/post_cli_resp.schema.json)
- [Hot list response schema](assets/hot_cli_resp.schema.json)
- [Comment request schema](assets/comment_cli_req.schema.json)
- [Comment response schema](assets/comment_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [json, shell commands, files, guidance]

**Output Format:** [JSON on stdout, with optional local JSON log files and concise human-facing guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; fetched Douyin data may be saved locally.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
