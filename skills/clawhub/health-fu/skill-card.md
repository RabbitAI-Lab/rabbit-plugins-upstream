## Description: <br>
整合健康教练傅康 AI分身是一个中文营养健康科普智能体，使用云端 ima 知识库和本地 Markdown 知识库回答体重管理、代谢指标、消化、营养素、补充剂、饮食结构和生活方式问题，同时避免诊断、替代医生或调整用药。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kevinfu1218](https://clawhub.ai/user/kevinfu1218) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Chinese-speaking users use this skill for nutrition and lifestyle education, including weight management, blood sugar/lipid/blood pressure topics, digestive issues, micronutrients, supplements, diet structure, and preparation for or interpretation of clinician visits. It is intended for public education and does not provide diagnosis, replace clinicians, or adjust medication. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may treat nutrition education as medical care for symptoms, abnormal tests, medications, pregnancy, children, elderly users, chronic disease, or urgent concerns. <br>
Mitigation: The skill should maintain its stated boundaries: do not diagnose, replace clinicians, or adjust medication, and direct users to licensed clinicians or urgent care when appropriate. <br>
Risk: A local health profile may contain sensitive health information. <br>
Mitigation: Create or update a local profile only with user consent, keep it local, and confirm key facts before using stored health context. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kevinfu1218/skills/health-fu) <br>
- [Safety Boundaries](references/safety-boundaries.md) <br>
- [Consultation Patterns](references/consultation-patterns.md) <br>
- [健康档案（本地）](references/health-records.md) <br>
- [知识库索引](references/knowledge-base/index.md) <br>
- [营养素参考数据](references/knowledge-base/nutrients.md) <br>
- [常见食物营养成分](references/knowledge-base/foods.md) <br>
- [常见健康问题的循证饮食建议](references/knowledge-base/conditions.md) <br>
- [补充剂循证评价](references/knowledge-base/supplements.md) <br>
- [中国居民膳食指南 2022 核心内容](references/knowledge-base/guidelines.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, guidance, markdown] <br>
**Output Format:** [Plain text Chinese responses with source labels and medical-boundary disclaimers] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Usually under 500 Chinese characters; asks at most one or two follow-up questions per turn.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
