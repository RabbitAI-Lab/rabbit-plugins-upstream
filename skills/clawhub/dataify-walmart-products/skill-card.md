## Description:

Collect Walmart product records by URL, category URL, SKU, or keyword. Do not use for Amazon, eBay, or general shopping-search results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit and monitor Dataify Builder jobs that collect Walmart product records from product URLs, category URLs, SKUs, or keywords.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release includes under-disclosed generic scraping code and a runtime import path that can load code from outside the skill package.

Mitigation: Review before installation, limit the package to Walmart Builder submission, and remove or separately package generic workflow code and sibling runtime imports.

Risk: Dataify API TOKEN handling and task submission can expose credentials or consume account credits if misconfigured.

Mitigation: Use a scoped or replaceable Dataify API TOKEN, keep tokens out of request URLs and logs, validate collection scope before submission, and monitor credit usage.

## Reference(s):

- [Modes and parameters](references/modes-and-parameters.md)
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-walmart-products)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON task result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit external Dataify Builder jobs and return task status, task IDs, or collected JSON results.]

## Skill Version(s):

1.3.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
