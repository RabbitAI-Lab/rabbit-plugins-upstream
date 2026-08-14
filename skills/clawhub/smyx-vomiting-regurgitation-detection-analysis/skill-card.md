## Description:

Detects pet vomiting or regurgitation in fixed-camera indoor video, including characteristic movements, vomitus appearance, event timing, frequency, and structured observation reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit pet-area video or a video URL for vomiting/regurgitation observation, event timing, frequency summaries, vomitus characteristics, and report retrieval. Results are behavior observations and should not be treated as veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Indoor pet-camera videos or URLs are sent to the publisher's cloud analysis service.

Mitigation: Use only footage you are authorized to upload, and confirm privacy, retention, and access-control assurances before use.

Risk: Analyses are tied to an internally managed account, and access tokens may be stored locally for reuse.

Mitigation: Use a controlled account, review token storage and rotation expectations, and avoid sensitive household footage unless those controls are acceptable.

Risk: Visual behavior analysis can miss or misclassify vomiting-like behavior and is not a medical diagnosis.

Mitigation: Treat results as observations and consult a veterinarian for frequent, severe, bloody, or otherwise concerning vomiting symptoms.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Shared API error documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, guidance]

**Output Format:** [Markdown text with structured JSON-like analysis results and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write the report text to a user-specified output file.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter says 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
