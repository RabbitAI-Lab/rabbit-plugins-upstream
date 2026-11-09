## Description:

协调多个分析角色，为大额或安全关键商品提供基于公开证据的选购比较与风险审计。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhashushu](https://clawhub.ai/user/zhashushu)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use this skill to compare products, check safety and quality records, assess pricing, and receive a recommendation with its evidence and limitations. It is aimed especially at expensive purchases and safety-critical categories.

### Deployment Geography for Use:

China, primarily Mainland China

## Known Risks and Mitigations:

Risk: The scanner reports broad activation triggers and a potential to distort evidence and product recommendations.

Mitigation: Review the workflow before use and require current, checkable sources for consequential product claims and recommendations.

Risk: The partial scan could not resolve several local references, so their safety was not established.

Mitigation: Resolve and review the referenced files before deployment.

Risk: The scanner identifies installation and revision review as relevant to this release.

Mitigation: Pin and review the installer and the exact skill revision before installation.

## Reference(s):

- [Skill release on ClawHub](https://clawhub.ai/zhashushu/skills/bilei-team)
- [Category profiles](references/category_profiles.md)
- [Report format and evidence requirements](references/output_template.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, Text]

**Output Format:** [Chinese Markdown product comparison and recommendation report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Layered presentation with a concise recommendation, supporting comparisons, and an evidence appendix; may include a shareable version.]

## Skill Version(s):

1.0.6 (source: release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
