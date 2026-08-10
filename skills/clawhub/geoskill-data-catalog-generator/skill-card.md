## Description: <br>
Scan raster and vector files in a directory, extract and classify metadata, and generate a browsable HTML / CSV data catalog. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and data stewards use this skill to inventory local geospatial raster and vector data, extract useful metadata, and publish catalog outputs for project review or data sharing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review reports that the package includes under-disclosed network, downloader, and credential-handling code, including hardcoded Earthdata credentials. <br>
Mitigation: Review the package before installing, run the catalog generator in a network-restricted environment when possible, remove or review bundled credential, geocoding, and downloader modules if they are not needed, and rotate or revoke the exposed Earthdata credentials. <br>
Risk: Generated HTML, CSV, JSON, and manifest files may disclose metadata about sensitive local geospatial data. <br>
Mitigation: Review generated catalog files before sharing them and run the skill only against directories whose metadata may be disclosed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-data-catalog-generator) <br>
- [Semantic Versioning](https://semver.org/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance and Python CLI output files including HTML, CSV, JSON, and an output manifest.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs on local files by default and can generate synthetic sample geospatial data for offline testing.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and script VERSION; artifact changelog/openai.yaml list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
