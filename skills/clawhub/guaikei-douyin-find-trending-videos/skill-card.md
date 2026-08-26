## Description:

Queries public Douyin data for keyword search, creator posts, video comments, and real-time trending topics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

Marketing, content, and research teams use this skill to query public Douyin videos, creator posts, comments, and hot-list data for topic discovery, competitor monitoring, sentiment review, and trend tracking.

### Deployment Geography for Use:

Global; depends on a China-hosted Guaikei service and Chinese-language interface.

## Known Risks and Mitigations:

Risk: The skill can match broad trend-research requests and may be invoked when the user did not explicitly name Douyin.

Mitigation: Confirm that the user wants Douyin public-data lookup before running a CLI command for generic trend, topic, or competitor research.

Risk: CLI runs automatically save scraped JSON results under logs/, which may include profile-linked public data and comments.

Mitigation: Collect only the fields and item counts needed, review or clear local logs after use, and avoid sharing raw exports outside the intended team.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-find-trending-videos)
- [Guaikei token and help site](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search CLI request schema](assets/search_cli_req.schema.json)
- [Search CLI response schema](assets/search_cli_resp.schema.json)
- [Post CLI request schema](assets/post_cli_req.schema.json)
- [Post CLI response schema](assets/post_cli_resp.schema.json)
- [Comment CLI request schema](assets/comment_cli_req.schema.json)
- [Comment CLI response schema](assets/comment_cli_resp.schema.json)
- [Hot list response schema](assets/hot_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Pure JSON on stdout, with operational logs on stderr and saved JSON log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; supports up to 10,000 returned items per run.]

## Skill Version(s):

1.0.0 (source: package.json, constants.js, changelog, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
