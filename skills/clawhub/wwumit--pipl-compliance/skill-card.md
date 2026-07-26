## Description: <br>
中国个人信息保护法（PIPL）合规检查、风险评估和文档生成工具，为企业提供PIPL合规自查、风险评估、合规文档生成和跨境传输检查支持。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wwumit](https://clawhub.ai/user/wwumit) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, compliance teams, and privacy practitioners use this skill to run local PIPL self-checks, assess personal information processing risks, and generate draft compliance reports or policy documents for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated legal documents, audit results, and compliance suggestions may be incomplete or unsuitable for a specific organization. <br>
Mitigation: Treat outputs as drafts, independently verify PIPL checklist coverage, and consult qualified counsel before relying on them for compliance decisions. <br>
Risk: The skill reads user-provided compliance data and writes reports or documents to selected paths. <br>
Mitigation: Run it locally on appropriate data, review input and output paths before execution, and protect generated files that may contain sensitive business or personal information. <br>
Risk: Dependency-locking and legal-coverage claims can become stale as laws, guidance, and packages change. <br>
Mitigation: Review the current requirements and authoritative PIPL sources before deployment or material compliance use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/wwumit/skills/pipl-compliance) <br>
- [中国个人信息保护法（PIPL）摘要指南](references/pipl-law.md) <br>
- [PIPL合规检查清单](references/pipl-checklist.md) <br>
- [中国PIPL合规检查清单](references/cn-checklist.md) <br>
- [PIPL风险评估指南](references/risk-assessment-guide.md) <br>
- [PIPL执法案例分析](references/enforcement-cases.md) <br>
- [小型个人信息处理者个人信息保护简化措施规定](references/2026-simplified-measures.md) <br>
- [国家网信办、公安部官方原文](https://www.cac.gov.cn/2026-07/24/c_1786638889704872.htm) <br>
- [PIPL合规检查报告](references/PIPL合规检查报告.pdf) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [CLI guidance plus generated text, JSON, Markdown, HTML, CSV, and document files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally and writes reports or documents to user-selected paths when requested.] <br>

## Skill Version(s): <br>
1.2.3 (source: changelog, package.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
