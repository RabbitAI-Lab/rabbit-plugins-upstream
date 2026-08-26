## Description:

Collects public Douyin search, creator post, comment, and trending-topic data through Node.js CLI commands and returns structured JSON for content research and analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Content researchers, marketing analysts, and agents use this skill to look up public Douyin videos, creator posts, comments, and hot lists for trend research, competitor analysis, topic planning, and sentiment review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad automatic activation may cause agents to run Douyin lookups on ambiguous user requests.

Mitigation: Confirm ambiguous requests before invoking the skill, especially when the user has not clearly asked for Douyin or short-video public-data analysis.

Risk: The skill sends requests to a third-party API provider and depends on GUAIKEI_API_TOKEN.

Mitigation: Use the skill only where third-party API use is acceptable, keep GUAIKEI_API_TOKEN private, and avoid exposing the token in logs or shared transcripts.

Risk: Returned public comments or profile data may be saved automatically in local JSON logs.

Mitigation: Review and periodically clean the logs directory, and avoid retaining results that contain personal or sensitive information longer than needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-public-videos-dataset)
- [Full options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search request schema](assets/search_cli_req.schema.json)
- [Search response schema](assets/search_cli_resp.schema.json)
- [Post request schema](assets/post_cli_req.schema.json)
- [Post response schema](assets/post_cli_resp.schema.json)
- [Comment request schema](assets/comment_cli_req.schema.json)
- [Comment response schema](assets/comment_cli_resp.schema.json)
- [Hot list response schema](assets/hot_cli_resp.schema.json)
- [Guaikei token and help site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Structured JSON emitted to stdout with optional local JSON log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; logs returned public data under logs/; documented command limits allow up to 10000 results per request.]

## Skill Version(s):

1.0.0 (source: release evidence, package.json, references/changelog.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
