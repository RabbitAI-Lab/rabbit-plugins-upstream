## Description:

ljh-xhs helps users assess and decompose Xiaohongshu (RED) image-text commerce posts by grading sample reliability, analyzing cover and content variables, extracting mechanisms, and producing controlled variant plans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[handsomeng](https://clawhub.ai/user/handsomeng)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, ecommerce operators, and content teams use this skill to analyze Xiaohongshu image-text posts, decide whether a sample is reliable enough to learn from, and plan controlled content variants for products or campaigns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create onboarding state and archive business-analysis outputs locally.

Mitigation: Use it in a dedicated workspace, avoid sensitive commercial details unless needed, and tell the agent not to create or update archives for no-persistence runs.

Risk: Weak or non-comparable Xiaohongshu samples can lead to misleading content conclusions.

Mitigation: Apply the built-in sample grading and require controlled variant testing before treating findings as repeatable factors.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Files]

**Output Format:** [Markdown analysis tables and step-by-step guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write onboarding state and archive final deliverables under local ljh-档案 paths when enabled by the user.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
