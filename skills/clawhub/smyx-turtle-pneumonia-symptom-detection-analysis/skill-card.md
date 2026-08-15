## Description:

Analyzes turtle enclosure camera images or videos to identify visual signs associated with abnormal open-mouth breathing, mucus, nasal discharge, and related pneumonia-risk warnings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External turtle keepers, breeders, veterinary staff, and developers use this skill to submit turtle camera media or URLs for respiratory-sign analysis, risk-level reporting, care guidance, and cloud history lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Turtle videos, images, or URLs may be sent to remote Life Emergence endpoints for analysis.

Mitigation: Submit only media you are permitted to share, and avoid private enclosure footage unless remote processing is acceptable.

Risk: The skill can create or reuse a local identity and store service tokens in the workspace data directory.

Mitigation: Review or clear `data/smyx-api-key.txt` and the local SQLite database when identity linkage or token reuse is not desired.

Risk: The skill can query cloud report history tied to the local identity.

Mitigation: Use an isolated workspace or identity when report history should not be linked to another user or session.

Risk: The output is a visual respiratory-risk warning and not a veterinary diagnosis.

Mitigation: Treat results as screening guidance and consult a professional reptile veterinarian for diagnosis or treatment decisions.

## Reference(s):

- [Turtle pneumonia symptom API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-turtle-pneumonia-symptom-detection-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown and JSON structured analysis reports, with optional saved text output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and historical report tables returned by the remote service.]

## Skill Version(s):

1.0.8 (source: ClawHub server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
