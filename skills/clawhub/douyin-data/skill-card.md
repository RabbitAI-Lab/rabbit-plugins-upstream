## Description:

Collects Douyin video details, comments, user profiles and posts, keyword search results, related search terms, and share-link IDs through a metered data API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cuiyunhai](https://clawhub.ai/user/cuiyunhai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use the skill to collect Douyin content and account data for product selection, creator, and comment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API requests consume account credits, so batch collection can incur costs.

Mitigation: Check the live balance and per-call prices before a batch, estimate its total cost, and confirm the budget for large runs.

Risk: The skill uses an API key, makes network requests, and can write collected results to local files.

Mitigation: Keep the key in environment variables, avoid exposing it in logs or shared output, use a trusted endpoint, and choose output paths deliberately.

Risk: The security review was partial and does not establish complete coverage.

Mitigation: Review the skill's network and file-writing scope before enabling it in the intended environment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/cuiyunhai/skills/douyin-data)
- [Data API platform](https://zlh.aidata366.com)
- [Data API registration](https://zlh.aidata366.com/auth/register)

## Skill Output:

**Output Type(s):** [JSON, Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [JSON API responses and optional JSON files, with Markdown usage guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports pagination and batch collection; large responses can be saved to local files.]

## Skill Version(s):

1.0.5 (source: SKILL.md frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
