## Description: <br>
Reconciles data sources using stable identifiers such as Pay Number and driver document numbers, producing exception report specifications and no-silent-failure checks for non-joins and mismatches. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kowl64](https://clawhub.ai/user/kowl64) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, analysts, and data operations teams use this skill to design deterministic reconciliation workflows for CSV/XLSX datasets and produce exception report specs with explicit reason codes for missing, duplicate, invalid, or mismatched records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Input datasets and generated exception reports may contain sensitive names, pay numbers, or driver document identifiers. <br>
Mitigation: Provide only the datasets needed, handle reports as sensitive, and review outputs before sharing or using them for operational decisions. <br>
Risk: Incorrect matching priorities or tolerance thresholds can produce misleading exceptions or failed reconciliation gates. <br>
Mitigation: Confirm key priority, field mappings, and thresholds before reconciliation, then review the exception report before making source-system changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kowl64/skills/data-reconciliation-exceptions) <br>
- [Matching rules](references/matching-rules.md) <br>
- [Exceptions report template](assets/exceptions-report-template.csv) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown with CSV schema and reason-code specifications] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include CSV exception report templates and variance gate definitions; source data remains read-only by default.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
