## Description:

Skill Forge is a meta-skill for creating, upgrading, reviewing, and consolidating WorkBuddy skills through structured forge, review, recast, clarity, release, and security gates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j-levee](https://clawhub.ai/user/j-levee)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, skill authors, and agent operators use this skill to design new skills, upgrade existing skills, audit quality, consolidate overlapping local skills, and prepare releases with review and safety gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release enables opt-out local logging and anonymous cloud upload of method-layer feedback signals.

Mitigation: Install only when this feedback collection is acceptable; disable cloud upload with .cloud_optin=off or the stop-upload phrase, and disable local logging with the stop-logging phrase when needed.

Risk: The optional semantic recast mode can send skill metadata to the configured embedding service.

Mitigation: Avoid --semantic unless sending that metadata to the configured service is acceptable; use the default non-semantic recast scan for local-only operation.

Risk: Generated or applied skill proposals may introduce incorrect, misleading, or unsuitable guidance into downstream skills.

Mitigation: Review proposed changes, scan generated skills, and require explicit user approval before publication, consolidation, or deployment.

Risk: Feedback collection defaults can be inherited by skills produced through this workflow.

Mitigation: Review generated skills for inherited telemetry behavior and make opt-out controls clear before release.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/j-levee/skills/cjg-skill-forge)
- [Publisher Profile](https://clawhub.ai/user/j-levee)
- [Distribution Readiness Card](artifact/references/discovery.md)
- [Skill Introduction](artifact/references/intro.md)
- [Signal Specification](artifact/references/signals.md)
- [Cloud Configuration Schema](artifact/references/cloud-config-schema.md)
- [Security Audit Report](artifact/references/security-audit.md)
- [Skill Review Rubric](artifact/references/skill-review-rubric.md)
- [Skill Consolidation Guide](artifact/references/skill-consolidation.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional code blocks, shell commands, JSON configuration, review reports, and proposed skill-file changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include forge plans, quality audits, recast reports, release checklists, publishing commands, and generated or revised skill artifacts for user review.]

## Skill Version(s):

2.9.9 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
