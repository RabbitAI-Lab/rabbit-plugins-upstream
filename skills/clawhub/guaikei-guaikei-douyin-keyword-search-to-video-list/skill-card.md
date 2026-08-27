## Description:

A command skill for retrieving public Douyin keyword search results, creator posts, video comments, and hot topic data for content analysis and operations workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operations teams use this skill to collect structured public Douyin data for keyword research, trend tracking, competitor monitoring, comment analysis, and downstream reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin queries, links, and the GUAIKEI API token are sent to guaikei.com.

Mitigation: Use only approved tokens, confirm that data sharing with guaikei.com is acceptable for the intended workflow, and avoid sending sensitive or unnecessary inputs.

Risk: The skill can collect large public social-media datasets, including comments, author data, and video metadata.

Mitigation: Limit each run to the minimum dataset needed for the task and use it only for legitimate public-data analysis.

Risk: Retrieved public social-media data may be retained in local JSON log files.

Mitigation: Review local log files after use and delete them when they are no longer required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-guaikei-douyin-keyword-search-to-video-list)
- [Guaikei API token and support site](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search request schema](assets/search_cli_req.schema.json)
- [Search response schema](assets/search_cli_resp.schema.json)
- [Post request schema](assets/post_cli_req.schema.json)
- [Post response schema](assets/post_cli_resp.schema.json)
- [Comment request schema](assets/comment_cli_req.schema.json)
- [Comment response schema](assets/comment_cli_resp.schema.json)
- [Hot topic response schema](assets/hot_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with bash command examples and JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI commands write pure JSON to stdout, logs to stderr, and may retain retrieved datasets in local JSON log files.]

## Skill Version(s):

1.0.0 (source: release evidence, SKILL.md metadata, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
