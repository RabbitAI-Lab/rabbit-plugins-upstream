## Description: <br>
Blends overlapping geospatial image tiles with average or feathering methods to produce a seamless mosaic. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and GIS or remote-sensing practitioners use this skill to mosaic overlapping GeoTIFF tiles or synthetic test tiles into a local geospatial raster output with a run manifest. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Server security evidence reports undisclosed bundled helper modules that can contact geocoding services, persist location lookups, and access local or API credentials. <br>
Mitigation: Review or remove helper modules unrelated to mosaicking before installation, and run in an isolated environment when only local raster mosaicking is needed. <br>
Risk: Server security evidence reports a hardcoded Earthdata password in bundled code. <br>
Mitigation: Rotate and remove the credential before use; rely on environment variables, netrc, or user-managed secrets outside the skill package. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-image-mosaicking) <br>
- [Artifact README](artifact/README.md) <br>
- [Artifact changelog](artifact/CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with command examples; generated GeoTIFF raster and JSON manifest when executed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The CLI writes a mosaic GeoTIFF and output-manifest.json; synthetic mode runs locally, while real-data mode consumes local GeoTIFF tile directories.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
