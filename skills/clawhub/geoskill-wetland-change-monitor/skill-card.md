## Description: <br>
Monitor wetland extent, inundation frequency, and land cover transitions to identify degradation, recovery, and human encroachment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and geospatial analysts use this skill to run wetland change monitoring over multi-year water rasters or downloaded geospatial water data, producing change patches, transition summaries, and machine-readable analysis outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automatic data download can contact remote geospatial data sources and store downloaded inputs and analysis products locally. <br>
Mitigation: Install and run the skill only where network access and file writes are acceptable, and use an explicit fresh --output-dir for each run. <br>
Risk: Dependency or geospatial processing changes can affect production behavior. <br>
Mitigation: Review and pin dependencies before production use. <br>
Risk: Wetland change outputs depend on input raster quality, selected years, thresholds, and minimum patch area. <br>
Mitigation: Review the generated report, transition matrix, and GeoJSON patches before using results for operational decisions. <br>


## Reference(s): <br>
- [ClawHub skill release](https://clawhub.ai/ruiduobao/skills/geoskill-wetland-change-monitor) <br>
- [Publisher profile](https://clawhub.ai/user/ruiduobao) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance with shell commands; runtime outputs include GeoTIFF, GeoJSON, CSV, JSON reports, and a JSON manifest.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can write multiple analysis files under the selected output directory and may include data-source metadata when automatic downloads are used.] <br>

## Skill Version(s): <br>
3.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
