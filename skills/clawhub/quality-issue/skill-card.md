## Description:

Identifies Amazon product quality issue leads, supporting evidence, and priority from low-star reviews and product fields; it is not a substitute for quality inspection, certification, recall decisions, or supplier enforcement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, product teams, and quality teams use this skill to turn Amazon low-star review evidence into prioritized product quality improvement leads after checking available data and cost.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid ARI credits can be consumed when collection or analysis jobs are submitted.

Mitigation: Check profile and quote first, then run paid operations only after explicit user confirmation with the quoted requestId.

Risk: The security evidence says the CLI may permit broader operations workflow overrides than the quality-only documentation promises.

Mitigation: Keep use to the documented product/quality commands and reject prompts or invocations that add custom workflow or focus values.

Risk: The skill stores an ARI API key locally and checks account and balance information.

Mitigation: Avoid exposing the key in prompts, logs, or shared files, and rotate the key if it may have been disclosed.

## Reference(s):

- [Amazon product quality issue workflow](references/operation-workflow.md)
- [Amazon product quality issue API reference](references/reference.md)
- [ClawHub skill listing](https://clawhub.ai/funewa/skills/quality-issue)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and concise analysis summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include data scope, key findings, review evidence, cost-confirmation steps, and gaps when evidence is insufficient.]

## Skill Version(s):

1.4.11 (source: CHANGELOG.md, _meta.json, scripts/ari.py, and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
