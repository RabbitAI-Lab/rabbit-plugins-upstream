## Description: <br>
Converts digital number raster data to TOA radiance or TOA reflectance using gain, offset, and ESUN calibration parameters. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and remote-sensing analysts use this skill to calibrate local or synthetic multispectral raster data into TOA radiance or reflectance outputs with accompanying run metadata. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review marks the release suspicious because packaged credential, geocoding, download, and persistent-cache helpers exceed the advertised local calibration purpose. <br>
Mitigation: Review the package before installation and prefer a minimal deployment that keeps only the calibration CLI and required raster-processing modules. <br>
Risk: Credential helpers can read environment variables, ~/.netrc, and ~/.geoskill/secrets.json, and the security guidance calls out hardcoded fallback credentials. <br>
Mitigation: Run only in an isolated environment, remove unused credential helpers and fallback credentials, and avoid running on systems with sensitive local credential files unless the package is trusted. <br>
Risk: Vendored geocoding and download helpers introduce network-capable behavior that is not part of the documented offline calibration workflow. <br>
Mitigation: Disable network access for normal calibration runs and permit outbound access only after reviewing the exact helper behavior needed for a specific workflow. <br>
Risk: Dependencies are unpinned in requirements.txt. <br>
Mitigation: Pin and review dependency versions before production or commercial deployment. <br>


## Reference(s): <br>
- [Skill README](README.md) <br>
- [Skill Definition](SKILL.md) <br>
- [Vendored Core Metadata](_geoskill_core/VENDORED.txt) <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/geoskill-radiometric-calibration) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Shell commands, Guidance] <br>
**Output Format:** [GeoTIFF raster files, JSON calibration parameters, JSON run manifest, and CLI console text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include calibrated TOA radiance or reflectance rasters and local run metadata; synthetic mode can run without network access.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata and artifact code VERSION; CHANGELOG lists 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
