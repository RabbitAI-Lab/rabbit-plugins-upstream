## Description:

Analyzes pet videos, with optional audio, for sneeze and cough events and provides event summaries and report history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, veterinary staff, and boarding-center staff use video analysis to review sneeze and cough frequency and consult past reports. Results support observation, not veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet videos may expose household audio, interiors, or sensitive clinic footage to the Life Emergence cloud service.

Mitigation: Use only footage suitable for cloud upload; review the service's retention, account identity, and deletion practices first.

Risk: The skill silently creates or reuses a persistent identity associated with cloud report history.

Mitigation: Review account and report-history handling before using the skill with sensitive footage.

Risk: Behavioral detections may be mistaken for a medical diagnosis.

Mitigation: Treat results as observations; consult a veterinarian for frequent coughing or breathing difficulty.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-sneeze-cough-detection-analysis)
- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured analysis text or JSON, Markdown report lists, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports can be saved to a local file; historical reports are retrieved from the cloud.]

## Skill Version(s):

1.0.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
