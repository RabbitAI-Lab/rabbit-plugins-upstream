## Description:

Provides command-line access to Douyin public data for keyword search, creator post lookup, video comment retrieval, and real-time hot ranking collection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content operators, marketers, and analysts use this skill to retrieve structured public Douyin data for trend tracking, content research, competitive monitoring, and comment analysis. It requires a GUAIKEI_API_TOKEN and should be used only for public data the user is allowed to collect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can bulk collect and locally retain public Douyin data, including comment text, user IDs, nicknames, profile links, and IP-region labels.

Mitigation: Use it only for public Douyin data the user is allowed to collect, limit collection scope, and handle generated logs as retained datasets that may contain personal data.

Risk: Requests and tokens are sent to guaikei.com through the required GUAIKEI_API_TOKEN workflow.

Mitigation: Review data-sharing and authorization requirements before use, keep the API token out of shared logs or prompts, and rotate it if exposed.

Risk: Outputs may include direct media URL fields even though the skill states it does not provide download capability.

Mitigation: Treat media URL fields as sensitive links, avoid using them to download or redistribute content without authorization, and filter them out when they are not needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-get-hot-ranking)
- [Guaikei API token and support site](https://www.guaikei.com)
- [Complete command options](references/options.md)
- [Changelog](references/changelog.md)
- [Search request schema](assets/search_cli_req.schema.json)
- [Search response schema](assets/search_cli_resp.schema.json)
- [Hot ranking response schema](assets/hot_cli_resp.schema.json)
- [Post request schema](assets/post_cli_req.schema.json)
- [Post response schema](assets/post_cli_resp.schema.json)
- [Comment request schema](assets/comment_cli_req.schema.json)
- [Comment response schema](assets/comment_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Node.js shell commands and structured JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands print JSON to stdout, write logs locally, and use stderr for logs or errors.]

## Skill Version(s):

1.0.0 (source: server release, skill metadata, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
