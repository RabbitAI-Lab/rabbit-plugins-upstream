## Description: <br>
Professional property valuation for Taiwan real estate using market comparison and floor-area pricing, with adjustments for location, floor level, building age, parking, and property type. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tsaitepiao-alt](https://clawhub.ai/user/tsaitepiao-alt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, real estate professionals, and developers use this skill to estimate Taiwan residential property values, compare similar transactions, and generate valuation reports from structured property inputs. <br>

### Deployment Geography for Use: <br>
Taiwan <br>

## Known Risks and Mitigations: <br>
Risk: Valuation inputs and generated reports may contain sensitive addresses and property details. <br>
Mitigation: Keep input JSON files and generated reports in an appropriate local storage location and avoid sharing them outside the intended workflow. <br>
Risk: Optional analytics and feedback channels may record or share usage activity. <br>
Mitigation: Run the analytics command or use feedback channels only when that activity is acceptable for the user or organization. <br>
Risk: Automated valuation outputs can be misleading when comparable sales, special property conditions, or local market assumptions are incomplete. <br>
Mitigation: Review comparable transactions and adjustment factors before relying on the report, and use a professional appraiser for decisions requiring precise valuation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tsaitepiao-alt/skills/taiwan-property-valuation-v2) <br>
- [Valuation report template](assets/valuation-report.md) <br>
- [Price adjustment factors](references/adjustment-factors.md) <br>
- [Parking deduction method](references/parking-deduction.md) <br>
- [Regional multipliers](references/regional-multipliers.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, markdown] <br>
**Output Format:** [Markdown guidance with bash command examples and a generated Markdown valuation report.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3; the valuation script reads a local JSON input file and writes a local report file.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
