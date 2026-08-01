## Description: <br>
审查中文内容的事实依据、逻辑连贯性、术语规范、翻译腔、AI 写作痕迹与整体结构，适用于文章、报告、教程、项目介绍和说明材料。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gogoingai](https://clawhub.ai/user/gogoingai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Writers, editors, technical authors, and agent workflows use this skill to review Chinese drafts for factual grounding, coherence, terminology, translation artifacts, AI-like phrasing, structure, style fit, and change closure. It can run as a standalone review or as an inline review phase for related writing skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad prompts such as "check this" can trigger a full review that may directly edit Chinese draft content, including sensitive publication wording. <br>
Mitigation: For legal, compliance, or publication-critical text, ask for manual review or a diff before accepting edits. <br>
Risk: Fact checking depends on available source materials and can be incomplete when source files, evaluation context, or cited materials are missing. <br>
Mitigation: Provide source materials and require the review report to state what evidence was checked and where coverage is limited. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gogoingai/skills/wenqu-review) <br>
- [ClawHub metadata homepage](https://github.com/gogoingai/wenqu-skills/tree/master/wenqu-review) <br>
- [Review workflow index](artifact/references/index.md) <br>
- [R0 fact checking](artifact/references/r0-factcheck.md) <br>
- [R1 English terminology](artifact/references/r1-english.md) <br>
- [R2 translation artifacts](artifact/references/r2-translation.md) <br>
- [R3 AI writing patterns](artifact/references/r3-ai-patterns.md) <br>
- [R4 structure review](artifact/references/r4-structure.md) <br>
- [R5 coherence review](artifact/references/r5-coherence.md) <br>
- [R6 style and narrative fit](artifact/references/r6-style-and-narrative-fit.md) <br>
- [R7 change closure](artifact/references/r7-change-closure.md) <br>
- [Chinese terminology glossary](artifact/references/language/glossary.md) <br>
- [Chinese AI-writing humanizer guide](artifact/references/language/humanizer-zh.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown review notes with candidate rewrites and, when authorized, edited article text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May directly revise local draft content during automatic review; manual review mode returns findings and candidate changes first.] <br>

## Skill Version(s): <br>
0.1.15 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
