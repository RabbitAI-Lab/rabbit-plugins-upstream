## Description:

This skill helps agents search public Douyin videos, images, users, creator posts, comments, and real-time hot rankings for topic research, competitor analysis, sentiment review, and trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content strategists, marketers, and developers use this skill to collect public Douyin search results, creator posts, comments, and hot rankings for topic planning, competitor analysis, sentiment review, and trend monitoring. It is not intended for posting, editing, downloading, or accessing private Douyin data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin search terms, target URLs, and GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Use the skill only when the user explicitly wants Douyin data, avoid sensitive queries, and keep the token scoped and rotated according to the publisher's guidance.

Risk: Search, post, and comment results are saved locally by default.

Mitigation: Review and delete local logs that contain sensitive research, user handles, comments, or business analysis after they are no longer needed.

Risk: Returned media URLs could be misused for downloading, redistribution, or other rights-sensitive activity.

Mitigation: Use returned media URLs for inspection and analysis only, and avoid downloading or redistributing media unless the user has confirmed rights and platform compliance.

Risk: The skill has broad activation language for trend, competitor, and sentiment tasks.

Mitigation: When the request is ambiguous, confirm that the user wants Douyin public-data lookup before running commands or sending target information to the API service.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-trend-radar)
- [CLI Option Reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search Request Schema](assets/search_cli_req.schema.json)
- [Search Response Schema](assets/search_cli_resp.schema.json)
- [Guaikei Token Service](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON on stdout, with operational logs on stderr and saved JSON result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and writes result logs locally by default.]

## Skill Version(s):

1.0.0 (source: package.json, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
