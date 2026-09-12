## Description:

Checks RAG answer claims against retrieved sources, reports grounding coverage, flags unsupported claims as hallucination risks, and requires citations with source provenance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to review retrieval-augmented generation answers before release or publication by checking whether each claim is supported by retrieved material and whether citations carry a source.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A global, unpinned installation can change account-wide skill behavior or pull a later version than the one reviewed.

Mitigation: Install only from a pinned, reviewed version or commit, and avoid the global install path unless account-wide skill changes are intended.

Risk: The checker can mislead users or automation if its output is treated as a conclusive grounding result.

Mitigation: Treat checker output as a heuristic triage signal and require human review before relying on results.

Risk: RAG grounding checks may be inappropriate as the sole basis for regulated, medical, clinical, or other high-stakes decisions.

Mitigation: Use the skill only as an auxiliary review aid in high-stakes domains and defer final decisions to qualified human reviewers and current official sources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/rag-grounding-guard)
- [LGD Hub](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with optional shell commands and checker output text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic checker behavior with exit codes for pass, findings, and usage errors.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 1.2.0 and manifest reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
