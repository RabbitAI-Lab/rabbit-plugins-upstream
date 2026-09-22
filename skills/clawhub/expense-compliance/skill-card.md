## Description:

报销合规审核 Skill 识别发票、收据、行程单或客票，并按用户的版本化制度给出带证据的报销合规审核建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

财务、运营和报销审核人员使用本 Skill 识别报销票据、创建或更新报销制度、按规则审核报销申请、检查同账户历史重复票据，并导出带规则和证据的审核建议。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Receipt images, OCR text, claim details, and reimbursement rules are sent to the external expense-compliance service.

Mitigation: Use a dedicated product API key, review the provider's retention and deletion controls, and submit only data the user is authorized to process.

Risk: Audit outcomes may be mistaken for payment approval, tax verification, or fraud determinations.

Mitigation: Present outputs as audit suggestions only and route payment approval, tax verification, and fraud decisions to authorized human processes.

Risk: Low-confidence OCR fields or suspected duplicate findings could be overstated.

Mitigation: Require user confirmation against the source image for low-confidence fields and describe duplicate matches as suspected duplicates only.

Risk: The product API key could leak through command arguments, logs, reimbursement materials, or exported reports.

Mitigation: Store the key only in EXPENSE_COMPLIANCE_API_KEY and omit secrets from logs, reimbursement materials, and reports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/youteacher/skills/expense-compliance)
- [AI Skills platform](https://ai-skills.open-idea.net)
- [API 密钥配置](https://ai-skills.open-idea.net/skill-docs/expense-compliance/API-KEY.md)
- [HTTP 请求、幂等与轮询](https://ai-skills.open-idea.net/skill-docs/expense-compliance/HTTP-REQUESTS.md)
- [操作、规则与结果结构](https://ai-skills.open-idea.net/skill-docs/expense-compliance/OPERATIONS.md)
- [证据、安全与人工复核规则](https://ai-skills.open-idea.net/skill-docs/expense-compliance/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Text guidance with setup shell commands, private Markdown reports, and JSON audit exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires EXPENSE_COMPLIANCE_API_KEY and curl; receipt extraction uses asynchronous polling and stable idempotency keys.]

## Skill Version(s):

1.0.1 (source: server release metadata and packageVersion metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
