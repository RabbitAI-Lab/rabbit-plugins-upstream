## Description: <br>
Searches geospatial datasets across preset or custom SpatioTemporal Asset Catalog (STAC) endpoints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to query STAC catalogs for satellite imagery and related assets by collection, bounding box, date range, and cloud cover. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Server security evidence flags under-disclosed credential-management code, including a hardcoded Earthdata password and home-directory secret reads. <br>
Mitigation: Audit or remove the bundled credential helper before installation, rotate any exposed credentials, and confirm the skill cannot read local secrets unexpectedly. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Plain text tables or JSON, often accompanied by shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May query remote STAC APIs and list assets or collection metadata.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
