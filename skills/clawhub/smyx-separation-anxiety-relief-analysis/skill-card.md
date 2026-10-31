## Description:

Analyzes video of pets left alone for possible separation-anxiety behaviors and returns structured observations and comfort recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and boarding staff use the skill to review video of a pet left alone, identify possible anxiety-related behaviors, and get structured observations and comfort suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private reports may be mixed when an account is shared.

Mitigation: Use an isolated account and avoid shared-agent use until account isolation is confirmed.

Risk: Video may be uploaded to the Life Emergence service even when no-analysis is selected.

Mitigation: Do not submit private recordings until no-analysis behavior is confirmed and enrollment, retention, deletion, and charges are understood.

Risk: The package should not be relied on for continuous camera monitoring or automatic operation of comfort devices.

Mitigation: Treat the skill as an on-demand analysis aid; verify any proposed comfort action and device setup yourself.

Risk: Credential handling may be unsafe for shared use.

Mitigation: Avoid using sensitive credentials in shared environments until safer credential handling is available.

## Reference(s):

- [API interface notes](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-separation-anxiety-relief-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured behavior report with observations, severity, recommendations, and report links; JSON or Markdown detail]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Behavior observations and recommendations are not a medical diagnosis.]

## Skill Version(s):

1.0.13 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
