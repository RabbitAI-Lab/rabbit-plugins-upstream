## Description:

Collects public Douyin keyword search, creator post, comment, and real-time hot-list data as structured JSON for content research, competitor analysis, sentiment review, and trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content research teams use this skill to translate natural-language Douyin research requests into Node.js commands that return public search, creator, comment, and hot-list data for analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can activate on broad or ambiguous content-research requests and collect Douyin public data.

Mitigation: Require explicit Douyin/public-data intent and confirm the selected command, target, and result limit before execution.

Risk: Search terms, profile or video URLs, and GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Use the skill only when third-party API transmission is acceptable, keep the token in the environment, and avoid sensitive monitoring targets.

Risk: Search, post, and comment results are saved under the skill's logs directory by default.

Mitigation: Keep logs out of shared repositories or public workspaces and delete them when they are no longer needed.

Risk: The release security verdict is suspicious and requires review before deployment.

Mitigation: Review the security summary and guidance, then run the skill in a constrained environment with only the permissions needed for the intended task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-trend-signal-detector)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search request schema](assets/search_cli_req.schema.json)
- [Search response schema](assets/search_cli_resp.schema.json)
- [Post request schema](assets/post_cli_req.schema.json)
- [Post response schema](assets/post_cli_resp.schema.json)
- [Comment request schema](assets/comment_cli_req.schema.json)
- [Comment response schema](assets/comment_cli_resp.schema.json)
- [Hot-list response schema](assets/hot_cli_resp.schema.json)
- [Guaikei token and help site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON to stdout with logs on stderr and saved JSON files under logs/]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; supports search, post, comment, and hot-list workflows with per-command limits up to 10000 results.]

## Skill Version(s):

1.0.0 (source: package.json, release evidence, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
