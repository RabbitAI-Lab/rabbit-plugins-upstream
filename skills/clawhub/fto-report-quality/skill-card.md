## Description:

Reviews existing FTO and patent-risk reports, scores their factual support, legal reasoning, and decision usefulness, and generates a structured HTML quality assessment with optional harness validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Legal, IP, product, and patent teams use this skill to review existing FTO reports, patent infringement risk analyses, or exhibition IP risk self-assessments before business decisions. It helps identify missing facts, weak legal reasoning, incomplete mitigation plans, and validation gaps in the report under review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may rely on the generated report as a verified FTO assurance report even though server security evidence flags a mismatch between advertised legal-quality safeguards and shipped scripts.

Mitigation: Treat the output as a draft quality checklist, require review by qualified legal or patent professionals, and verify v9.0 controls and recall calculations before production legal-risk use.

Risk: Independent search and recall features depend on external patent-search tooling and may run in degraded mode when that tooling is unavailable.

Mitigation: Record tool availability in the report and avoid claiming recall rates, missed patents, or absence of missed patents unless real independent patent pools were retrieved and compared.

Risk: The workflow may involve confidential product, patent, or legal-risk materials sent through an external MCP service.

Mitigation: Confirm account authorization, data-handling terms, and approved confidentiality scope before using external search services with sensitive materials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/fto-report-quality)
- [FTO quality standards](references/fto-quality-standards.md)
- [Assessment checklist](references/assessment-checklist.md)
- [Harness checks](references/harness-checks.md)
- [Independent verification guide](references/independent-verification-guide.md)
- [PatSnap open platform](https://open.zhihuiya.com/)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance, files]

**Output Format:** [HTML report file, with optional JSON and HTML harness reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The main report is generated as a fixed-section HTML file; harness validation is only run when explicitly requested.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact describes v9.0 method controls)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
