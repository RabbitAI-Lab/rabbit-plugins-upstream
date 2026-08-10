## Description: <br>
Transforms coordinate reference systems with pyproj EPSG codes and built-in WGS84, GCJ02, and BD09 conversions for point sets and vector features. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and GIS or remote-sensing practitioners use this skill to reproject local vector data or batch point sets between EPSG coordinate reference systems and WGS84, GCJ02, or BD09 coordinate systems for map alignment, GPS track correction, and cross-CRS registration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package is marked suspicious because it bundles network, download, and credential-handling code outside the normal local CRS converter path. <br>
Mitigation: Review before installing and remove, isolate, or clearly document those modules before use with private location queries or stored API credentials. <br>
Risk: Evidence reports a plaintext fallback Earthdata password in bundled credential-handling code. <br>
Mitigation: Delete the fallback secret, rotate any affected credential, and require credentials through documented environment variables or a secret manager. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-crs-transformation) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Code, Shell commands] <br>
**Output Format:** [GeoJSON files, JSON reports and manifests, and CLI status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes transformed.geojson, transformation_report.json, and output-manifest.json under the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and test output manifests; artifact openai.yaml and CHANGELOG.md list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
