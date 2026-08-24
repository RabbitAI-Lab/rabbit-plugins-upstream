## Description:

Collects public Douyin keyword search, creator post, video comment, and real-time hot-list data as structured JSON for content research, competitor benchmarking, sentiment analysis, and trend monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to run Node.js CLI commands that query public Douyin data through the guaikei.com API, then analyze returned JSON for short-video planning, competitor monitoring, audience feedback, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Douyin search terms, creator URLs, and video URLs to the guaikei.com API.

Mitigation: Install and run it only for workflows where that API submission is intended; avoid sensitive or private inputs.

Risk: The skill can broadly trigger Douyin collection for content research or competitor benchmarking, including when a user does not explicitly say Douyin.

Mitigation: Use explicit Douyin-related prompts or confirm the target platform before running collection commands when intent is ambiguous.

Risk: Returned public data may be saved automatically as local JSON logs.

Mitigation: Delete local logs when no longer needed and collect only the minimum number of posts or comments required.

Risk: Returned media URLs or public platform data may be subject to rights or platform-policy restrictions.

Mitigation: Do not use returned media URLs for downloading, redistribution, or publication unless rights and platform-policy clearance are confirmed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-videos-for-competitor-benchmarking)
- [Usage documentation](readme.md)
- [Command options](references/options.md)
- [Changelog](references/changelog.md)
- [Search CLI schemas](assets/search_cli_req.schema.json)
- [Post CLI schemas](assets/post_cli_req.schema.json)
- [Comment CLI schemas](assets/comment_cli_req.schema.json)
- [Hot CLI response schema](assets/hot_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Files, Guidance]

**Output Format:** [JSON on stdout with local JSON log files and concise stderr status messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js >= 16.14.0 and GUAIKEI_API_TOKEN; commands support limits up to 10000 public records per run.]

## Skill Version(s):

1.0.0 (source: artifact package.json, changelog, constants, and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
