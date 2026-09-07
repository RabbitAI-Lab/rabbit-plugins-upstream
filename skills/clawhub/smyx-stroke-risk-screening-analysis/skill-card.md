## Description:

Combines TCM facial feature recognition with physiological indicator information to provide early warnings of high-risk stroke conditions such as cerebral infarction and cerebral hemorrhage, and provides lifestyle intervention suggestions and medical guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and health-oriented application agents use this skill to screen stroke risk from facial images or videos with optional physiological indicators, then receive a structured risk report, lifestyle suggestions, medical guidance, and report links. The output is a screening aid and does not replace professional medical examination or diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends facial images or videos, optional physiological values, and an internally resolved user identity to a configured backend service.

Mitigation: Use only after an explicit privacy and consent review, confirm the backend operator and data-handling terms, and avoid sensitive real-user media during evaluation.

Risk: The skill can silently create or reuse identities and persist tokens or profile data in the workspace data directory.

Mitigation: Run it in an isolated workspace, review and delete stored local data after use, and require clear account-linkage and token-deletion controls before production deployment.

Risk: The artifact includes dev/private endpoint defaults and documentation that still references pet-health analysis rather than stroke screening.

Mitigation: Require a reviewed production configuration and corrected documentation before release or installation in a user-facing environment.

Risk: The generated stroke risk report is a screening aid and may be mistaken for a medical diagnosis.

Mitigation: Present results as health-risk screening only, keep the non-diagnostic disclaimer visible, and direct high-risk users to professional medical care.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-stroke-risk-screening-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](artifact/references/api_doc.md)
- [Analysis API interface documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown and JSON-style structured analysis reports with optional report export links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can print a basic, standard, or JSON-detail report; historical report queries return structured records.]

## Skill Version(s):

1.0.12 (source: server release evidence; artifact frontmatter reports 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
