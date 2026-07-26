## Description: <br>
PRD智能评审专家（餐饮SaaS专版）。基于14+1章节结构和5大核心框架原则，提供9维度全面评审（章节完整性、需求质量、交互流程、架构设计、餐饮SaaS专项、渐进式复杂度、文档合规性、可交付性、竞品对标）。当用户要求评审PRD、检查需求文档质量、评估产品设计完整性、验证竞品对标深度、做Go/No Go决策时使用。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[woai36d](https://clawhub.ai/user/woai36d) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Product managers, product reviewers, and development teams use this skill to review Chinese PRDs for restaurant SaaS products against a 14+1 chapter structure, five gating principles, and nine scoring dimensions. It produces Go/No Go guidance, graded issue findings, and optional user-confirmed patch plans for PRD improvements. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad PRD review requests may route to this skill even when the user intended a different reviewer. <br>
Mitigation: Confirm that the document is a restaurant SaaS PRD before relying on the scoring rubric or Go/No Go recommendation. <br>
Risk: The optional patching workflow can edit PRD content and update version or changelog text. <br>
Mitigation: Require explicit user approval before applying patches, then review the changed PRD for scope, accuracy, and consistency. <br>


## Reference(s): <br>
- [评审标准手册](references/评审标准手册.md) <br>
- [问题分级标准](references/问题分级标准.md) <br>
- [行业适配规则](references/行业适配规则.md) <br>
- [补丁落地规范](references/补丁落地规范.md) <br>
- [ClawHub skill page](https://clawhub.ai/woai36d/skills/prd-reviewer) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown review report, issue list, and optional patch checklist] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose direct PRD document edits only after explicit user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
