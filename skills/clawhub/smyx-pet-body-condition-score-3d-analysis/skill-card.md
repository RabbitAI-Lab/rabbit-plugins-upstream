## Description:

Analyzes multi-angle pet videos through a cloud service to estimate a 1–9 body condition score and provide structured observations without diagnosing disease.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and developers use the skill to assess body condition from pet videos and retrieve historical analysis reports for weight-management monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet videos or video URLs are sent to a configured cloud service.

Mitigation: Confirm the service and obtain appropriate consent before sending pet footage or links.

Risk: The skill silently creates or reuses an account identity, stores authentication tokens in workspace data, and uses that identity to access historical reports.

Mitigation: Review account creation and token storage before installation; restrict access to workspace data and historical reports.

Risk: Visual body-condition estimates may differ from a hands-on assessment.

Mitigation: Treat scores as weight-management observations, not diagnoses, and consult a veterinarian for clinical assessment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-body-condition-score-3d-analysis)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown]

**Output Format:** [Structured JSON or Markdown report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include historical report links or save results to a file.]

## Skill Version(s):

1.0.11 (source: server-resolved ClawHub release; artifact frontmatter lists 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
