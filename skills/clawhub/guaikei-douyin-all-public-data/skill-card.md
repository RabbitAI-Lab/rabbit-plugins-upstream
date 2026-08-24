## Description:

This skill helps agents collect and structure public Douyin data for keyword search, creator post retrieval, comment analysis, and real-time trending queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, analysts, marketers, and content researchers use this skill to gather public Douyin search results, creator posts, comments, and trending topics as structured JSON for content planning, competitor analysis, sentiment review, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can broadly collect public Douyin data and send research terms, account targets, or comment targets to an external API.

Mitigation: Review planned collection before execution and confirm it complies with applicable law, platform terms, and organizational data-handling rules.

Risk: The skill can automatically save large JSON datasets locally under logs/.

Mitigation: Run it only where exported data can be protected, and delete saved JSON files when they are no longer needed.

Risk: The skill requires a GUAIKEI_API_TOKEN for API access.

Mitigation: Use a dedicated token supplied through the environment, protect it on shared machines, and avoid exposing token values in logs or shared command history.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-all-public-data)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search request schema](assets/search_cli_req.schema.json)
- [Search response schema](assets/search_cli_resp.schema.json)
- [Post request schema](assets/post_cli_req.schema.json)
- [Post response schema](assets/post_cli_resp.schema.json)
- [Comment request schema](assets/comment_cli_req.schema.json)
- [Comment response schema](assets/comment_cli_resp.schema.json)
- [Hot list response schema](assets/hot_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands, Guidance]

**Output Format:** [JSON on stdout, diagnostic logs on stderr, and timestamped JSON files under logs/.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14 or newer and GUAIKEI_API_TOKEN. Public data collection commands support up to 10000 records per request.]

## Skill Version(s):

1.0.0 (source: package.json, changelog, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
