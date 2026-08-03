## Description: <br>
挂接 IMA 知识库的软考高级「系统规划与管理师」智能问答 Skill，针对考生关于考情政策、知识点、真题解析、备考方法和 IT 服务管理理论等问题，检索主库与次库给出可溯源的专业解答。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External learners preparing for the Ruankao advanced System Planning and Management Engineer exam use this skill to get Markdown answers on exam policy, concepts, past-question analysis, preparation methods, and project-material examples. The skill emphasizes source labels, current-policy disclaimers, and refusal of cheating or exam-integrity violations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Answers may include recurring branding and a WeChat contact prompt. <br>
Mitigation: Review generated responses for acceptable branding and off-platform contact language before using them in a governed setting. <br>
Risk: Policy or exam-date guidance may be outdated or unofficial. <br>
Mitigation: Treat policy conclusions as unofficial unless checked against the current official exam notice. <br>
Risk: Optional IMA knowledge-base lookup can retrieve external materials. <br>
Mitigation: Authorize knowledge-base lookup only when external retrieval is intended, and keep source labels in the answer. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/chesaram/skills/ruankao-spgm-qa-1-0-0) <br>
- [IMA 知识库挂接指南](artifact/references/ima_kb_guide.md) <br>
- [问答分类与知识库路由指南](artifact/references/qa_routing.md) <br>
- [系统规划与管理师专业术语速查](artifact/references/spgm_terminology.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown Q&A with a direct conclusion, bullet points, source notes, time-sensitivity notices, signature, and disclaimer] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include IMA knowledge-base source labels; optional external lookup should be authorized by the user.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and manifest.yaml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
