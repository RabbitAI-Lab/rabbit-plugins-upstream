## Description:

Provides commands for searching public Douyin videos, retrieving creator posts and comments, and querying real-time trend rankings for content research and competitive analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to gather structured public Douyin data for short-video topic research, competitor monitoring, sentiment review, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin keywords, URLs or IDs, and the GUAIKEI token are sent to guaikei.com.

Mitigation: Use the skill only when that third-party data flow is acceptable, and keep the GUAIKEI_API_TOKEN scoped and protected.

Risk: Result JSON files are saved locally by default.

Mitigation: Review and remove local logs when they contain sensitive research topics, account identifiers, comments, or profile data.

Risk: The activation scope can apply to broad short-video research even when the user does not explicitly name Douyin.

Mitigation: Confirm Douyin is the intended source before running searches or analysis for broad short-video requests.

Risk: Returned media URLs could be misused as part of a video-download workflow.

Mitigation: Use returned URLs only for review and analysis, not for downloading, watermark removal, reposting, or redistribution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-trending-videos-and-rankings)
- [Usage and token documentation](readme.md)
- [Complete options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search request schema](assets/search_cli_req.schema.json)
- [Search response schema](assets/search_cli_resp.schema.json)
- [Post request schema](assets/post_cli_req.schema.json)
- [Post response schema](assets/post_cli_resp.schema.json)
- [Comment request schema](assets/comment_cli_req.schema.json)
- [Comment response schema](assets/comment_cli_resp.schema.json)
- [Hot ranking response schema](assets/hot_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON on stdout with stderr logs and optional local JSON log files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; result JSON files are saved locally by default.]

## Skill Version(s):

1.0.0 (source: package.json, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
