## Description: <br>
Convert between vector GIS formats using the Python standard library, including Shapefile, GeoJSON, KML, GPX, GeoPackage, and CSV. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and GIS practitioners use this skill to inspect and convert local vector GIS files between common formats, optionally applying CRS conversion, precision control, field filtering, or bounding-box clipping. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release was flagged suspicious because it ships unrelated credential and network utilities alongside the local GIS converter. <br>
Mitigation: Audit or remove the credential and network helper modules before installing it in sensitive environments, and run the converter in an isolated workspace when possible. <br>
Risk: Credential helpers may access local secret stores such as ~/.netrc or ~/.geoskill/secrets.json. <br>
Mitigation: Avoid running it in environments with sensitive local credential files, use a disposable home directory or container, and rotate any exposed account if a credential is real. <br>
Risk: Conversion commands can overwrite output files. <br>
Mitigation: Use explicit output paths, keep backups of source data, and review generated files before relying on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/vector-convert) <br>
- [README](artifact/README.md) <br>
- [Skill definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [files, text, shell commands] <br>
**Output Format:** [Converted vector GIS files plus CLI status or file-info text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python 3.8+ and local filesystem access; output paths should be chosen carefully because conversions can overwrite files.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
