## Description: <br>
Calculate construction costs using DDC CWICR resource-based methodology, with transparent labor, material, and equipment breakdowns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[datadrivenconstruction](https://clawhub.ai/user/datadrivenconstruction) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Construction estimators, project teams, and developers use this skill to calculate or compare work-item costs from quantities, CWICR codes, resource norms, unit prices, and regional factors. It presents auditable cost components for labor, materials, equipment, overhead, profit, and totals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cost estimates can be wrong if resource norms, regional factors, or user-supplied prices are stale or incomplete. <br>
Mitigation: Verify pricing assumptions, CWICR matches, quantities, regional factors, and totals before using outputs for bids or budgets. <br>
Risk: The skill may need filesystem access for local quantity takeoff or CWICR data files. <br>
Mitigation: Grant access only to local project files the agent needs to read. <br>
Risk: Python package installation or execution may be needed for code examples. <br>
Mitigation: Review package installs and run generated Python in a controlled project environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/datadrivenconstruction/skills/cwicr-cost-calculator) <br>
- [Publisher profile](https://clawhub.ai/user/datadrivenconstruction) <br>
- [Data Driven Construction homepage](https://datadrivenconstruction.io) <br>
- [OpenConstructionEstimate-DDC-CWICR](https://github.com/datadrivenconstruction/OpenConstructionEstimate-DDC-CWICR) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown with cost tables, summaries, and optional Python or shell code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs separate labor, material, equipment, overhead, profit, unit cost, and total cost values; default currency is USD unless the user requests another currency.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
