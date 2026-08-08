## Description: <br>
Detects clouds and cloud shadows using spectral thresholds and solar azimuth projection, generating cloud masks and coverage statistics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and remote-sensing users can use this skill to run local cloud and cloud-shadow detection over a WGS84 bounding box or local multiband GeoTIFF and produce masks plus coverage statistics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package security summary reports under-disclosed network and credential-handling code, including a hardcoded Earthdata password. <br>
Mitigation: Review before installing, run in an isolated environment without sensitive ~/.netrc, ~/.geoskill/secrets.json, or unrelated API keys, and prefer a release that removes or clearly gates the credential, geocoding, and downloader modules. <br>
Risk: Threshold-based cloud and shadow detection can misclassify scenes when spectral values, dark surfaces, or solar-shadow geometry differ from the configured assumptions. <br>
Mitigation: Validate outputs against trusted imagery or local QA data before using the generated mask or coverage statistics for operational decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-cloud-shadow-detection) <br>
- [README](README.md) <br>
- [Vendored geoskill core manifest](_geoskill_core/VENDORED.txt) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, code, configuration, guidance] <br>
**Output Format:** [Python CLI usage guidance plus generated GeoTIFF and JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The CLI writes cloud_shadow_mask.tif, coverage_stats.json, and output-manifest.json to the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and script VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
