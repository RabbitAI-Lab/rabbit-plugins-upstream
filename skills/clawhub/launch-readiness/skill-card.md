## Description:

Checks relaunch readiness for an existing Amazon ASIN by using product detail and review evidence to identify redesign or relaunch risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and operators use this skill to assess whether an existing Amazon ASIN has enough product-detail and review evidence for a relaunch or listing revision audit. It supports fixed launch-readiness analysis and explicitly excludes new-product prediction, advertising budget planning, and supply-chain execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use ARI account access and paid operations beyond the fixed launch-readiness workflow it advertises.

Mitigation: Review before installing, check capabilities and profile output first, and approve paid runs only when the quote matches the intended audit/launch task.

Risk: ASIN, product/review, account, and billing-related data may be sent to the ARI service.

Mitigation: Use the skill only if you trust the ARI service with that data and avoid adding unrelated sensitive information.

Risk: A saved ARI API key in ~/.ari/config.json can authorize future account activity.

Mitigation: Protect the local config file and remove the saved key when you stop using the skill.

Risk: Custom workflow, focus, or competitor parameters could broaden the task beyond launch-readiness analysis.

Mitigation: Keep use to the fixed audit/launch workflow and avoid custom workflow, focus, or competitor parameters.

## Reference(s):

- [Operation Workflow](references/operation-workflow.md)
- [API Reference](references/reference.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/launch-readiness)
- [ARI Service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with CLI commands and structured audit findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and an existing ASIN with product-detail and review evidence; paid operations require quote confirmation.]

## Skill Version(s):

1.4.11 (source: server release evidence, _meta.json, CHANGELOG.md, scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
