## Description: <br>
Detects and classifies cropland changes from before/after NDVI rasters, identifying suspected construction, water, forest, and bare soil changes and generating compliance investigation materials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External geospatial analysts, compliance teams, and developers use this skill to compare before/after NDVI rasters or bounded satellite downloads for cropland conversion investigations and compliance reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Remote-download mode can use satellite preview imagery as if it were NDVI data, which can lead to mismatched compliance findings. <br>
Mitigation: Prefer validated local before/after NDVI GeoTIFF inputs. If bbox/date downloads are used, verify that NDVI is computed from proper red and near-infrared bands before relying on the report. <br>
Risk: Compliance outputs could influence real-world land-use or enforcement decisions. <br>
Mitigation: Require human geospatial review and supporting evidence before using generated reports as decision inputs. <br>
Risk: Network downloads, local cache state, and unpinned dependencies can reduce reproducibility. <br>
Mitigation: Pin dependencies, retain downloaded source assets and manifests, and rerun important analyses from fixed local rasters. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-cropland-change-compliance) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/ruiduobao) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, files, configuration] <br>
**Output Format:** [CLI status text plus generated HTML, JSON, GeoJSON, and manifest files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces report.html, compliance-report.json, suspected_changes.geojson, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
2.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
