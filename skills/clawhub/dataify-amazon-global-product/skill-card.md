## Description:

Collects Amazon global-marketplace product data by product URL, category URL, keyword, or keyword plus brand.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit Dataify Amazon global product collection jobs, monitor the asynchronous task, and return collected product results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Amazon product URLs, keywords, domains, brand filters, and related collection parameters to Dataify.

Mitigation: Install and use it only when sending those collection inputs to Dataify is intended.

Risk: A Dataify API TOKEN is required for Builder requests.

Mitigation: Keep DATAIFY_API_TOKEN scoped to Dataify, store it in the environment, and do not paste or print it in chat.

Risk: High-volume, multi-page, or broad collection jobs can consume more Dataify credits.

Mitigation: Review consequential parameters such as maximum count, page turning, filters, and domain before submitting larger jobs.

## Reference(s):

- [Modes and parameters](references/modes-and-parameters.md)
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-amazon-global-product)
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON task/result output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit API calls to Dataify Builder and wait for final task results when DATAIFY_API_TOKEN is configured.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
