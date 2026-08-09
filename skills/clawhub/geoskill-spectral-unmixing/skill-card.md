## Description: <br>
Performs linear spectral unmixing (LSMM) with constrained least squares to estimate endmember abundances and generate abundance maps and endmember spectra. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts can use this skill to run local spectral unmixing over multispectral GeoTIFF or synthetic data and inspect the resulting abundance maps, endmember spectra, and run manifest. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled credential, download, and geocoding utilities are broader than the documented local spectral-unmixing workflow. <br>
Mitigation: Review the bundled utility modules before installation and remove unused credential, download, or geocoding code when a local-only workflow is required. <br>
Risk: Credential discovery and fallback credential behavior could expose or reuse credentials unexpectedly. <br>
Mitigation: Rotate any exposed credentials, provide secrets only through trusted environment or user secret stores, and avoid committing credential defaults. <br>
Risk: Network-capable geocoding and download helpers may run outside a purely offline processing posture. <br>
Mitigation: Run in an isolated environment, prefer synthetic or local-input modes, and allow network access only after reviewing the requested endpoints. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-spectral-unmixing) <br>
- [README](README.md) <br>
- [CHANGELOG](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Analysis, Shell commands] <br>
**Output Format:** [GeoTIFF abundance maps, JSON endmember spectra, JSON run manifests, and console status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are written to a user-selected output directory and may include local geospatial artifacts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
