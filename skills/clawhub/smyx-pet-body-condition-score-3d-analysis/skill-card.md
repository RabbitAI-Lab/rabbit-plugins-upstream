## Description:

Analyzes pet videos through a cloud service to estimate a 1–9 body condition score and provide a structured report or account-linked report history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, caregivers, and developers use this skill to assess body condition from pet videos and review past reports for weight-management planning; its estimates are not veterinary diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media or supplied URLs are sent to lifeemergence.com services.

Mitigation: Obtain permission before submitting pet media and review the external service's data-handling terms.

Risk: The skill may silently create or reuse an identity and store service tokens in a local workspace database.

Mitigation: Review before installation, restrict workspace access, and avoid shared or multi-user environments unless identity and token isolation are verified.

Risk: Cloud history queries may retrieve reports linked to the current identity.

Mitigation: Check which identity is active and authorize access before requesting historical reports.

Risk: Visual body condition estimates may differ from a hands-on veterinary assessment.

Mitigation: Use results for weight-management reference only and consult a veterinarian for clinical assessment.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-body-condition-score-3d-analysis)
- [Pet analysis API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis results and report links; Markdown tables for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can be saved to a file; historical reports are retrieved from the cloud.]

## Skill Version(s):

1.0.10 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
