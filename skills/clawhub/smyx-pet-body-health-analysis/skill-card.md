## Description:

Identifies obesity, emaciation, external injuries, skin abnormalities, and abnormal mental states to help pet owners detect potential health issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners can submit pet photos or videos to receive a structured assessment of body condition, skin, and behavior, with findings and report links to support early follow-up. Results are for health reference and do not replace a veterinarian’s diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account handling may associate reports with the wrong user.

Mitigation: Use a corrected release with reliable sender-to-account separation.

Risk: Export-only mode may still upload media.

Mitigation: Use a corrected release with a working export-only mode; avoid sending sensitive recordings until upload behavior is confirmed.

Risk: Credentials are stored without encryption.

Mitigation: Use a corrected release with protected credential storage.

Risk: Media is uploaded to LifeEmergence, and cloud deletion was not verified.

Mitigation: Confirm the provider’s retention policy before sending sensitive recordings.

Risk: Use may trigger automatic account registration or require paid credits.

Mitigation: Confirm account and credit requirements before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-pet-body-health-analysis)
- [Skill introduction demo](https://lifeemergence.com/sample.html)
- [API interface documentation](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis report, with optional Markdown report list and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include detected conditions, monitoring results, recommendations, and links. Analysis is informational and not a veterinary diagnosis.]

## Skill Version(s):

1.0.19 (source: server-resolved release metadata; artifact frontmatter lists 1.0.23)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
