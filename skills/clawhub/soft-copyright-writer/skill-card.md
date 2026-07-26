## Description: <br>
AI software copyright (ruanzhu) application assistant that guides users through information collection, material checklist generation, source code formatting, design document drafting, application form guidance, and pre-submission verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bettermen](https://clawhub.ai/user/bettermen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users preparing Chinese software copyright registration materials use this skill to assemble material checklists, format source-code excerpts, draft design documentation, fill application forms, and review consistency before submission. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may need to share project files, source code, and application details while preparing filing materials. <br>
Mitigation: Share only the files needed for the filing workflow, remove API keys, passwords, tokens, and other secrets from source code, and review generated materials before submission. <br>
Risk: Generated application guidance or drafted materials may be incomplete, outdated, or inconsistent with current filing requirements. <br>
Mitigation: Verify requirements with the official copyright registration site and confirm that software names, versions, dates, source code, and design-document content match before submission. <br>
Risk: Formatted source-code excerpts could include third-party, open-source, generated, or non-original code that is unsuitable for a filing. <br>
Mitigation: Review formatted code excerpts and include only original core modules, excluding third-party libraries, framework code, generated code, and sensitive configuration. <br>


## Reference(s): <br>
- [软著申请材料清单](references/material-checklist.md) <br>
- [源代码文档格式规范](references/source-code-format.md) <br>
- [软件设计说明书模板](references/design-doc-template.md) <br>
- [软著申请表填写指南](references/application-form-guide.md) <br>
- [常见驳回原因与避坑策略](references/common-rejections.md) <br>
- [软件分类号参考表](references/classification-codes.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Chinese Markdown with tables, checklists, prose guidance, and formatted source-code excerpts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are intended for user review and conversion into application-ready filing materials.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
