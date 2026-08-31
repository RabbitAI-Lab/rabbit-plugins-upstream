## Description:

Assists with Chinese academic paper, proposal, and literature-review outlining, drafting, revision, review, evidence checking, citation checking, long-form consistency, and reducing templated prose when the user provides or authorizes the source material.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Students, academic authors, and reviewers use this skill to work on Chinese undergraduate papers, master's theses, course papers, proposal reports, and standalone literature reviews while keeping claims tied to provided or explicitly authorized sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Drafting and revising academic text can be misused to bypass authorship, disclosure, or institutional academic-integrity rules.

Mitigation: Use the skill under the author's institutional rules and keep outputs tied to the user's own materials, reviewer feedback, or explicitly authorized sources.

Risk: Academic claims, citations, statistics, or conclusions may become misleading if the user has not provided supporting material or has not authorized retrieval.

Mitigation: Treat unsupported items as gaps or suggestions, and authorize source retrieval or provide source text before using claims in final academic writing.

Risk: Local audit scripts read manuscript files supplied to them.

Mitigation: Run helper scripts only on files the user is comfortable letting the local agent read, and treat their findings as candidates for review.

## Reference(s):

- [普通中文论文专项叶](references/academic-writing.md)
- [中文论文开题报告专项叶](references/academic-proposal.md)
- [中文论文独立文献综述专项叶](references/academic-literature-review.md)
- [学术来源检索与引用覆盖](references/citation-research.md)
- [中文论文长稿稳定与全文一致性](references/long-form-consistency.md)
- [论文 ANTI-AI 语义复核](references/anti-ai-writing.md)
- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/chinese-academic-writing-assistant)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Chinese academic prose, Markdown review notes, and optional text or JSON reports from local read-only audit scripts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are constrained to user-provided or explicitly authorized materials; helper-script findings are review candidates rather than automatic corrections.]

## Skill Version(s):

0.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
