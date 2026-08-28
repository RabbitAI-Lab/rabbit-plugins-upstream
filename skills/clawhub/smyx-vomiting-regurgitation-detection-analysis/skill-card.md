## Description:

Detects pet vomiting and regurgitation behavior from indoor fixed-camera video, including abdominal contractions, head-forward extension, mouth opening, vomitus on the floor, event timing, frequency, and vomitus characteristics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, animal-care teams, and developers use this skill to analyze pet-area videos for visual signs of vomiting or regurgitation and to produce structured observation reports. The skill is intended for behavior monitoring and report review, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Indoor pet camera footage or provided video URLs are sent to a remote analysis service.

Mitigation: Install only after confirming that the publisher, production endpoints, data retention controls, and cloud-processing terms are acceptable for the footage being analyzed.

Risk: The skill automatically creates or reuses an internal identity and stores tokens locally.

Mitigation: Run it in a controlled environment, limit access to local token storage, and clear or rotate stored credentials according to local security policy.

Risk: Visual analysis can produce false positives or miss behavior that looks similar to vomiting or regurgitation.

Mitigation: Treat results as behavior observations, confirm concerning events with additional context, and seek veterinary review for frequent, severe, bloody, or otherwise concerning symptoms.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-vomiting-regurgitation-detection-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown text with structured JSON analysis, cloud report history, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save analysis output to a file when an output path is provided; list mode returns cloud report history.]

## Skill Version(s):

1.0.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
