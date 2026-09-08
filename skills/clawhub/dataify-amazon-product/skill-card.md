## Description:

Collect Amazon product details by ASIN or URL, or collect standard product results by keyword, category URL, or Best Sellers URL. Do not use for reviews, seller profiles, global-marketplace collection, or keyword-and-domain product lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to submit Amazon product collection jobs through Dataify Builder by ASIN, product URL, keyword, category URL, or Best Sellers URL, then monitor and return final JSON results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: DATAIFY_API_TOKEN exposure could grant access to Dataify collection capabilities.

Mitigation: Treat DATAIFY_API_TOKEN as a secret; avoid pasting it into chat or printing it in logs.

Risk: Broad, multi-page, or multi-input collections can consume credits or run longer than expected.

Mitigation: Review collection scope before submission and confirm high-volume or credit-consuming requests before running.

## Reference(s):

- [Modes and Parameters](artifact/references/modes-and-parameters.md)
- [Dataify Builder endpoint](https://scraperapi.dataify.com/builder)
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-amazon-product)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON task or result payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a task ID and resume command if final-result monitoring times out; large result payloads may be summarized while preserving access to the raw result.]

## Skill Version(s):

1.3.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
