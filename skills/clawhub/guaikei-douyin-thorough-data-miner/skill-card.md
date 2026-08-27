## Description:

This skill helps agents collect structured public Douyin data through keyword search, creator post retrieval, comment collection, and real-time hot ranking queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Content researchers, marketers, and analysts use this skill to gather public Douyin search results, creator posts, comments, and hot-list data for content research, competitor analysis, sentiment exploration, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A third-party Douyin API provider receives the configured token, keywords, and target URLs.

Mitigation: Use a dedicated GUAIKEI_API_TOKEN, protect it as a secret, and install the skill only where sharing those request details with the provider is acceptable.

Risk: Search, creator post, and comment results are saved under the skill's logs directory by default.

Mitigation: Review, retain, or delete generated logs according to the user's data handling requirements before sharing workspaces or outputs.

Risk: Broad activation rules can trigger the skill for generic research or trend questions.

Mitigation: Narrow activation rules or require explicit confirmation before running Douyin data collection in multi-step research workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-thorough-data-miner)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Usage documentation](readme.md)
- [Complete option reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search request schema](assets/search_cli_req.schema.json)
- [Search response schema](assets/search_cli_resp.schema.json)
- [Post request schema](assets/post_cli_req.schema.json)
- [Post response schema](assets/post_cli_resp.schema.json)
- [Comment request schema](assets/comment_cli_req.schema.json)
- [Comment response schema](assets/comment_cli_resp.schema.json)
- [Hot ranking response schema](assets/hot_cli_resp.schema.json)
- [Guaikei token and support site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [shell commands, json, files, guidance]

**Output Format:** [JSON on stdout with logs written to files for search, post, and comment commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; command outputs follow the JSON schemas in assets/ and can return up to 10000 items per request.]

## Skill Version(s):

1.0.0 (source: evidence release, package.json, changelog, constants)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
