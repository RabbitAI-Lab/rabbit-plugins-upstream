## Description:

Collects public Douyin keyword search results, creator posts, video comments, and hot-list data for short-video marketing research, competitor analysis, sentiment review, and trend monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External marketers, analysts, and developers use this skill to gather public Douyin search, creator, comment, and hot-list data for content planning, competitor research, sentiment analysis, and trend monitoring.

### Deployment Geography for Use:

Global; primarily relevant to Douyin research and subject to access to Douyin and guaikei.com.

## Known Risks and Mitigations:

Risk: The security review says activation rules are broad and should be limited to explicit Douyin research tasks.

Mitigation: Confirm the user intends Douyin data collection before running commands when the platform or data source is ambiguous.

Risk: Keywords, profile or video URLs, result data, and the GUAIKEI token may be sent to guaikei.com.

Mitigation: Use the skill only for approved Douyin research, avoid sensitive inputs unless service use is approved, and protect the token environment variable.

Risk: Successful search, post, and comment runs can leave JSON files under logs that may contain sensitive business research.

Mitigation: Review generated logs after use and delete or control access to files that contain confidential research.

Risk: The security review notes runtime token-error behavior can show a website or phone contact despite the skill document saying it will not.

Mitigation: Treat token errors neutrally, avoid relaying contact details to end users, and review stderr before sharing command output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-collection)
- [Complete options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search request schema](assets/search_cli_req.schema.json)
- [Search response schema](assets/search_cli_resp.schema.json)
- [Post request schema](assets/post_cli_req.schema.json)
- [Post response schema](assets/post_cli_resp.schema.json)
- [Comment request schema](assets/comment_cli_req.schema.json)
- [Comment response schema](assets/comment_cli_resp.schema.json)
- [Hot-list response schema](assets/hot_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON from Node.js CLI commands, with JSON log files written for successful data collection runs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; each run can request up to 10,000 public Douyin records.]

## Skill Version(s):

1.0.0 (source: package.json, references/changelog.md, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
