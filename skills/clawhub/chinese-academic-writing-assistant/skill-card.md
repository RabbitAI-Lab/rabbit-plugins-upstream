## Description: <br>
Assists with Chinese undergraduate, master's, and course-paper writing tasks, including outlines, drafted sections, revisions, reviews, proposals, literature reviews, citation checks, long-manuscript consistency, and evidence-bounded style refinement. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Students, researchers, and academic writers use this skill to plan, draft, revise, and review Chinese academic manuscripts from provided materials, school requirements, and explicitly authorized source searches. It is intended to keep claims, citations, research status, and manuscript structure within the evidence supplied or verified. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill could be misused to create unsupported academic work or substitute for the author's own scholarly contribution. <br>
Mitigation: Use it for evidence-bounded planning, drafting, revision, and review; require author-provided or verified materials for claims, research process, data, citations, results, and conclusions. <br>
Risk: Citation or source errors could make a manuscript misleading even when citation markers are present. <br>
Mitigation: Use the skill's source authorization and evidence-led citation workflow, and treat local citation audit output as structural candidates rather than proof of semantic support. <br>
Risk: Manuscripts may contain private, unpublished, or institutionally sensitive material. <br>
Mitigation: Do not search or transmit source material unless explicitly authorized; limit authorized searches to public-source queries and avoid uploading non-public full text or sensitive research material. <br>
Risk: Long-draft project notes may retain manuscript state on disk. <br>
Mitigation: Use local project-state notes only when helpful for long manuscripts, and disable or avoid them when the user does not want persistent notes. <br>


## Reference(s): <br>
- [中文论文写作](SKILL.md) <br>
- [普通中文论文专项叶](references/academic-writing.md) <br>
- [中文论文开题报告专项叶](references/academic-proposal.md) <br>
- [中文论文独立文献综述专项叶](references/academic-literature-review.md) <br>
- [学术来源检索与引用覆盖](references/citation-research.md) <br>
- [中文论文长稿稳定与全文一致性](references/long-form-consistency.md) <br>
- [论文 ANTI-AI 语义复核](references/anti-ai-writing.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Chinese prose, Markdown outlines or review tables, optional shell commands, and optional JSON findings from read-only local audit scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May maintain local long-draft project notes when useful; search is used only after explicit authorization.] <br>

## Skill Version(s): <br>
0.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
