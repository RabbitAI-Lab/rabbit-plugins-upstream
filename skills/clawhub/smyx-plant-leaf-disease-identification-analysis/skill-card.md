## Description:

Identifies likely plant leaf diseases from submitted leaf images or videos, reports lesion features and confidence, and returns general prevention direction without specific chemical treatment plans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, growers, greenhouse operators, home gardeners, and farm inspectors use this skill to analyze plant leaf media for visible disease symptoms, likely disease type, confidence, general care direction, and prior report lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted images, videos, or URLs may be sent to LifeEmergence cloud services and tied to an internally managed identity.

Mitigation: Avoid sensitive internal URLs or private media unless the publisher provides acceptable retention, deletion, and account-linking controls.

Risk: The skill stores account records or tokens locally and automatically reuses them for account-linked API calls.

Mitigation: Review local storage behavior before installation and run the skill only in an environment where local token storage is acceptable.

## Reference(s):

- [API documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown or JSON analysis report with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include likely disease type, lesion features, confidence score, general prevention direction, report link, and historical report table.]

## Skill Version(s):

1.0.8 (source: ClawHub release metadata; artifact frontmatter says 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
