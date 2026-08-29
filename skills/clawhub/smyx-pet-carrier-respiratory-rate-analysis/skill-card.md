## Description:

Analyzes pet carrier videos or video URLs through a configured service to estimate resting respiratory rate, compare it with safety thresholds, and return non-diagnostic alerts and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to process pet transport videos, estimate breathing frequency, and review structured risk alerts during airline carrier or long-distance transport scenarios. Results are health references only and are not disease diagnoses or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet videos, video URLs, and analysis requests are sent to a configured remote health service.

Mitigation: Use only media the user is authorized to submit, avoid sensitive footage where possible, and verify the configured API environment before execution.

Risk: The skill can create or reuse identity records and store account tokens locally in the workspace data directory.

Mitigation: Run the skill in an isolated workspace, protect local data directories, and clear stored tokens when the workspace is shared or decommissioned.

Risk: Evidence security guidance flags the artifact as suspicious because default configuration may point to development or private service endpoints.

Mitigation: Confirm the intended service host and environment before use, especially for commercial deployments or customer data.

Risk: Respiratory-rate alerts can be misread as clinical diagnosis or treatment guidance.

Mitigation: Present outputs as health-reference monitoring only and direct urgent or abnormal findings to qualified veterinary review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-carrier-respiratory-rate-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Pet carrier respiratory rate API documentation](references/api_doc.md)
- [Common analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown report or JSON analysis output, with optional saved text or JSON file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include respiratory-rate values, threshold alerts, historical report tables, and report links.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter says 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
