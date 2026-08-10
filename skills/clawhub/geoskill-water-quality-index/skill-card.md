## Description:

Retrieves chlorophyll-a, total suspended solids, Secchi depth, water masks, and eutrophication classes from local or synthetic multispectral imagery using empirical water-color remote-sensing models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT

## Use Case:

Developers, geospatial analysts, and environmental monitoring teams can use this skill to produce water-quality rasters and summary reports for lake or coastal algae monitoring, eutrophication assessment, and water transparency mapping.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports bundled credential, geocoding, and download helpers, including hardcoded Earthdata credentials.

Mitigation: Review the package before installation, remove or clearly document unused vendored helpers, and rotate the hardcoded Earthdata credential if it is real.

Risk: The security guidance warns that user credential stores such as ~/.netrc, ~/.geoskill/secrets.json, and unrelated API keys could be exposed to this skill.

Mitigation: Run the skill in an isolated environment with only the minimum required environment variables and home-directory files mounted.

Risk: The main command is intended for local water-quality processing, but bundled helper modules can perform geocoding or network downloads.

Mitigation: Prefer synthetic or local-input mode for offline operation, and audit or disable network-capable helpers before broader deployment.

Risk: Empirical remote-sensing estimates can be inaccurate for water bodies or sensors outside the assumptions of the implemented models.

Mitigation: Validate outputs against local observations or trusted reference data before using them for operational environmental decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-water-quality-index)
- [README](README.md)
- [Skill instructions](SKILL.md)
- [Vendored geoskill core manifest](_geoskill_core/VENDORED.txt)

## Skill Output:

**Output Type(s):** [Files, JSON, Analysis, Shell commands]

**Output Format:** [GeoTIFF rasters plus JSON reports, output manifests, and concise CLI status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include chl_a.tif, tss.tif, secchi.tif, trophic_class.tif, water_quality_report.json, and output-manifest.json.]

## Skill Version(s):

1.0.0 (source: server release evidence and script VERSION; openai.yaml and CHANGELOG list 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
