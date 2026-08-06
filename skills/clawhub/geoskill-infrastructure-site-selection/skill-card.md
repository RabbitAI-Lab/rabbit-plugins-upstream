## Description: <br>
Geoskill: Infrastructure Site Selection performs multi-criteria suitability analysis for infrastructure site selection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and infrastructure planners use this skill to analyze raster and optional downloaded geospatial data, compare infrastructure suitability criteria, and generate assessment outputs for site-selection decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Outbound geospatial data requests and local caching may expose area-of-interest coordinates or retain local copies of downloaded data. <br>
Mitigation: Review data-handling policy before use, provide local raster inputs when network access is not approved, and set explicit cache and output directories. <br>
Risk: Unpinned dependencies can change geospatial processing behavior across environments. <br>
Mitigation: Pin dependencies for production or controlled use and review generated suitability reports before relying on them for decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-infrastructure-site-selection) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with CLI examples; generated artifacts include JSON, HTML, and manifest files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes outputs to a configurable output directory and may use a local cache when downloading geospatial data.] <br>

## Skill Version(s): <br>
2.0.0 (source: evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
