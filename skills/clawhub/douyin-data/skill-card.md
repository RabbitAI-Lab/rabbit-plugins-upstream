## Description:

Collects Douyin video details, comments, user profiles and posts, keyword search results, related search terms, and IDs from share links through the Data API platform.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cuiyunhai](https://clawhub.ai/user/cuiyunhai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to collect Douyin content and audience data for product research, creator analysis, and comment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security inspection was partial and notes environment, file, network, and shell capabilities without a declared tool scope.

Mitigation: Review the source and run only the collection commands you understand; keep API keys private.

Risk: Data API requests consume platform credits, and charges can accumulate during batch collection.

Mitigation: Check the current balance and per-call prices before a batch, and set a budget for larger runs.

## Reference(s):

- [Data API Platform](https://zlh.aidata366.com)

## Skill Output:

**Output Type(s):** [JSON data, Files, Shell commands, Guidance]

**Output Format:** [Structured JSON responses or saved JSON files, with command-line guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Large responses can be saved to files.]

## Skill Version(s):

1.0.6 (source: frontmatter; confirmed by release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
