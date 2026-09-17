## Description:

Analyzes newborn face images or short videos to produce a visual jaundice risk hint based on sclera color and facial skin yellowness, with recommendations for clinical confirmation when risk is elevated.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, clinicians, and developers use this skill to run an AI-assisted visual prescreening workflow for neonatal jaundice from newborn face media. The output supports early risk triage and directs medium or high risk cases to professional bilirubin testing and medical review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles highly sensitive newborn health images, videos, and report queries.

Mitigation: Install and use it only with explicit guardian consent and after confirming retention, deletion, and access controls for infant health records.

Risk: Default networking and hidden identity or account handling may expose sensitive data in ways users do not expect.

Mitigation: Confirm the release uses HTTPS production endpoints, avoids silent account creation or token storage, and clearly documents any account association before deployment.

Risk: Visual jaundice screening can be misleading under poor lighting, color casts, filters, or obstructed facial features.

Mitigation: Require clear naturally lit media and treat medium, high, or repeated abnormal results as prompts for professional bilirubin testing rather than diagnosis.

## Reference(s):

- [API Interface Documentation](references/api_doc.md)
- [Supplemental API Error Codes](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON analysis report with risk level, confidence, recommended action, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save analysis output to a user-specified file and may list prior reports as a Markdown table.]

## Skill Version(s):

1.0.11 (source: ClawHub release evidence; artifact frontmatter reports 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
