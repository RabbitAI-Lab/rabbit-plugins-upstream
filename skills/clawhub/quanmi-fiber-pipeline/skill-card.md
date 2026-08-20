## Description:

A Chinese-language diabetes-management business pipeline for dietary-fiber food companies that guides agents through knowledge intake, product and service design, audience-specific content, validation reports, and sales activation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangjiaocheng](https://clawhub.ai/user/wangjiaocheng)

### License/Terms of Use:

MIT-0

## Use Case:

External operators and developers at dietary-fiber food companies use this skill to run a five-stage workflow covering medical and market knowledge collection, product and service packaging, content generation, CGM-based validation reporting, and sales follow-up. It should be reviewed before use in healthcare, patient-data, or customer-outreach settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill overreaches into patient monitoring and medical-style advice.

Mitigation: Do not use it with real CGM data or patient recommendations until clinician and legal review, explicit consent, privacy controls, retention limits, and human approval gates are in place.

Risk: The skill can support outbound sales automation and partner or customer follow-up.

Mitigation: Require human approval for external outreach, limit follow-up frequency, and verify all claims against reviewed evidence before sending customer-facing material.

Risk: The artifact includes a de-identification mapping file that can support identity re-mapping.

Mitigation: Remove the mapping file before broad sharing or installation, and keep any re-identification material under restricted access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangjiaocheng/skills/quanmi-fiber-pipeline)
- [Task catalog and dependency topology](references/qfp-catalog.md)
- [Task requirements](references/qfp-requirements.md)
- [Exemplar index](references/qfp-exemplars.md)
- [Optional role definitions](references/qfp-roles.md)
- [Pipeline reconstruction process](references/管线重构过程.md)
- [De-identification mapping](references/脱敏前后对照表.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown, tables, structured reports, workflow checklists, and optional JSON data summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces domain plans, content packages, validation summaries, sales materials, and compliance review artifacts; human review is required for medical, privacy, pricing, and partnership decisions.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
