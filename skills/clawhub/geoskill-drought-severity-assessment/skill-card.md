## Description: <br>
Combined drought grading fusing SPI and VHI to produce drought-grade rasters, SPI rasters, and per-grade area statistics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Geospatial analysts, climate researchers, and agricultural monitoring teams use this skill to assess regional drought severity from precipitation and vegetation signals. It supports offline synthetic runs for validation and local GeoTIFF inputs for SPI-based assessment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Security evidence reports under-disclosed credential and network helper code, including hardcoded Earthdata credentials, that does not fit the published drought-assessment purpose. <br>
Mitigation: Review the package before installation and remove, document, or isolate unrelated credential brokers, hardcoded credentials, and geocoding or download helpers. <br>
Risk: Security guidance warns against installing the package in environments containing valuable .netrc files, geospatial service credentials, OpenAI keys, or other API keys. <br>
Mitigation: Run the skill in an isolated environment without sensitive credentials unless the extra helper modules have been removed or separately approved. <br>
Risk: Security guidance identifies unpinned dependencies as a review concern. <br>
Mitigation: Pin and review runtime dependencies before production deployment. <br>


## Reference(s): <br>
- [Skill README](artifact/README.md) <br>
- [Skill Definition](artifact/SKILL.md) <br>
- [License](artifact/LICENSE) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Configuration, Shell commands, Guidance] <br>
**Output Format:** [GeoTIFF rasters, JSON reports, run manifests, and Markdown usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces drought_grade.tif, spi.tif, drought_report.json, and output-manifest.json for a run.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
