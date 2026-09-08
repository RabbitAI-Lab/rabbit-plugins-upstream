## Description:

共同赢（GTYT）供应商账单与到货单的三阶段对账流程，用于按月核对「共同赢X月账单-上海-共同赢.xls」与「到货单明细表」在每店每产品上的「单价」「数量」「金额」是否一致，并输出金额差异对比与原账单标黄差异 Excel 文件。

This skill is ready for commercial/non-commercial use.

## Publisher:

[charlesoyoung](https://clawhub.ai/user/charlesoyoung)

### License/Terms of Use:

MIT-0

## Use Case:

Operations, procurement, and finance staff use this skill to reconcile monthly GTYT supplier bill spreadsheets against arrival-order spreadsheets, identify store-level and SKU-level discrepancies, and produce review-ready Excel outputs.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill handles sensitive business spreadsheets and may stage outputs for outbound Feishu delivery.

Mitigation: Use it only with files approved for local staging and Feishu transfer, and review generated workbooks before sending them.

Risk: The default output path can place generated workbooks and parsed JSON intermediates under /tmp.

Mitigation: Provide an explicit private output directory, run as an unprivileged user, and remove generated files after reconciliation is complete.

Risk: Hard-coded store mappings and known merged-store cases can affect reconciliation interpretation.

Mitigation: Review unmatched-store outputs and documented merged-store notes before using discrepancies for financial decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/charlesoyoung/skills/gtyt-reconcile)
- [Publisher profile](https://clawhub.ai/user/charlesoyoung)

## Skill Output:

**Output Type(s):** [files, json, text, shell commands]

**Output Format:** [Text guidance and shell commands that produce .xls reconciliation workbooks and a JSON run summary.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a difference report workbook, a copy of the original bill with highlighted discrepancy cells, and an optional parsed JSON intermediate file.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
