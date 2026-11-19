## Description:

Creates publication-ready scientific figures from JSON, CSV, or Excel data, with a broad range of statistical chart types and journal export presets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and scientific analysts use it to turn JSON, CSV, or Excel data into static figures for papers and journal submissions, including batch re-rendering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan rated this release suspicious and reported unsafe command execution in the test suite; some files were only partly inspected.

Mitigation: Review test and script commands before running them, and inspect files not fully covered by the scan.

Risk: Installation sources and dependencies are unpinned, and the scan noted capabilities beyond the stated scope.

Mitigation: Pin installation sources and dependency versions, then review the requested actions before use.

Risk: The bundle includes original data that may have sharing restrictions.

Mitigation: Check data permissions and remove sensitive or restricted data before sharing the bundle or its outputs.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Quickstart](references/quickstart.md)
- [Limits and flag interactions](references/limits.md)
- [Python API](references/python-api.md)

## Skill Output:

**Output Type(s):** [Files, Shell commands]

**Output Format:** [Static figure files (TIFF, PNG, PDF, SVG, or EPS) and command-line invocations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated locally from data files or a YAML pipeline; supports journal presets and high-resolution export.]

## Skill Version(s):

8.0.7 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
