## Description:

Extracts packaging improvement tasks and supporting evidence from Amazon reviews about shipping damage, missing items, unboxing, and storage issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to analyze Amazon product reviews for packaging issues and generate evidence-backed packaging improvement recommendations. The workflow checks ARI capabilities, profile data, and quote details before any paid analysis is run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run paid ARI analyses after a quote and explicit confirmation.

Mitigation: Present the quote first, require explicit user confirmation, reuse the quoted requestId for execution, and use status checks after interruptions instead of rerunning confirmed work.

Risk: Security guidance flags that workflow or focus overrides could move the skill outside the intended product packaging scope.

Mitigation: Keep the workflow and focus fixed to product/packaging, do not pass alternate --workflow or --focus values, and rely on the packaged defaults and allowed-command checks.

Risk: ARI processes Amazon product and review data for analysis.

Mitigation: Send only the product/review data needed for the packaging task, avoid secrets or unrelated business data, and stop if the required ARI account or API key is not available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/packaging-improve)
- [ARI service](https://ari.funewa.com)
- [Operation workflow](references/operation-workflow.md)
- [API reference](references/reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown responses with inline shell commands and structured findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ARI quote/status details, review evidence, limitations, and packaging improvement tasks; paid actions require explicit confirmation.]

## Skill Version(s):

1.4.11 (source: evidence release, changelog, _meta.json, script version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
