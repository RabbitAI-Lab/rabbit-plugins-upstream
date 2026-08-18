## Description:

Generates a professional, client-ready PDF report from a GEO audit with a cover page, score tables, severity-tagged findings, and a 90-day roadmap.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asale-ai](https://clawhub.ai/user/asale-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, consultants, and marketing or SEO teams use this skill to convert a trusted GEO-AUDIT-REPORT.md into styled HTML and PDF deliverables for client review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow runs local shell/browser-based conversion commands and writes HTML/PDF outputs in the working directory.

Mitigation: Run it only in a trusted workspace, use trusted GEO audit reports as input, and review the generated HTML/PDF before sharing.

Risk: Missing or mismatched local browser/PDF tooling can prevent report generation.

Mitigation: Confirm the required local conversion tools are installed before relying on the skill for a client deliverable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/asale-ai/skills/geo-report-pdf)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Files, Guidance]

**Output Format:** [Markdown guidance plus generated HTML and PDF files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes GEO-REPORT.html and GEO-REPORT.pdf in the working directory when the local conversion workflow succeeds.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter says 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
