## Description:

Creates publication-style scientific figures from research data, with a broad range of chart types and journal formatting options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and developers can turn JSON, CSV, or Excel data into static scientific figures for papers and journal submissions, or batch-render figures with consistent styles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A --pub-ready .repro bundle can include original research data, and generated charts may remain in temporary storage.

Mitigation: Review and de-identify data before sharing bundles, and check temporary storage before cleanup or handoff.

Risk: Runtime behavior and dependency versions were not verified, and generated statistical results or output safeguards may need review.

Mitigation: Independently validate statistical results before publication and use trusted fixtures when checking generated outputs.

## Reference(s):

- [Quickstart](artifact/references/quickstart.md)
- [Data formats](artifact/references/data-formats.md)
- [Limits and supported inputs](artifact/references/limits.md)
- [Python API](artifact/references/python-api.md)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [Static PNG, TIFF, or PDF figures, with command and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Figures are generated locally from supplied data; available chart types and options depend on the input format.]

## Skill Version(s):

7.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
