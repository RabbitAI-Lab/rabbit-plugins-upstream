## Description:

Find Precedent helps an agent find and compare relevant historical cases, such as contracts, proposals, projects, incidents, decisions, designs, or exceptions, without treating similarity as authority.

This skill is ready for commercial/non-commercial use.

## Publisher:

[raguets](https://clawhub.ai/user/raguets)

### License/Terms of Use:

MIT-0

## Use Case:

Knowledge workers, legal and commercial teams, project teams, and agents use this skill to search authorized historical sources for comparable prior cases and extract reusable lessons for a current decision. It is intended for precedent-aware analysis, not for treating prior approvals, contracts, proposals, or decisions as current authority.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Precedent searches may touch sensitive internal contracts, proposals, incident records, or decision records.

Mitigation: Connect the skill only to document sources the agent is authorized to read.

Risk: Historical precedent can be stale, materially different, or mistaken for current approval authority.

Mitigation: Require outputs to explain comparability, surface material differences, separate reusable lessons from stale or customer-specific commitments, and state the limits of analogy.

## Reference(s):

- [Overpowered suite](https://github.com/raguets/overpowered)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown-style structured text with precedent comparisons, reusable lessons, material differences, pattern synthesis, and limits of analogy.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires authorized access to relevant historical knowledge sources such as RAG, search, document repositories, or equivalent tools.]

## Skill Version(s):

1.0.1 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
