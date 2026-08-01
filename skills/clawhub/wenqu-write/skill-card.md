## Description: <br>
基于证据撰写中文内容的完整流程，涵盖调研、规划、提纲、逐节写作、审查、配图、翻译和发布准备，适用于文章、报告、教程、项目介绍、解读和说明材料。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gogoingai](https://clawhub.ai/user/gogoingai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to plan, draft, revise, review, translate, and prepare Chinese technical articles, reports, tutorials, project introductions, source-code explanations, and related explanatory materials. It emphasizes evidence-backed writing workflows, persistent article context, material tracking, and quality checks before publication. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create durable writing profiles, article context, preferences, material indexes, and draft files. <br>
Mitigation: Use it only where persistent writing state is acceptable, and review or delete generated wenqu-skills and .gogoingai files that contain information you do not want retained. <br>
Risk: The skill can scan and index project source files or local materials to build article evidence. <br>
Mitigation: Run it only in repositories where code and material indexing is acceptable, and inspect collected material indexes before sharing drafts or generated outputs. <br>
Risk: External articles, papers, code excerpts, and user-provided materials may contain instruction-like text that should not control the agent. <br>
Mitigation: Treat collected materials only as evidence for article facts, and keep instruction priority anchored to the user request and the skill workflow. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/gogoingai/skills/wenqu-write) <br>
- [Project Repository](https://github.com/gogoingai/wenqu-skills) <br>
- [Skill Homepage](https://github.com/gogoingai/wenqu-skills/tree/master/wenqu-write) <br>
- [Reference Index](references/INDEX.md) <br>
- [Writing Style Guide](references/writing/style-guide.md) <br>
- [Writing Anti-Patterns](references/writing/anti-patterns.md) <br>
- [Planning Questionnaire](references/planning/questionnaire.md) <br>
- [Materials Governance](references/planning/materials-governance.md) <br>
- [Content Provenance Guidance](references/planning/content-provenance.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown drafts, structured planning files, review notes, article material indexes, and concise command or code snippets when needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create durable project files under wenqu-skills/ and profile or preference files under .gogoingai when the writing workflow requires persistent context.] <br>

## Skill Version(s): <br>
0.1.15 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
