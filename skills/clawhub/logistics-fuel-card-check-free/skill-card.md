## Description:

油卡充值与油耗明细表逐项核对（卡余额勾稽、公里油耗复算、加油量与油卡扣款一致性、合计行复核、重复加油、里程回退与空缺），每条结论引用原文行号与车牌号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Fleet vehicle administrators and finance teams use this skill during monthly fuel-card recharge and fuel-consumption reconciliation to check table arithmetic, duplicate refuelling entries, mileage consistency, and missing key fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fleet fuel-card and fuel-consumption tables can contain sensitive operational and financial data.

Mitigation: Run the checker locally where possible, provide only the table needed for reconciliation, and review outputs before sharing them beyond authorized operations or finance staff.

Risk: Runner messages mention anonymous usage statistics and a --no-stats option, but the inspected evidence says network transmission is not implemented and the option is not implemented.

Mitigation: Verify the packaged runner behavior and user-facing wording before deployment; do not promise telemetry or opt-out behavior unless it is implemented in the released artifact.

Risk: The free version intentionally omits cross-fleet summaries, ranked abnormal-consumption handling, and fuel-consumption root-cause attribution.

Mitigation: Treat the output as table-level arithmetic and consistency checking only, and use separate review processes for omitted operational, tax, GPS, fuel-station, or policy judgments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/logistics-fuel-card-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable text or structured JSON with reconciliation findings, source line numbers, vehicle plates, severity levels, summaries, and missing-input guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs deterministic local checks over a single fleet fuel-card table; reports insufficient input without drawing a conclusion.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
