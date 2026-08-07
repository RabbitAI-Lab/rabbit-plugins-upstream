## Description: <br>
多Agent并行辩论式创意决策引擎。输入模糊创意→三独立视角(建构/解构/数据锚定)并行分析→Critic+Defender交叉验证→20分制量化评分→可执行策划案+Skill双格式输出。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vane1981](https://clawhub.ai/user/vane1981) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external creators, and developers use this skill to evaluate fuzzy creative, business, IP, and planning ideas through multiple agent perspectives, adversarial critique, data grounding, and a 20-point scorecard. It produces an executable planning proposal, scoring card, evidence table, and optional agent-skill output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad planning and brainstorming triggers may invoke the skill during ordinary requests. <br>
Mitigation: Use explicit invocation or scoped activation where possible, and review generated plans before relying on them. <br>
Risk: The data-grounding phase may use web searches based on user-provided ideas. <br>
Mitigation: Avoid confidential business plans, regulated advice, client data, and proprietary concepts, or redact sensitive details before use. <br>
Risk: Task-derived ideas may be persisted to local topic files for future reuse. <br>
Mitigation: Review and delete stored topic files after sensitive work, or disable knowledge accumulation when handling private projects. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/vane1981/skills/creative-origin-engine) <br>
- [Project homepage](https://github.com/Vane1981-2011/creative-origin-engine) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown planning documents with scorecards, evidence tables, and agent skill files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include locally persisted topic notes for future reuse when the skill's knowledge accumulation behavior is used.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release metadata, frontmatter, config.yaml, and changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
