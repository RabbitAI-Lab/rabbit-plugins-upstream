## Description: <br>
Simplified D-InSAR deformation monitoring that generates interferograms, coherence rasters, and surface deformation from master/slave SLC imagery or offline synthetic inputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and remote-sensing practitioners can use this skill to run local D-InSAR deformation monitoring over a WGS84 bounding box or local SLC GeoTIFF input. It supports offline synthetic runs for validation and produces deformation, coherence, and run-parameter artifacts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release is marked suspicious because the local InSAR tool ships with under-disclosed credential, network geocoding, download, and cache modules. <br>
Mitigation: Review the package before installing, remove unused network and credential modules when deploying only the local InSAR workflow, and run the skill in an isolated environment. <br>
Risk: The package includes hardcoded Earthdata fallback credentials. <br>
Mitigation: The publisher should remove and rotate the embedded credentials; users should not rely on them and should avoid installing the package in environments containing sensitive credentials. <br>
Risk: The credential helpers can inspect environment secrets, .netrc, and ~/.geoskill/secrets.json. <br>
Mitigation: Do not run the skill in an environment with sensitive .netrc entries, ~/.geoskill/secrets.json, or credential environment variables unless the credential modules have been removed or audited. <br>


## Reference(s): <br>
- [Skill README](artifact/README.md) <br>
- [Skill Definition](artifact/SKILL.md) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-insar-deformation-monitoring) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with CLI commands; runtime outputs GeoTIFF and JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces deformation.tif, coherence.tif, insar_params.json, and, when manifest support is available, output-manifest.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata and script VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
