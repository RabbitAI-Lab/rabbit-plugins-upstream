## Description:

Collects Douyin video details, comments, user profiles and posts, keyword search results, related terms, and IDs from shared links through the AI Data Platform.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cuiyunhai](https://clawhub.ai/user/cuiyunhai)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and developers use the skill to collect Douyin videos, comments, user and post data, and search results for product selection, creator research, and comment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Collection calls consume platform credits, so batches can incur cumulative charges.

Mitigation: Check the live balance and interface prices before a batch, confirm the budget for tasks over 20 calls, and stop if credits are insufficient.

Risk: API credentials and collected data are stored or written on the local machine.

Mitigation: Keep the API key in the documented local configuration or environment variable, do not share it in logs, and choose an intentional path for saved JSON output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cuiyunhai/skills/douyin-data)
- [AI Data Platform](https://zlh.aidata366.com)

## Skill Output:

**Output Type(s):** [JSON, Files, Analysis]

**Output Format:** [Structured JSON API responses, optionally saved as JSON files, with analysis as requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may be paginated or collected in batches; local JSON output is optional.]

## Skill Version(s):

1.0.8 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
