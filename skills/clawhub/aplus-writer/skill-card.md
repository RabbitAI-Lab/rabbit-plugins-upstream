## Description:

Plans Amazon A+ content modules, information hierarchy, and buyer-question responses using Amazon product-detail and review evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon operators and marketplace content teams use this skill to plan A+ content from product and review evidence before drafting or updating listing content. It is limited to A+ planning and does not create images, run ads, or publish Amazon pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shipped CLI can run broader paid product-operation workflows than the narrow A+ planning description suggests.

Mitigation: Review before installing, trust the ARI service before use, and constrain agent use to the documented listing/aplus workflow and allowed commands.

Risk: The skill stores an ARI API key locally when configured and contacts ari.funewa.com for account, balance, quote, collection, and analysis operations.

Mitigation: Protect the local API key, use only the documented ARI endpoint, and verify account and balance details with check or quote commands before paid work.

Risk: Paid operations can spend credits after explicit confirmation.

Mitigation: Require a quote and user confirmation before run or collect commands, and use the original request or task status command after interruptions instead of rerunning paid work.

## Reference(s):

- [Amazon A+ Content Planning Workflow](references/operation-workflow.md)
- [Amazon A+ Content Planning API Reference](references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text with inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include product evidence summaries, A+ content recommendations, quote or status details, and setup guidance.]

## Skill Version(s):

1.4.11 (source: server release evidence, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
