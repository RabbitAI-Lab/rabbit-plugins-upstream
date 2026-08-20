## Description:

Uses a GUAIKEI API token to help an agent search public Douyin content, retrieve creator posts, collect video comments, and query real-time Douyin hot lists for content research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users and content research teams use this skill to gather public Douyin search results, creator post lists, comments, and hot-list data for topic selection, competitor analysis, sentiment review, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Douyin search terms, target URLs, token-bearing requests, and usage metadata to guaikei.com.

Mitigation: Use it only when that third-party API exposure is acceptable, treat GUAIKEI_API_TOKEN as a secret, and avoid invoking it for unspecified research tasks.

Risk: Saved logs may contain scraped public comments, profile metadata, and sensitive search interests.

Mitigation: Regularly review, protect, or delete the generated logs directory according to the user's data-retention needs.

Risk: The server security summary marks the release for review because it can trigger on generic research requests.

Mitigation: Require explicit user intent for Douyin public-data collection and confirm scope before running broad searches or comment collection.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-deep-comments)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
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

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [JSON on stdout with logs on stderr and saved JSON log files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js >=16.14 and GUAIKEI_API_TOKEN; individual retrieval commands support limits up to 10000 records.]

## Skill Version(s):

1.0.0 (source: package.json, changelog, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
