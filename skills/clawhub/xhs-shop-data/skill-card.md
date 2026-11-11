## Description:

Collects Xiaohongshu marketplace product search results, shop listings, and product details through the AI Data Platform.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cuiyunhai](https://clawhub.ai/user/cuiyunhai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Xiaohongshu marketplace products, retrieve a shop's listings, and inspect product prices, shop sales, and images through a paid data platform.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product search and retrieval calls consume platform points and may incur cost.

Mitigation: Check the current balance and endpoint price before batch requests, and stop pagination when a page returns fewer than 20 items.

Risk: The CLI stores an API key locally and can write response data to files.

Mitigation: Protect the local credential and output files, and grant only the file access the task needs.

## Reference(s):

- [AI Data Platform](https://zlh.aidata366.com)

## Skill Output:

**Output Type(s):** [JSON data, Shell commands, Configuration guidance]

**Output Format:** [JSON responses with command-line and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paginated product data; large responses can be saved to files.]

## Skill Version(s):

1.0.6 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
