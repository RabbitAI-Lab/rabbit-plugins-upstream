## Description:

Analyzes litter-box videos to track cats’ visits, summarize frequency and duration against historical baselines, and flag behavioral changes for veterinary follow-up; it does not diagnose disease.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and care teams use the skill to review litter-box videos, monitor each cat’s visit frequency and duration over time, and spot changes that may warrant veterinary attention.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags automatic service-account enrollment, unsafe access-key handling, and video uploads even in advertised export-only mode.

Mitigation: Wait for fixes to export-only behavior and credential handling, plus clear controls for account enrollment. Confirm retention and deletion terms before submitting private videos; --api-url currently does not change the processing destination.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-litter-box-usage-monitor-analysis)
- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Guidance]

**Output Format:** [Structured analysis report in JSON or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes visit frequency and duration, historical comparisons, behavioral alerts, and report links; alerts are not medical diagnoses.]

## Skill Version(s):

1.0.13 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
