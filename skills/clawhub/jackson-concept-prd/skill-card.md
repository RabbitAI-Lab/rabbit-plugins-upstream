## Description:

Transcribes a confirmed Jackson concept model into PRD specs, including a central overall PRD, wyx-compatible colocated CONCEPT.md files, and flow-grouped SYNCS.md.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and product engineers use this skill to convert a confirmed Jackson concept design into persistent PRD documentation. It organizes the application-level PRD, per-concept specifications, and flow-grouped sync specifications without adding model content not present in the confirmed design.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated PRD documents may contain incorrect or misleading content if the confirmed concept model is incomplete or stale.

Mitigation: Review generated documents against the confirmed concept model before accepting them into a project.

Risk: Broad Chinese requests for specification documents may invoke this workflow and produce Chinese-structured output.

Mitigation: Use the skill only when Jackson concept-model PRD generation is intended, and verify that the generated document structure matches the target workflow.

## Reference(s):

- [WYSIWID paper](https://arxiv.org/abs/2508.14511)
- [Beyond Objects](https://arxiv.org/abs/2606.27258)
- [conceptbox](https://github.com/61040-fa25/conceptbox)

## Skill Output:

**Output Type(s):** [Markdown, Files, Guidance]

**Output Format:** [Markdown PRD documents and structured specification files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces docs/prd/README.md, per-concept CONCEPT.md files, and flow-grouped SYNCS.md content when applied by an agent.]

## Skill Version(s):

0.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
