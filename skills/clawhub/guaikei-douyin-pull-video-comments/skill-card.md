## Description:

This skill helps agents collect public Douyin data for keyword search, creator posts, video comments, and real-time trending topics for operations, competitor research, sentiment review, and content planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, marketers, operations analysts, and content researchers use this skill to collect public Douyin search, creator, comment, and hot-list data for topic discovery, competitor monitoring, sentiment review, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can trigger on broad short-video research requests and collect Douyin data beyond the user's intended scope.

Mitigation: Use prompts that explicitly name Douyin and review the request scope before running collection commands.

Risk: Fetched comment, profile, and video data is saved locally in the skill's logs directory.

Mitigation: Avoid collecting or retaining sensitive comment or profile data unless authorized, and delete logs when exported data is no longer needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/engheng-art/skills/guaikei-douyin-pull-video-comments)
- [Guaikei token and support site](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search CLI request schema](assets/search_cli_req.schema.json)
- [Search CLI response schema](assets/search_cli_resp.schema.json)
- [Post CLI request schema](assets/post_cli_req.schema.json)
- [Post CLI response schema](assets/post_cli_resp.schema.json)
- [Comment CLI request schema](assets/comment_cli_req.schema.json)
- [Comment CLI response schema](assets/comment_cli_resp.schema.json)
- [Hot CLI response schema](assets/hot_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Files, Guidance]

**Output Format:** [Pure JSON on stdout, stderr logs, and JSON log files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14 or newer and GUAIKEI_API_TOKEN; each collection command supports up to 10,000 records and writes local logs.]

## Skill Version(s):

1.0.0 (source: package.json, changelog, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
