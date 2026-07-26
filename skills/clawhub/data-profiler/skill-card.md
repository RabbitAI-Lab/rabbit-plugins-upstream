## Description: <br>
Profile construction data to understand characteristics, distributions, quality metrics, and patterns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[datadrivenconstruction](https://clawhub.ai/user/datadrivenconstruction) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, data engineers, and construction analytics teams use this skill to inspect user-provided construction datasets before ETL, reporting, quality monitoring, schema validation, and anomaly review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated profiles and exports can expose sensitive construction dataset details such as project identifiers, costs, contacts, repeated values, and column names. <br>
Mitigation: Use only approved input files and store generated reports or exports in approved locations with appropriate access controls. <br>
Risk: The profiler reads user-provided datasets from local files and can create local reports. <br>
Mitigation: Validate file paths and inputs before processing, and review generated reports before sharing or using them for decisions. <br>


## Reference(s): <br>
- [DataDrivenConstruction homepage](https://datadrivenconstruction.io) <br>
- [ClawHub Data Profiler release page](https://clawhub.ai/datadrivenconstruction/skills/data-profiler) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown reports, structured tables, JSON exports, and Python usage examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports may include dataset column names, quality scores, duplicate counts, top values, inferred construction data types, and recommendations.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
