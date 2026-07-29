## Description: <br>
Search, filter, compare, recommend, and explain Google Earth Engine public datasets using a bundled bilingual catalog. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and geospatial practitioners use this skill to find, compare, and explain Google Earth Engine datasets for a study area, time period, sensor, band, resolution, provider, or license requirement. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release was flagged as suspicious because it ships hardcoded Earthdata credentials and under-discloses credential behavior. <br>
Mitigation: Do not run credential helper workflows until the hardcoded default is removed; provide required credentials through scoped environment variables or user secrets. <br>
Risk: Place resolution, catalog update, and audit modes may send location or catalog metadata to external services and may modify local catalog or report files. <br>
Mitigation: Use the offline query path for lower-risk work; avoid place resolution for sensitive locations unless third-party geocoding is acceptable, and treat update and audit commands as explicit networked file-mutating operations. <br>
Risk: Catalog metadata can overstate coverage or license suitability if broad bounding boxes or unverified terms are treated as definitive. <br>
Mitigation: Use strict filters such as full coverage and temporal requirements, inspect original source URLs and terms, and verify footprints in Earth Engine for high-stakes decisions. <br>


## Reference(s): <br>
- [Query Guide](references/query-guide.md) <br>
- [Normalized Record Schema](references/schema.md) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/gee-dataset-intel-v1-final) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with optional JSON query output and shell command examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Offline query workflows read local catalog assets; update and audit modes can access networks and write catalog assets or reports.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
