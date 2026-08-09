## Description: <br>
Estimates surface soil moisture via thermal inertia and the SAR Dubois model, with drought grading. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and remote-sensing practitioners use this skill to estimate surface soil moisture and drought grades from local or synthetic raster inputs and generate geospatial outputs for analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes plaintext fallback Earthdata credentials in helper code. <br>
Mitigation: Remove and rotate the bundled credentials before deployment; use environment variables, .netrc, or an external secrets file for any required accounts. <br>
Risk: Helper modules include geocoding and download behavior beyond the locally focused soil-moisture CLI. <br>
Mitigation: Review whether these helpers are needed, document any network use, and constrain downloads to expected sources and sizes before operational use. <br>
Risk: Dependencies are not pinned, which can change runtime behavior across installations. <br>
Mitigation: Pin and review dependency versions in the deployment environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-soil-moisture-mapping) <br>
- [README](artifact/README.md) <br>
- [Skill definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Files, Shell commands] <br>
**Output Format:** [GeoTIFF raster files, JSON run manifest, and optional console text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes moisture, drought grade, and combined GeoTIFF outputs plus output-manifest.json to the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata and executable VERSION; artifact CHANGELOG/openai.yaml list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
