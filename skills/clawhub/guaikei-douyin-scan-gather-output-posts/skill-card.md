## Description:

This skill helps agents search Douyin public content, gather creator posts, read comments, and fetch hot topics as structured JSON for analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and content analysts use this skill for Douyin public-content research, competitor monitoring, comment analysis, hot-topic tracking, and marketing report preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can trigger on broad short-video research prompts and may run when the user did not explicitly ask for Douyin.

Mitigation: Use it for explicit Douyin research, and confirm intent before running it for ambiguous trend or short-video prompts.

Risk: Search terms, Douyin URLs, and GUAIKEI_API_TOKEN are sent to a third-party service.

Mitigation: Install only when that data sharing is acceptable, store the token in an environment variable, and avoid using sensitive queries or private URLs.

Risk: Collected public-content results are saved locally in JSON log files.

Mitigation: Review saved logs before sharing outputs and remove local logs that are no longer needed.

Risk: Results may expose media URL fields even though downloading videos is out of scope.

Mitigation: Use returned URLs for analysis only and do not download or redistribute content unless separately authorized.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-scan-gather-output-posts)
- [Guaikei token and help site](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search CLI request schema](assets/search_cli_req.schema.json)
- [Search CLI response schema](assets/search_cli_resp.schema.json)
- [Post CLI response schema](assets/post_cli_resp.schema.json)
- [Comment CLI response schema](assets/comment_cli_resp.schema.json)
- [Hot CLI response schema](assets/hot_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, JSON]

**Output Format:** [JSON on stdout, operational messages on stderr, and saved JSON log files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; CLI results are limited by command options and may be saved under logs/.]

## Skill Version(s):

1.0.0 (source: SKILL.md metadata, package.json, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
