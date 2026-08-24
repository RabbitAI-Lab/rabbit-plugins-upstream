## Description:

Collects public Douyin search results, creator posts, video comments, and hot-list data through Node.js CLI commands for short-video research and content analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content operations teams use this skill to research Douyin topics, monitor competitor accounts, inspect public comments, and retrieve hot-list data for analysis workflows. It does not provide posting, editing, account-growth, or private-backend access capabilities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad short-video or trend-research prompts may trigger the skill even when the user did not explicitly ask to query Douyin.

Mitigation: Ask for explicit user confirmation before running a command and confirm that the task should use public Douyin data.

Risk: Queries, Douyin URLs, and returned results are sent to guaikei.com and saved locally in the skill logs directory.

Mitigation: Avoid sensitive research terms, disclose the external request before use, and periodically delete local logs for sensitive projects.

Risk: The skill requires an API token to run.

Mitigation: Keep GUAIKEI_API_TOKEN in the environment, do not paste it into prompts or logs, and stop on authentication errors instead of retrying.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-keyword-search-to-video-list)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Manifest repository metadata](https://github.com/um-why/douyin-search-openclaw)
- [Guaikei token and support site](https://www.guaikei.com)
- [Complete CLI options](references/options.md)
- [Release changelog](references/changelog.md)
- [Search CLI request schema](assets/search_cli_req.schema.json)
- [Search CLI response schema](assets/search_cli_resp.schema.json)
- [Post CLI request schema](assets/post_cli_req.schema.json)
- [Post CLI response schema](assets/post_cli_resp.schema.json)
- [Comment CLI request schema](assets/comment_cli_req.schema.json)
- [Comment CLI response schema](assets/comment_cli_resp.schema.json)
- [Hot list CLI response schema](assets/hot_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [shell commands, JSON, configuration, guidance]

**Output Format:** [JSON results from stdout, with operational logs on stderr and saved JSON log files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0 or newer and a GUAIKEI_API_TOKEN environment variable; single command runs may return up to 10000 public Douyin records.]

## Skill Version(s):

1.0.0 (source: server release evidence, package.json, skill metadata, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
