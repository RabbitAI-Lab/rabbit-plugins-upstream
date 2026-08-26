## Description:

ARS Academic Reviewer runs a role-separated academic peer review panel that analyzes manuscripts, produces reviewer reports, and synthesizes editorial decisions and revision guidance.

This skill is for research and development only.

## Publisher:

[sedey999](https://clawhub.ai/user/sedey999)

### License/Terms of Use:

CC BY-NC 4.0

## Use Case:

Researchers, authors, reviewers, and academic teams use this skill to simulate multi-perspective manuscript review, check revisions, focus on methodology, run guided review, or calibrate review standards before submission or re-review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads unpublished manuscripts and review materials, which may include confidential or embargoed content.

Mitigation: Install and use it only in environments authorized to process those materials, and avoid submitting sensitive work unless the user has permission.

Risk: Optional cross-model verification can send manuscript content to an external provider when enabled.

Mitigation: Keep cross-model verification disabled for confidential work unless external provider use and any required API keys are explicitly authorized.

Risk: Automated peer-review output can be incorrect, incomplete, or overly authoritative if treated as a final expert judgment.

Mitigation: Use outputs as review support and require human academic review before relying on recommendations, decisions, or revision priorities.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sedey999/skills/ars-academic-reviewer)
- [Review criteria framework](references/guides/review_criteria_framework.md)
- [Editorial decision standards](references/guides/editorial_decision_standards.md)
- [Review panel provenance protocol](references/guides/review_panel_provenance_protocol.md)
- [Cross-model verification](references/shared/cross_model_verification.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown review reports, reviewer configuration cards, editorial decision letters, and revision roadmaps.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured YAML or JSON artifacts when mode-specific schemas are used.]

## Skill Version(s):

1.11.2 (source: SKILL.md metadata and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
