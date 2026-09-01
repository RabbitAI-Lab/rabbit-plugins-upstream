## Description:

安装后通过 MedGroup OAuth 登录授权，查询 DRG/DIP 城市与规则、检索 ICD 编码、执行分组和结算测算、查询 CC/MCC。用户提出医保分组、编码或规则核对任务时使用；不需要 API Key，不替代临床诊断、医保审核或实际结算。

This skill is ready for commercial/non-commercial use.

## Publisher:

[u201013903](https://clawhub.ai/user/u201013903)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to work with the MedGroup remote MCP service for DRG/DIP rule lookup, ICD code search, grouping, settlement scenario calculations, and CC/MCC checks. Outputs are decision-support estimates for medical insurance grouping and coding review, not final clinical diagnosis, coding approval, insurance audit, or reimbursement determinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends task data to the MedGroup remote MCP service after OAuth authorization.

Mitigation: Install only if the user is comfortable authorizing MedGroup through OAuth, and do not ask users for API keys, tokens, account passwords, or other credentials.

Risk: DRG/DIP grouping and settlement calculations may be mistaken for official clinical, coding, audit, or reimbursement decisions.

Mitigation: Label settlement results as scenario estimates and state that outputs do not replace clinical diagnosis, final medical coding review, insurance audit, or local official settlement documents.

Risk: Medical grouping workflows can involve patient-identifying information.

Mitigation: Prefer synthetic or de-identified data and avoid requesting or repeating patient names, ID numbers, contact details, admission numbers, or similar identifiers.

## Reference(s):

- [MedGroup homepage](https://medgroup.medchat.fun)
- [ClawHub skill page](https://clawhub.ai/u201013903/skills/medgroup-drgdip-skill)
- [Publisher profile](https://clawhub.ai/user/u201013903)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, API calls]

**Output Format:** [Markdown responses with tool-derived DRG/DIP, ICD, rule, grouping, CC/MCC, and settlement values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OAuth authorization to the MedGroup remote MCP service; results should identify the tool and city or rule version used.]

## Skill Version(s):

1.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
