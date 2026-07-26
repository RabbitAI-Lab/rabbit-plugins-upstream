## Description: <br>
Professional property valuation for Taiwan real estate using market comparison, floor area pricing, comparable transaction data, and adjustments for location, floor level, building age, parking, and property type. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tsaitepiao-alt](https://clawhub.ai/user/tsaitepiao-alt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, real estate professionals, and agents use this skill to estimate Taiwan residential property value, compare nearby transactions, adjust for property-specific factors, and prepare client-facing valuation reports. <br>

### Deployment Geography for Use: <br>
Taiwan <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks users to run a local usage-count analytics command after use. <br>
Mitigation: Users who do not want usage tracking should avoid running the analytics command; the valuation script itself operates locally on the provided input file. <br>
Risk: Property valuations are heuristic estimates and may be inaccurate when comparable transaction data or adjustment inputs are incomplete. <br>
Mitigation: Review recent comparable transactions, document manual adjustments, and consult a qualified real-estate appraiser when a precise valuation is required. <br>


## Reference(s): <br>
- [Adjustment Factors](references/adjustment-factors.md) <br>
- [Parking Deduction](references/parking-deduction.md) <br>
- [Regional Multipliers](references/regional-multipliers.md) <br>
- [Valuation Report Template](assets/valuation-report.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/tsaitepiao-alt/skills/taiwan-property-valuation-v1) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown valuation report with a console summary from a local Python script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-provided JSON input file with property attributes, comparable transactions, and adjustment percentages.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
