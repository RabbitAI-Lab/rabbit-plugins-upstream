## Description:

Assists with Chinese undergraduate, master's, course-paper, proposal, and literature-review writing tasks by drafting, revising, reviewing, checking evidence and citations, maintaining long-form consistency, and reducing template-like prose when supported by author-provided or explicitly authorized sources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT-0

## Use Case:

Students, researchers, and academic writers use this skill to plan, draft, revise, and review Chinese academic papers, opening reports, and literature reviews. It is also used to check citation coverage, preserve source attribution, and manage consistency across longer manuscripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Academic writing assistance can introduce unsupported claims, fabricated sources, or content that exceeds the author's actual contribution.

Mitigation: Use author-provided or explicitly authorized sources, keep source attribution visible, and have the author review final academic content under applicable institutional rules.

Risk: External source lookup may expose sensitive research material or rely on sources that have not been fully verified.

Mitigation: Approve web lookup only for the agreed task scope and send only the search terms or public metadata needed for source discovery and verification.

Risk: Cross-session state files may retain project details that the user did not intend to persist.

Mitigation: Allow `.academic-writing/` project state files only when cross-session continuity is desired, and avoid placing sensitive or unnecessary material in saved state.

Risk: Bundled read-only scanners can consume excessive resources on very large or suspicious DOCX/text inputs.

Mitigation: Run scanner scripts only on trusted, appropriately sized files, and apply host file-size and resource limits for untrusted inputs.

## Reference(s):

- [普通中文论文专项叶](references/academic-writing.md)
- [中文论文开题报告专项叶](references/academic-proposal.md)
- [中文论文独立文献综述专项叶](references/academic-literature-review.md)
- [论文 ANTI-AI 语义复核](references/anti-ai-writing.md)
- [学术来源检索与引用覆盖](references/citation-research.md)
- [中文论文长稿稳定与全文一致性](references/long-form-consistency.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Markdown or plain text, with optional shell command snippets for local read-only audit scripts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include outlines, academic prose, revision notes, review findings, citation-check results, source lists, or scanner JSON summaries when requested.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
