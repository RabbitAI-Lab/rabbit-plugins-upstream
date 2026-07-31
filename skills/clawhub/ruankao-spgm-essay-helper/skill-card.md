## Description: <br>
辅助备考软考高级资格「系统规划与管理师」的考生，根据论文题目与本人真实项目背景，结合 IMA 备考资料库生成符合评分标准的论文框架与写作提示。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External learners preparing for the System Planning and Management Engineer essay use this skill to turn a real personal project background and exam topic into a structured Markdown essay framework, writing prompts, terminology suggestions, and a scoring self-check. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional IMA knowledge-base lookups may use a separate integration and may include user-provided exam or project context. <br>
Mitigation: Use lookup only when the user wants exam-prep retrieval, and ask users to provide only project details they are comfortable sharing. <br>
Risk: Essay guidance could become misleading if project details are invented or copied from third-party materials. <br>
Mitigation: Require project background to come from the user's own real experience; use placeholders for missing details instead of fabricating facts. <br>
Risk: Generated frameworks and prompts may still contain accuracy or originality issues. <br>
Mitigation: Tell users to review outputs for correctness and originality, and use retrieved examples only for structure and terminology rather than copying source essays. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chesaram/skills/ruankao-spgm-essay-helper) <br>
- [系统规划与管理师论文框架模板](artifact/references/essay_framework_template.md) <br>
- [系统规划与管理师论文评分标准](artifact/references/essay_scoring_criteria.md) <br>
- [IMA 知识库挂接指南](artifact/references/ima_kb_guide.md) <br>
- [项目背景信息收集模板](artifact/references/project_bg_template.md) <br>
- [系统规划与管理师专业术语速查](artifact/references/spgm_terminology.md) <br>
- [Feedback and issues](https://github.com/ruankao-spgm/essay-helper/issues) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown essay framework with writing prompts, terminology suggestions, word-count guidance, and scoring self-check] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May optionally use scoped IMA knowledge-base lookup for exam-prep references when authorized; falls back to local templates when lookup is unavailable.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
