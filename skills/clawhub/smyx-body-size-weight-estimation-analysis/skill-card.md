## Description:

Estimates livestock body measurements and weight from side-view images or video to help track fattening progress.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Farm operators and livestock analysts use side-view images or video of pigs, cattle, or sheep to estimate body dimensions, weight, and fattening stage and to review past reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Farm images or video may be sent to lifeemergence.com for cloud analysis.

Mitigation: Confirm cloud processing and data-sharing approval before submitting farm media or URLs.

Risk: The skill can silently create or reuse an account identity and retain account tokens locally.

Mitigation: Use only where automatic account linkage is acceptable and protect local account data and tokens.

Risk: Cloud-linked report history may be retrieved under the active identity.

Mitigation: Check account access and report visibility before requesting or sharing historical reports.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-body-size-weight-estimation-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis text or JSON; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Estimated measurements, weight, fattening stage, and report links; results are estimates, not formal weighing.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
