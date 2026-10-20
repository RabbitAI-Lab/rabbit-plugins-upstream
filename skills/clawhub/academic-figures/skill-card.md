## Description:

Generates publication-ready scientific figures from research data using local chart-rendering tools and journal presets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and developers use this skill to turn study data into static figures for papers and journal submissions, including survival curves, forest plots, and multi-panel charts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Regression tests use a shell-based harness that may be unsafe with untrusted templates or examples.

Mitigation: Do not run regression tests on untrusted templates or examples until the harness is hardened.

Risk: Optional fixes and installation paths may download dependencies; the separate Pro cloud service may upload data.

Mitigation: Use the local renderer by default; enable dependency downloads or Pro cloud use only after approving those boundaries.

Risk: Submission PDFs can contain unnoticed overlapping labels if verification is not enabled.

Mitigation: Run the explicit PDF overlap check or publication-ready mode and inspect figures before submission.

## Reference(s):

- [ClawHub release](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Quickstart](artifact/references/quickstart.md)
- [Data formats](artifact/references/data-formats.md)
- [Limits and flag interactions](artifact/references/limits.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Files]

**Output Format:** [Markdown guidance and static figure files (PNG, TIFF, PDF)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local rendering; journal presets and optional overlap checks for submission PDFs.]

## Skill Version(s):

5.6.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
