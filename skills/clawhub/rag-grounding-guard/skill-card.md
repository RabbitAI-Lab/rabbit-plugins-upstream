## Description:

Checks RAG answer claims against retrieved text and flags claims without sufficient source-term coverage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only)

## Use Case:

Developers and other RAG users check answer claims against retrieved material before sharing responses, identifying claims that need closer review or better citations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill declares no filesystem access, but its checker can read local claim and source files.

Mitigation: Review and align file permissions with actual use; provide only intended local inputs.

Risk: The documented command-line arguments differ from those accepted by the checker.

Mitigation: Use the checker's --claims and --sources arguments and correct the usage instructions before operational deployment.

Risk: Broad activation triggers and simple term overlap can produce misleading grounding judgments.

Mitigation: Narrow activation to relevant RAG checks and manually verify consequential claims against their cited passages.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/rag-grounding-guard)
- [LGD theory background](https://github.com/zhaoxinghua09-cell/lgd-theory)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text]

**Output Format:** [Text or Markdown assessment; optional CLI text report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The checker reports claim coverage and lists covered and uncovered claims; it does not establish semantic proof or automatically verify citations.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata; bundled skill frontmatter lists 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
