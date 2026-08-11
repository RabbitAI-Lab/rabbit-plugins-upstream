## Description: <br>
Extracts river networks from a DEM, generates multi-level riparian buffer zones, summarizes LULC composition within the buffers, and assesses buffer integrity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to run local riparian-buffer analysis from a DEM or synthetic raster input, producing river-network, buffer, land-cover composition, and integrity outputs for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The server security summary says the skill can generate misleading results from synthetic land-cover data and should not be used for real environmental decisions unless real LULC input handling is fixed. <br>
Mitigation: Use it only in a contained environment, validate real-input handling against trusted geospatial workflows, and require expert review before relying on outputs for environmental decisions. <br>
Risk: The server security guidance flags bundled credential and network modules with hardcoded credentials. <br>
Mitigation: Remove or audit the bundled credential and network helpers, rotate any exposed credentials, and run the skill with network access disabled unless those modules are required and reviewed. <br>
Risk: The server security guidance recommends pinning dependencies before production use. <br>
Mitigation: Pin and review dependencies in the execution environment before production deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-riparian-buffer-analysis) <br>
- [README](artifact/README.md) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Changelog](artifact/CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Analysis, Shell commands] <br>
**Output Format:** [GeoJSON, JSON, GeoTIFF, and console text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes river-network, buffer, LULC statistics, integrity assessment, and run-manifest files to the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact changelog and openai.yaml list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
