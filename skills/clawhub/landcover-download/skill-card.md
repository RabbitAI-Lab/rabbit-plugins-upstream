## Description: <br>
Download global land cover data from multiple sources including ESA WorldCover (10m), FROM-GLC (30m), and GlobeLand30 (30m), with STAC search and regional bbox subsetting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, GIS analysts, and land-cover data users use this skill to search public land-cover catalogs, download matching regional tiles, and generate optional QA or category summary outputs for a selected bbox or resolved place. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional place lookup can contact external geocoding services and disclose the place query. <br>
Mitigation: Use --bbox instead of --place for sensitive locations, and skip optional geocoding where precise location privacy matters. <br>
Risk: Optional QA and category-stat outputs write files to user-selected paths. <br>
Mitigation: Review --qa, --format, and --format-output paths before running the skill. <br>
Risk: FROM-GLC and GlobeLand30 direct-download helpers are not a reliable production path in the current evidence, and some inactive helpers use plain HTTP. <br>
Mitigation: Prefer the ESA WorldCover STAC path for normal use and avoid relying on FROM-GLC or GlobeLand30 direct downloads until transport and implementation are clarified. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/landcover-download) <br>
- [README](artifact/README.md) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Planetary Computer STAC endpoint](https://planetarycomputer.microsoft.com/api/stac/v1) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands; the CLI emits text or JSON and can write GeoTIFF, CSV, GeoJSON, and QA JSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses public land-cover services; optional place lookup can contact geocoding services, while bbox-based use avoids sending a place query.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
