## Description: <br>
Compute carbon stock changes, emissions/removals, and uncertainty from multi-temporal land cover data using IPCC Tier 1/2 carbon factors. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and geospatial analysts use this skill to estimate land use change carbon budgets, deforestation or afforestation CO2e impacts, transition matrices, and uncertainty summaries from before/after land cover rasters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: BBox/date-only runs can produce synthetic results that may appear tied to the requested place and dates. <br>
Mitigation: Use explicit before and after land-cover rasters for real accounting, and label bbox/date-only output as synthetic or exploratory. <br>
Risk: The skill can make outbound Planetary Computer queries and cache downloaded data. <br>
Mitigation: Confirm that outbound data access and local caching are acceptable before using the download mode in restricted environments. <br>
Risk: Production or compliance use may depend on clearer provenance and dependency control than the release currently provides. <br>
Mitigation: Require documented data provenance, pinned dependencies, and reviewer approval before using outputs for compliance, MRV, or financial decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-land-use-carbon-accounting) <br>
- [Carbon factors registry](references/carbon_factors.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with shell commands; generated analysis artifacts include CSV, JSON, GeoTIFF, and manifest files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May download remote imagery metadata/data when bbox and date-range inputs are used; supports synthetic fallback output when explicit land-cover rasters are not provided.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
