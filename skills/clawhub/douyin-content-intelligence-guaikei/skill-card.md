## Description:

Supports Douyin public-content research by helping an agent search keywords, collect public account posts, retrieve comments, and check real-time hot topics for content planning and competitive analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn short-video research requests into Douyin-specific CLI calls for topic discovery, competitor monitoring, comment analysis, and trend tracking. It is intended for public Douyin data research and content-planning workflows, not publishing, editing, downloading, or private account access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad auto-invocation may route ambiguous short-video or content-planning requests into Douyin-specific API calls.

Mitigation: Install only in agent environments where Douyin public-data research is expected, and require the agent to confirm platform and task intent before running a CLI command when the user request is ambiguous.

Risk: Generated logs may contain sensitive research topics, public account identifiers, URLs, comments, or competitive-analysis results.

Mitigation: Treat the logs directory as sensitive working data, restrict access to it, and delete logs when they are no longer needed.

Risk: Token errors may display provider contact or website text despite the skill documentation saying runtime token errors should stay neutral.

Mitigation: Review runtime error output before deployment and suppress provider contact or marketing text from agent-visible responses.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/douyin-content-intelligence-guaikei)
- [User documentation](readme.md)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search CLI request schema](assets/search_cli_req.schema.json)
- [Search CLI response schema](assets/search_cli_resp.schema.json)
- [Post CLI request schema](assets/post_cli_req.schema.json)
- [Post CLI response schema](assets/post_cli_resp.schema.json)
- [Comment CLI request schema](assets/comment_cli_req.schema.json)
- [Comment CLI response schema](assets/comment_cli_resp.schema.json)
- [Hot list CLI response schema](assets/hot_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with shell commands; CLI stdout is JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN. CLI runs write task logs under the skill logs directory.]

## Skill Version(s):

1.0.0 (source: server release metadata, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
