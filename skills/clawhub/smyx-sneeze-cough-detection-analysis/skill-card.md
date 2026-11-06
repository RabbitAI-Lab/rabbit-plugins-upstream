## Description:

Analyzes pet videos, optionally with audio, to identify sneeze and cough events and summarize their timing and frequency for behavioral observation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and animal-care teams can analyze submitted pet videos to log suspected sneeze and cough events, review their timing and frequency, and consult historical reports. Results support behavioral observation only and do not provide a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may send private pet footage to Life Emergence, and retention and deletion practices are unclear; the export-only setting may not prevent uploads.

Mitigation: Review before installing, submit only footage you approve sending, confirm retention and deletion practices, and require the export-only behavior to be fixed before relying on it.

Risk: Account credentials are handled without clear user control, and a shared token database needs protection.

Mitigation: Require fixes for credential-as-identity handling, protect the token database, and consider rotating any real API secret already used.

Risk: Behavioral detections can be mistaken for a medical diagnosis.

Mitigation: Treat results as observational only and consult a veterinarian about frequent or concerning symptoms.

## Reference(s):

- [API documentation](references/api_doc.md)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-sneeze-cough-detection-analysis)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Guidance]

**Output Format:** [JSON analysis results and Markdown-formatted historical report lists with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes detected event type, timing, and frequency when returned by the service; intended for behavioral observation, not medical diagnosis.]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
