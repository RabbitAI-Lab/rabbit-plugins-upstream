## Description:

Collects public Douyin search, creator post, comment, and hot-list data through Node.js CLI commands and returns structured JSON for content research, competitor analysis, sentiment review, and trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to gather public Douyin videos, posts, comments, user-facing metrics, and hot-list data for marketing research, competitor monitoring, public-sentiment review, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin search terms, URLs, IDs, and GUAIKEI_API_TOKEN are sent to the provider API.

Mitigation: Use the skill only for explicit Douyin research tasks, provide the token through the environment, and avoid submitting sensitive or private identifiers.

Risk: Fetched public social data is automatically saved in the skill logs directory.

Mitigation: Limit filesystem access to appropriate users and delete logs when the collected data is no longer needed.

Risk: Broad triggers may run the skill during general short-video research even when Douyin is not named.

Mitigation: Confirm the user intends to use Douyin data before executing commands in ambiguous workflows.

Risk: The security summary notes that some runtime behavior exceeds the skill's stated limits.

Mitigation: Start with small limits, review generated JSON before using it downstream, and stop if observed behavior differs from the documented command contract.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-data-funnel)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Guaikei token and support site](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search request schema](assets/search_cli_req.schema.json)
- [Search response schema](assets/search_cli_resp.schema.json)
- [Post request schema](assets/post_cli_req.schema.json)
- [Post response schema](assets/post_cli_resp.schema.json)
- [Comment request schema](assets/comment_cli_req.schema.json)
- [Comment response schema](assets/comment_cli_resp.schema.json)
- [Hot-list response schema](assets/hot_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Files, Guidance]

**Output Format:** [Pure JSON on stdout, operational messages on stderr, and JSON result files saved under logs/]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js >= 16.14 and GUAIKEI_API_TOKEN; documented command limits allow up to 10000 items per request.]

## Skill Version(s):

1.0.0 (source: server release metadata, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
