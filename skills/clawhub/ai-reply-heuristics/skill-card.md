## Description:

Estimates AI-writing trace strength in a supplied text using deterministic heuristics for cliche density, dash frequency, sentence-length uniformity, and parallel structures, returning a 0-100 score and three-level band as a heuristic aid rather than a verdict.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, reviewers, and governance teams can use this skill to ask an agent or CLI workflow for a quick heuristic signal about whether text has formulaic AI-writing traits. It is intended to support human review, not to make automated attribution, legal, compliance, employment, academic, medical, or other high-stakes determinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented one-line global installer can fetch code at install time and modify agent skills from an unpinned source.

Mitigation: Prefer a reviewed release or commit, verify provenance when available, and install only this skill into a user-scoped skills directory.

Risk: Heuristic AI-writing signals can produce false positives or false negatives if used as a final attribution decision.

Mitigation: Use the score as a review aid only and require human review for consequential decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/ai-reply-heuristics)
- [Publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Plain text or JSON from the included CLI, with Markdown usage guidance for agents.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic standard-library Python script; outputs a 0-100 score, a risk band, matched cliche signals, counts, and a disclaimer.]

## Skill Version(s):

1.0.0 (source: server release evidence; artifact frontmatter reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
