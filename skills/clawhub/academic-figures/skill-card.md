## Description:

Helps create publication-ready scientific charts and journal-formatted figures from local data using configurable chart types and quality checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, authors, and developers use this skill to turn local research data into scientific figures, apply journal presets, and check figure readability before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local inputs may contain sensitive research data, and rendering writes figure files, reports, and sidecars.

Mitigation: Use only intended input files, review output locations, and keep sensitive datasets in the local workflow.

Risk: Setup can clear Matplotlib's font cache and batch rendering can start local Python subprocesses.

Mitigation: Run setup and batch jobs deliberately in an appropriate local environment.

Risk: The separately mentioned cloud Pro service requires uploading data.

Mitigation: Review privacy requirements separately before using the cloud service with sensitive data.

## Reference(s):

- [ClawHub release](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Quickstart](references/quickstart.md)
- [Input data formats](references/data-formats.md)
- [Limits and compatibility](references/limits.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides local generation of figure files and optional verification reports.]

## Skill Version(s):

3.7.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
