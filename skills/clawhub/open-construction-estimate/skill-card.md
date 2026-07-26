## Description: <br>
Access and utilize open construction pricing databases. Match BIM elements to standardized work items, calculate costs using public unit price databases with 55,000+ work items. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[datadrivenconstruction](https://clawhub.ai/user/datadrivenconstruction) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Construction estimators, BIM practitioners, and developers use this skill to match element descriptions or BIM element data to standardized construction work items and generate cost estimates with confidence scores and CSI division summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read local pricing or project files and may use network access for pricing API endpoints. <br>
Mitigation: Grant file and network access only in workspaces containing trusted construction data and approved pricing sources. <br>
Risk: Generated estimates can be wrong when pricing data, regional factors, quantities, or semantic matches are stale or low confidence. <br>
Mitigation: Review confidence scores, manually check low-confidence or missing matches, and validate estimates before professional use. <br>
Risk: Online or subscription pricing databases can have separate licensing or terms of use. <br>
Mitigation: Confirm database terms before using or redistributing pricing-derived outputs. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/datadrivenconstruction/skills/open-construction-estimate) <br>
- [CSI MasterFormat](https://www.csiresources.org/standards/masterformat) <br>
- [Data Driven Construction](https://datadrivenconstruction.io) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, files, guidance] <br>
**Output Format:** [Markdown responses with matched work item tables, cost calculations, summary data, and optional Excel export instructions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes confidence scores, regional adjustment factors when supplied, CSI division summaries, and flags for missing or low-confidence matches.] <br>

## Skill Version(s): <br>
2.0.0 (source: claw.json and server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
