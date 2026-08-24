## Description:

This skill helps agents collect public Douyin keyword search results, creator posts, video comments, and hot-list data for competitor research, content analysis, and trend monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content strategists, marketing analysts, and research teams use this skill to gather public Douyin data for short-video topic discovery, competitor account monitoring, comment review, and hot-trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin research terms, profile URLs, video URLs, and retrieved public data are sent through the Guaikei API using GUAIKEI_API_TOKEN.

Mitigation: Use the skill only when that data flow is acceptable, avoid confidential research terms where inappropriate, and protect the token as a secret.

Risk: Generated logs can retain business-sensitive research topics or large comment exports.

Mitigation: Restrict access to the logs directory and delete generated logs when they are no longer needed.

Risk: Broad competitor-analysis or trend requests could invoke the skill even when the user did not explicitly ask for Douyin data.

Mitigation: Confirm that Douyin is the intended data source before running collection commands for generic competitor or trend requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-competitor-videos-and-comments)
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

**Output Type(s):** [shell commands, JSON, files, guidance]

**Output Format:** [Pure JSON on stdout with operational logs on stderr; successful data collection can also create timestamped JSON log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js >= 16.14 and GUAIKEI_API_TOKEN; supports keyword, URL, sorting, time-window, content-type, duration, and limit parameters depending on command.]

## Skill Version(s):

1.0.0 (source: package.json, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
