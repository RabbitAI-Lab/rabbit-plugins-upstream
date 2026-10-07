## Description:

Guides batch reading of a document collection with a local language model, recovering structured summaries and retrying failed reads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (.py code only); all rights reserved (documentation and theory)

## Use Case:

Knowledge-base maintainers and document reviewers use the skill to batch-read local documents, save per-document summaries and questions, and retry unsuccessful reads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow reads and writes the inbox, outbox, document hub, and output folders supplied by the user.

Mitigation: Grant access only to intended folders and review the destination paths before running it.

Risk: Summary and retry output may be in Chinese despite the multilingual description.

Mitigation: Review generated summaries for language suitability and accuracy before sharing them.

Risk: WebSearch permission is declared, though the inspected local recovery helper does not need network access.

Mitigation: Restrict WebSearch permission when an offline-only workflow is required.

## Reference(s):

- [MedXpert L1 Batch Study on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/medxpert-l1-batch-study)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown summaries and command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Per-document summaries include three core points, table highlights, and questions; failed jobs can be retried.]

## Skill Version(s):

1.1.3 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
