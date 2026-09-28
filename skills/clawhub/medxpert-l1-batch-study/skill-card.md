## Description:

Helps agents batch-read local documents through a local language model and produce structured summaries and a consolidated list of questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (code only); documentation and theory all rights reserved

## Use Case:

People maintaining document or knowledge-base collections use this skill to generate per-document summaries and a consolidated list of uncertainties with a local model. Medical or regulatory conclusions require human verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated medical or regulatory summaries may be inaccurate or omit important context.

Mitigation: Treat summaries as drafts and verify conclusions against source documents with a qualified human reviewer.

Risk: Writing summary and retry files may affect unintended local files if input paths or task data are untrusted.

Mitigation: Use a dedicated workspace and trusted names.json and outbox contents; check selected output directories before running.

## Reference(s):

- [MedXpert L1 Batch Study release on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/medxpert-l1-batch-study)

## Skill Output:

**Output Type(s):** [Markdown, Text, Files]

**Output Format:** [Markdown summaries and a consolidated question list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes summaries and retry tasks in user-selected local directories.]

## Skill Version(s):

1.1.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
