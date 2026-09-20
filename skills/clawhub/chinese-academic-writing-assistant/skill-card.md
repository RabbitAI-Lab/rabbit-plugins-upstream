## Description:

中文论文、开题报告与文献综述的起草、改写、审稿和证据核对。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to draft, revise, review, and check Chinese undergraduate, master's, course-paper, proposal, and literature-review writing from author-provided materials or explicitly authorized sources. It is intended to support structure, evidence mapping, citation checking, long-form consistency, and prose quality while preserving academic integrity limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Academic-writing assistance could be misused to overstate evidence or replace the author's own academic contribution.

Mitigation: Use the skill only with author-provided materials, explicitly authorized sources, and the stated integrity limits; keep citation support and institutional requirements in scope during review.

Risk: DOCX or unusually large manuscript inputs may create avoidable exposure when running local audit scripts.

Mitigation: Avoid running the DOCX audit scripts on untrusted or unusually large documents, and treat script output as candidate findings that require review.

Risk: Project continuity files under .academic-writing/ may create or update local writing state when authorized.

Mitigation: Authorize state-file use only when local continuity is desired, and compare stored state against the latest manuscript materials before relying on it.

## Reference(s):

- [普通中文论文专项叶](references/academic-writing.md)
- [中文论文开题报告专项叶](references/academic-proposal.md)
- [中文论文独立文献综述专项叶](references/academic-literature-review.md)
- [论文 ANTI-AI 语义复核](references/anti-ai-writing.md)
- [学术来源检索与引用覆盖](references/citation-research.md)
- [中文论文长稿稳定与全文一致性](references/long-form-consistency.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown or plain text, with optional JSON reports from read-only audit scripts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include academic prose, outlines, review findings, citation coverage notes, source-check results, and localized revision guidance; scanner results are review candidates rather than final semantic judgments.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
