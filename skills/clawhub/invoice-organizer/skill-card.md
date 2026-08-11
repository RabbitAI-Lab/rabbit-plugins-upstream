## Description: <br>
整理发票/票据 PDF，按购买方抬头匹配项目、复制归档，并生成报销清单、消费清单或对账流水。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cat-xierluo](https://clawhub.ai/user/cat-xierluo) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Employees, external professionals, and agents use this skill to extract structured invoice details, match invoices to client or project context, copy the original PDFs into the right reimbursement location, and produce concise reimbursement or expense lists. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Invoice PDFs and nearby project files can contain client, case, tax, travel, and personal data. <br>
Mitigation: Provide only the invoice files and project root needed for the task, and review generated lists so sensitive identifiers such as ID numbers and phone numbers are not included. <br>
Risk: The skill copies invoice files into project reimbursement folders and could place files in the wrong project if the purchaser heading does not match the client context. <br>
Mitigation: Review the proposed destination before execution, require confirmation when the purchaser heading and project client do not match, and copy rather than move or delete originals. <br>
Risk: Reimbursement reasons and trip context may be inferred incorrectly when invoice dates do not clearly align with project timeline events. <br>
Mitigation: Use project context only when it matches the invoice business dates, and mark unsupported fields as pending confirmation instead of fabricating details. <br>


## Reference(s): <br>
- [发票字段识别指南](references/invoice-field-guide.md) <br>
- [清单输出模板](references/output-template.md) <br>
- [项目上下文回溯指南](references/project-context-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown tables, file paths, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated lists use normalized dates and amounts, include totals, and avoid identity numbers or phone numbers.] <br>

## Skill Version(s): <br>
0.1.1 (source: frontmatter and changelog, released 2026-06-22) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
