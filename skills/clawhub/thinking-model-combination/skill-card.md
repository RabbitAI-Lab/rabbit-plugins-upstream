## Description:

When one mental model leaves a material blind spot on a multi-domain or high-stakes problem, sequence complementary models with named roles and a conflict rule.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tjboudreaux](https://clawhub.ai/user/tjboudreaux)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to decide when a complex or high-stakes problem needs multiple distinct reasoning models, then synthesize those model outputs into one decision-ready recommendation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make responses more structured for complex decisions, which may make weak or incomplete reasoning look more definitive than warranted.

Mitigation: Use the required conflict rule, model-distinctness check, and final residual-uncertainty statement before acting on the recommendation.

Risk: Over-applying multiple reasoning models can add cost and confusion when a single model already answers the problem.

Mitigation: Apply the skill's stop rule: use one adequate model when it closes the gap, and never exceed three distinct models.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or structured text following the skill's output template]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Caps model combination at three distinct models, requires a predeclared conflict rule, and ends with a single synthesized recommendation.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
