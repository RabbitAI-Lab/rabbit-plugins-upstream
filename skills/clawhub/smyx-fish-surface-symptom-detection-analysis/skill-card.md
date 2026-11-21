## Description:

Analyzes fish images and video for visible white spots, skin or fin-base redness, and fin damage, then returns symptom findings and confidence scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium keepers, aquarium staff, and ornamental fish farmers can use the skill to review fish images or video for visible surface symptoms and receive structured findings for follow-up. Its output is an aid to observation, not a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan flags remote data handling, account and token management, and a possible mismatch between an option and whether analysis runs.

Mitigation: Before use, review whether the remote destination and persistent account or token handling are acceptable, and confirm the behavior associated with the selected option. Avoid sending media or identity data you do not want handled that way.

Risk: The security scan was partial because a referenced path was missing, leaving evidence about that reference incomplete.

Mitigation: Review the missing reference and treat the security assessment as incomplete until it has been covered.

Risk: Image-based symptom findings may be uncertain and could be mistaken for a veterinary diagnosis.

Mitigation: Treat findings as visual observations and consult a qualified aquatic veterinarian for diagnosis or treatment decisions.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-fish-surface-symptom-detection-analysis)
- [API interface reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured symptom findings with confidence scores, human-readable reports, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Visual symptom classifications and follow-up guidance; not a veterinary diagnosis or medication plan.]

## Skill Version(s):

1.0.17 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
