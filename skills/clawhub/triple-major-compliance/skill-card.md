## Description: <br>
国企采购领域的"三重一大"决策合规 AI 辅助技能，基于用户上传的企业内部制度，辅助判定采购事项是否属三重一大、校验决策程序合规性、生成内部参考合规报告。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
国企采购经办人、法务合规人员、纪检监察人员和董事会办公室秘书 use this skill to triage procurement matters, map decision bodies, check procedure order, identify common compliance risks, and draft internal reference reports. It is an aid for internal review and does not replace legal advice or the enterprise's governance decision. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Users may treat an AI-generated compliance report as legal advice or a final governance decision. <br>
Mitigation: Use outputs only as internal reference material and route final judgments through enterprise governance bodies, counsel, or the relevant regulator. <br>
Risk: Procurement facts, supplier identities, amounts, state secrets, commercial secrets, or personal data may be exposed in prompts. <br>
Mitigation: Provide only the minimum necessary information and redact enterprise names, supplier names, exact amounts, state secrets, core commercial secrets, and personal data. <br>
Risk: Legal citations, enterprise thresholds, or knowledge-base outputs may be stale, incomplete, or inconsistent with the user's internal policy. <br>
Mitigation: Verify citations and outputs against current law, the uploaded enterprise policy, and professional legal or compliance review before relying on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chesaram/skills/triple-major-compliance) <br>
- [企业清单结构化示例](references/企业清单结构化示例.md) <br>
- [会议纪要模板](references/会议纪要模板.md) <br>
- [决策主体与事项映射](references/决策主体与事项映射.md) <br>
- [四类事项判定路由](references/四类事项判定路由.md) <br>
- [城投集团清单对照](references/城投集团清单对照.md) <br>
- [常见问题 FAQ](references/常见问题FAQ.md) <br>
- [法规索引](references/法规索引.md) <br>
- [负面案例库](references/负面案例库.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown reports, decision-path summaries, risk checklists, meeting-minute drafts, and internal reference statements.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs depend on user-provided internal policies and built-in reference materials; users should verify citations and conclusions before relying on them.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
