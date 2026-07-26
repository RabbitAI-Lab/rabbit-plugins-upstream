## Description: <br>
Estimates Taiwan real estate values using market comparison and floor area pricing with adjustments for location, floor level, building age, parking, and property type. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tsaitepiao-alt](https://clawhub.ai/user/tsaitepiao-alt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External real estate professionals, buyers, and sellers use this skill to estimate Taiwan residential property prices, compare nearby transactions, and prepare valuation reports. <br>

### Deployment Geography for Use: <br>
Taiwan <br>

## Known Risks and Mitigations: <br>
Risk: Valuation reports may make user-supplied comparable sales look like verified Taiwan transaction-registry evidence. <br>
Mitigation: Treat outputs as rough estimates and independently verify comparable sales from official sources before relying on the report. <br>
Risk: The optional analytics command records usage. <br>
Mitigation: Do not run the analytics command unless usage recording is acceptable. <br>


## Reference(s): <br>
- [Valuation Report Format](assets/valuation-report.md) <br>
- [Price Adjustment Factors](references/adjustment-factors.md) <br>
- [Parking Deduction Method](references/parking-deduction.md) <br>
- [Regional Multipliers](references/regional-multipliers.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, text, shell commands, guidance] <br>
**Output Format:** [Markdown valuation report with terminal status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and a JSON input file; writes a valuation report to the requested output path.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
