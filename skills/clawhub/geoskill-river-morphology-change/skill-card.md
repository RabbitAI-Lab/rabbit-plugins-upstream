## Description: <br>
Extracts shorelines, centerlines, and channel widths from multi-temporal water body masks, and quantifies shoreline migration, channel migration, change hotspots, and migration zones. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and environmental teams use this skill to analyze river channel change from multi-temporal water masks or downloaded imagery, identify erosion and deposition areas, and generate river morphology reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make outbound requests to Microsoft Planetary Computer, download imagery, and create a persistent cache. <br>
Mitigation: Use explicit local --input-masks when network access is not intended, and set controlled --output-dir and --cache-dir locations for runs that download data. <br>
Risk: A run without real input masks can produce demo analysis outputs. <br>
Mitigation: Treat no-input outputs as demonstration data, or require explicit local inputs or an explicit demo mode before relying on results. <br>
Risk: Water level changes, narrow channels near pixel resolution, and complex braided or anastomosing channels can reduce morphology accuracy. <br>
Mitigation: Use same-season imagery when possible and require geospatial expert review before using outputs for engineering or operational decisions. <br>


## Reference(s): <br>
- [River Morphology Parameters](artifact/references/river_morphology.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with CLI commands; runtime outputs include GeoJSON, CSV, and JSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces persistent output files and may use a local cache when downloading imagery.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
