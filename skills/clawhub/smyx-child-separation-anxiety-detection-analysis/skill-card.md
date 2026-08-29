## Description:

Analyzes home-entrance or kindergarten-gate videos to identify crying expressions, clinging actions, and resistance behaviors, then summarizes a mild, moderate, or severe separation-anxiety level with caregiver and teacher guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, teachers, school operators, and developers can use this skill to analyze fixed-camera child drop-off media for visible crying, clinging, and resistance patterns. It produces behavior summaries, anxiety-level classifications, history lookups, and non-diagnostic comfort or escalation suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Child and caregiver videos, media URLs, account identifiers, and report history may be sent to external services.

Mitigation: Use only with explicit guardian and school consent, confirm retention and deletion terms with the publisher, and avoid uploading real child media until data handling is approved.

Risk: The skill may silently create or reuse cloud-linked identities and store tokens.

Mitigation: Review authorization, identity-linking, token storage, and report-access controls before deployment.

Risk: Behavior analysis can be mistaken for clinical diagnosis or produce misleading classifications.

Mitigation: Treat outputs as visual behavior summaries only, review recommendations with caregivers or qualified staff, and seek professional support for severe or persistent concerns.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-separation-anxiety-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](artifact/references/api_doc.md)
- [Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown or JSON analysis report with behavior metrics, anxiety level, recommendations, history tables, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call external APIs to analyze local or URL media and to retrieve historical reports.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact SKILL.md states 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
