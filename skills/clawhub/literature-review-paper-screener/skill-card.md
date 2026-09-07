## Description:

The Literature Review Paper Screener helps an internet-enabled local agent find medical-science literature, build per-paper evidence records, submit one record per paid LoomLoom cloud task for screening, audit the results, and render Excel Paper Sheet and Reading List outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ez-hq](https://clawhub.ai/user/ez-hq)

### License/Terms of Use:

MIT

## Use Case:

Developers, researchers, and students use this skill to assemble evidence-backed medical-science literature review paper pools, screen them through a paid private cloud workflow, and receive audited Paper Sheet and Reading List workbooks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research topics, assignment context, and per-paper evidence records are sent to the selected LoomLoom cloud platform.

Mitigation: Install and run only when this data sharing is acceptable, and confirm the selected platform before each cloud submission.

Risk: Cloud screening is a paid workflow with one fee unit per paper.

Mitigation: Confirm the platform, paper row count, per-task fee, and total estimated cost before every submission.

Risk: Cloud screening can only evaluate evidence supplied by the local agent and may have limited support for Level C or D records.

Mitigation: Do not claim unavailable full-text review; preserve evidence availability levels and flag evidence-limited papers in the delivery summary.

Risk: Incorrect bibliographic metadata can contaminate the screened paper pool.

Mitigation: Run the metadata validation gate against PubMed or Crossref, block mismatched or invalid records before handoff, and record partially verified identifiers explicitly.

Risk: The private cloud template and prompts are proprietary and are not covered by the local MIT license.

Mitigation: Use the local package under its MIT terms while avoiding reproduction or publication of the private cloud template instructions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ez-hq/skills/literature-review-paper-screener)
- [Architecture Reference](artifact/references/architecture.md)
- [Evidence Package Schema](artifact/references/evidence-package-schema.md)
- [Metadata Validation Gate](artifact/references/metadata-validation-gate.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Excel files, Audit reports]

**Output Format:** [Markdown guidance with inline shell commands, per-paper JSON evidence records, audit JSON, and XLSX workbooks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one evidence record per paper, validates returned cloud results locally, and renders merged Paper Sheet and Reading List workbooks.]

## Skill Version(s):

1.4.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
