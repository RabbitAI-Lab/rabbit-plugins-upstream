## Description:

Academic Figures generates publication-ready scientific charts from JSON, CSV, Excel, or YAML inputs using local Python tools with journal presets, accessibility options, and PDF quality checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, clinicians, analysts, and developers use this skill to turn local datasets into publication-ready scientific figures, supplementary legends, and accessibility sidecars. It is suited for journal submission workflows that need repeatable chart generation, format export, and quality checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local Python setup and rendering scripts run on user-provided data and local files.

Mitigation: Use a virtual environment, review the commands before execution, and pin dependencies when reproducibility matters.

Risk: Batch or YAML pipeline manifests can trigger many figure-generation actions from one file.

Mitigation: Review pipeline manifests, input paths, and output paths before running them.

Risk: The advertised cloud Pro variant may not have the same local-only privacy posture as this package.

Mitigation: Treat the cloud variant separately and avoid uploading sensitive data unless its data handling terms are acceptable.

Risk: Generated scientific figures can be misleading if chart type, statistics, labels, or input data are wrong.

Mitigation: Use the documented validation, PDF overlap checks, font-size audits, and human review before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Data Format Reference](references/data-formats.md)
- [Limits & Compatibility](references/limits.md)
- [Python API](references/python-api.md)
- [FAQ](references/faq.md)
- [Academic Figures Pitfalls](references/pitfalls.md)
- [Composite Figure Layout Patterns](references/composite-layouts.md)
- [Clinical Lab Parameter Trend Figure](references/clinical-lab-trends.md)
- [Examples](examples/README.md)
- [Template Library](templates/README.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Code, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON/YAML configuration examples, and generated figure files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typical generated artifacts include PDF, PNG, TIFF, EPS, legend text, and alt-text sidecar files.]

## Skill Version(s):

2.6.0 (source: server release metadata and artifact version history)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
