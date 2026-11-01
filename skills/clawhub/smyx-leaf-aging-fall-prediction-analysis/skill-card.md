## Description:

Analyzes recurring houseplant images for signs of leaf aging and predicts likely leaf-fall windows with care suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External plant owners and plant-care operators use this skill to review recurring images of indoor plants, identify leaf aging trends, and plan care around predicted leaf fall.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected videos or URLs and account identifiers may be sent to a cloud service, while account setup may retain credentials without clear storage or retention disclosures.

Mitigation: Avoid using private footage until upload behavior, account setup, credential storage, and retention practices are clarified.

Risk: The export-only option may still allow analysis uploads, and the API URL option may not change the destination.

Mitigation: Assume selected videos or URLs may be sent to the configured service; do not rely on these options to prevent uploads or redirect data.

## Reference(s):

- [Leaf Aging Analysis API Documentation](references/api_doc.md)
- [Analysis API Errors](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Release Page](https://clawhub.ai/18072937735/skills/smyx-leaf-aging-fall-prediction-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis report (JSON); Markdown report lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include aging indicators, predicted fall windows, at-risk leaves, cause hints, care suggestions, and report links.]

## Skill Version(s):

1.0.18 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
