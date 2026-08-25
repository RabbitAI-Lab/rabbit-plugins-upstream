## Description:

Collects public Douyin search results, creator posts, video comments, and hotlist data as structured JSON for content research, competitor analysis, sentiment review, and trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, researchers, and developers use this skill to run Douyin keyword, creator, comment, and hotlist queries from a Node.js CLI and consume structured JSON for internal content and market research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin research keywords, target URLs, and the GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Use approved tokens and avoid submitting sensitive research targets unless the external service and handling process are acceptable.

Risk: Results are saved automatically under the skill's logs directory, which may retain sensitive research outputs.

Mitigation: Review, protect, rotate, or delete generated logs according to the user's data retention needs.

Risk: Returned media URLs may be mistaken for permission to download or redistribute Douyin content.

Mitigation: Use returned links only for lawful internal research and do not treat them as redistribution authorization.

Risk: Broad activation for short-video research can run Douyin collection even when the user did not explicitly name Douyin.

Mitigation: Confirm the intended platform before invoking the skill for ambiguous or sensitive short-video research.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-audience-voice-reader)
- [User documentation](readme.md)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search CLI request schema](assets/search_cli_req.schema.json)
- [Search CLI response schema](assets/search_cli_resp.schema.json)
- [Comment CLI response schema](assets/comment_cli_resp.schema.json)
- [Post CLI response schema](assets/post_cli_resp.schema.json)
- [Hotlist CLI response schema](assets/hot_cli_resp.schema.json)
- [Guaikei token and usage site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands, Guidance]

**Output Format:** [JSON on stdout with operational messages on stderr and timestamped JSON logs under logs/]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14 or newer and a GUAIKEI_API_TOKEN environment variable; query limits are documented up to 10000 results per request.]

## Skill Version(s):

1.0.0 (source: server release metadata, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
