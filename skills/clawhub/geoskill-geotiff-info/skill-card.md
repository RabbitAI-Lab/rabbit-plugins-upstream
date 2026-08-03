## Description: <br>
Reads GeoTIFF metadata, including CRS, resolution, image size, bands, NoData values, corner coordinates, and batch scan results, using Python standard-library parsing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, geospatial analysts, and data engineers use this skill to inspect GeoTIFF files or directories quickly without installing GIS tools or third-party Python packages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Batch mode reads metadata from matching GeoTIFF files under the selected local directory. <br>
Mitigation: Run it only against the file or directory intended for inspection, and review JSON exports before sharing them outside the intended workflow. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/geoskill-geotiff-info) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples; the tool itself emits text tables or JSON metadata.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Metadata-only inspection; batch mode scans matching GeoTIFF files under the selected local directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
