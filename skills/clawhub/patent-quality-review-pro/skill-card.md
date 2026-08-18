## Description:

Patent Quality Review Pro reviews uploaded PDF or Word patent application documents across all evaluation indicators, incorporates reexamination and invalidation decision-point guidance, supports chemistry, mechanical, electrical, and general AHP weighting with user confirmation, and generates a standard two-page Word quality evaluation report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent attorneys, patent operations teams, and agent users use this skill to evaluate patent application drafting quality, confirm the appropriate technical-domain weighting scheme, and produce a structured Word quality evaluation table with issues and revision suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes sensitive patent application materials and writes generated reports to an output directory.

Mitigation: Use an approved local workspace or controlled output path, confirm access controls for generated Word reports, and avoid sharing review inputs outside the authorized environment.

Risk: The Word generator may open the output folder after report creation.

Mitigation: Pass --no-open-output when automatic opening is not desired or when running in a shared or unattended environment.

Risk: Live patent-data conclusions depend on an authorized patent MCP service.

Mitigation: Confirm the PatSnap/Open Platform account authorization and enabled MCP tools before relying on database-backed novelty or inventiveness conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/patent-quality-review-pro)
- [Publisher profile](https://clawhub.ai/user/yuanzhian-patsnap)
- [PatSnap Open Platform](https://open.zhihuiya.com/)
- [Issue 9 patch note](references/issue9_patch.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance, JSON review data, and generated .docx Word reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-confirmed AHP domain selection and authorized patent MCP access for live data; the Word generator can open the output directory unless disabled.]

## Skill Version(s):

1.0.0 (source: evidence.release.version and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
