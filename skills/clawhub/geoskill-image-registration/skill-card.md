## Description: <br>
Estimates image translation with phase-correlation FFT to perform sub-pixel image registration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial engineers use this skill to align local or synthetic raster image pairs, estimate pixel shifts, and generate registered GeoTIFF outputs with JSON run metadata. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence flags the release as suspicious because the package includes geocoding, downloading, caching, and credential-reading helpers beyond the stated image-registration purpose. <br>
Mitigation: Review the package before deployment, trim or isolate unrelated helper modules, and keep those capabilities explicitly opt-in. <br>
Risk: Credential-related helper code may read environment variables, .netrc, or user-level secrets if invoked. <br>
Mitigation: Run in an isolated environment without valuable credentials or secret files unless those helpers are intentionally needed. <br>
Risk: Downloader and geocoding helper code may introduce network behavior that is not part of the local registration workflow. <br>
Mitigation: Disable network access for normal image-registration runs and use synthetic or local GeoTIFF inputs when validating the release. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-image-registration) <br>
- [Publisher profile](https://clawhub.ai/user/ruiduobao) <br>
- [Artifact README](artifact/README.md) <br>
- [Artifact SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, files] <br>
**Output Format:** [Console text plus GeoTIFF and JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces registered.tif, offset.json, and output-manifest.json when run successfully.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and entrypoint VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
