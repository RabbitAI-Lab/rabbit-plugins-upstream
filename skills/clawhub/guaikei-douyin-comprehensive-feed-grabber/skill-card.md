## Description:

Retrieves structured public Douyin data for keyword video search, creator post fetching, video comment reading, and real-time hot ranking analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content teams, marketers, and analysts use this skill to research public Douyin videos, creator posts, comments, and hot rankings for topic planning, competitor analysis, sentiment review, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can trigger on broad short-video research requests, including cases where the user did not explicitly ask for Douyin.

Mitigation: Confirm that Douyin public-data collection is intended before running collection commands.

Risk: Queries, Douyin URLs, and collection results are sent to guaikei.com.

Mitigation: Avoid submitting sensitive or unnecessary queries and only use the skill for approved public-data research.

Risk: Generated logs may contain public comments and profile identifiers.

Mitigation: Review, protect, or delete generated logs, and retain only the data needed for the task.

Risk: The skill depends on a private API token.

Mitigation: Keep GUAIKEI_API_TOKEN in the environment only, do not paste it into prompts or logs, and rotate it if exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-comprehensive-feed-grabber)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search request schema](assets/search_cli_req.schema.json)
- [Search response schema](assets/search_cli_resp.schema.json)
- [Post request schema](assets/post_cli_req.schema.json)
- [Post response schema](assets/post_cli_resp.schema.json)
- [Comment request schema](assets/comment_cli_req.schema.json)
- [Comment response schema](assets/comment_cli_resp.schema.json)
- [Hot ranking response schema](assets/hot_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; the invoked CLIs emit structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and may save JSON logs containing public Douyin result data.]

## Skill Version(s):

1.0.0 (source: server release evidence and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
