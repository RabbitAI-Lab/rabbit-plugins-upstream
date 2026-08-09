## Description:

Helps agents retrieve and summarize Douyin creator posts, image/text content, short-drama series, and recent publishing data through SocialDataX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect Douyin creator works and short-drama series data for content research, creator benchmarking, account tracking, and recent publishing analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SocialDataX API key for authenticated data requests.

Mitigation: Provide the key only through the SOCIALDATAX_API_KEY environment variable and confirm that using SocialDataX for these requests is acceptable before installation.

Risk: Broad pagination such as --all can consume credits or fetch large result sets.

Mitigation: Use --max-items, --pages, or page-token based collection when the task needs bounded data retrieval.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin-creator-videos)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON data returned by SocialDataX commands or MCP tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY; broad pagination can fetch large result sets or consume credits, so use page or item limits when bounded collection is needed.]

## Skill Version(s):

0.1.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
