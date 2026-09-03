## Description:

Douyin Detail helps agents retrieve and analyze public Douyin search results, creator posts, comments, content metrics, and trending topics through Node.js command tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operations teams use this skill to collect public Douyin data for content research, competitor monitoring, trend tracking, and comment analysis. Agents route user requests to the appropriate Node.js CLI, request missing keywords or URLs when needed, and return structured results for downstream summaries or reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin query terms, public links or IDs, and GUAIKEI_API_TOKEN are sent to the disclosed third-party API at guaikei.com.

Mitigation: Install and run the skill only when that data transfer is acceptable; avoid using sensitive business terms or links unless the user has authorized the API use.

Risk: Local JSON logs can retain comments, author metadata, keywords, links, and business research outputs.

Mitigation: Review, restrict access to, and delete generated files under logs/ when retained Douyin data is no longer needed.

Risk: The skill is limited to public Douyin data and does not support private, hidden, or logged-in content.

Mitigation: Use it only for public-data workflows and ask for a keyword, public video URL, public profile URL, sec_uid, or aweme_id before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/douyin-detail)
- [Guaikei API token and service site](https://www.guaikei.com)
- [Complete CLI options](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)
- [Search request schema](artifact/assets/search_cli_req.schema.json)
- [Search response schema](artifact/assets/search_cli_resp.schema.json)
- [Creator posts request schema](artifact/assets/post_cli_req.schema.json)
- [Creator posts response schema](artifact/assets/post_cli_resp.schema.json)
- [Hot list response schema](artifact/assets/hot_cli_resp.schema.json)
- [Comments request schema](artifact/assets/comment_cli_req.schema.json)
- [Comments response schema](artifact/assets/comment_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [Shell commands, JSON data, Files, Guidance]

**Output Format:** [Markdown guidance with Node.js command examples and structured JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command output is written as JSON to stdout; operational logs are written to stderr and local JSON files under logs/; execution requires GUAIKEI_API_TOKEN.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata, SKILL.md frontmatter, package.json, references/changelog.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
