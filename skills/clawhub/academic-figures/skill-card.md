## Description:

Helps researchers create publication-ready scientific figures from JSON, CSV, or Excel data using local chart-generation tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and developers use this skill to choose chart types, prepare figure commands, and render journal-oriented plots and statistical visualizations from their own data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local scripts read user-supplied data and write figures or reports.

Mitigation: Review commands and output locations before running them, and de-identify sensitive clinical data.

Risk: The advertised Pro/cloud service has a different data-sharing boundary from local rendering.

Mitigation: Treat cloud use as a separate decision and review its data-handling terms before uploading data.

## Reference(s):

- [Academic Figures on ClawHub](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Quickstart](artifact/references/quickstart.md)
- [Limits and compatibility](artifact/references/limits.md)
- [Python API](artifact/references/python-api.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Running the suggested commands locally can produce figure files and optional accessibility text.]

## Skill Version(s):

3.8.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
