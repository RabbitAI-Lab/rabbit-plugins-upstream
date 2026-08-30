## Description:

Identifies obesity, emaciation, external injuries, skin abnormalities, and abnormal mental states, helping pet owners detect health issues promptly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and care teams use this skill to analyze pet images or videos for body condition, skin abnormalities, external injuries, mental-state indicators, and historical report lookup. Results are health reference outputs and are not veterinary diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet photos, videos, and identity-linked metadata are sent to publisher backend services.

Mitigation: Use the skill only when users are comfortable with publisher-hosted processing of pet media and associated metadata.

Risk: The skill silently creates or reuses local user identities and stores tokens or user records locally.

Mitigation: Review local identity storage and token handling before installation, especially in shared workspaces.

Risk: Default configuration includes non-HTTPS private-network development endpoints.

Mitigation: Correct endpoint configuration for normal use and prefer HTTPS/TLS service URLs.

Risk: Health analysis output may be mistaken for a veterinary diagnosis.

Mitigation: Treat reports as health reference information and consult a veterinarian when abnormalities are detected.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-body-health-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, json]

**Output Format:** [Markdown or JSON analysis report with optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May output historical report lists as Markdown tables; media inputs are limited to supported image/video formats and size limits documented by the artifact.]

## Skill Version(s):

1.0.14 (source: server release metadata; artifact frontmatter is 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
