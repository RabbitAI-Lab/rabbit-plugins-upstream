## Description: <br>
Crawls satellite imagery metadata from Copernicus, USGS EarthExplorer, and Microsoft Planetary Computer by bounding box, date range, cloud cover, and platform, then outputs JSON or CSV summaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and remote sensing practitioners use this skill to search available satellite scenes before downloading imagery, compare metadata across public sources, and create auditable JSON or CSV result sets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Searches send bounding box, date range, platform, and source queries to public satellite metadata services. <br>
Mitigation: Use the skill only for AOIs and date ranges that are appropriate to disclose to those services, and choose the metadata source deliberately. <br>
Risk: Place-name resolution may disclose the place string to online geocoding services when that path is used. <br>
Mitigation: Prefer explicit --bbox values or offline presets for sensitive areas of interest. <br>
Risk: Result, cache, and QA sidecar files can contain AOI, date range, source, and scene metadata. <br>
Mitigation: Write --output, --qa, and --cache-dir paths to controlled locations and remove cached data when it is no longer needed. <br>
Risk: Network behavior depends on the installed Python requests package. <br>
Mitigation: Install and maintain a current patched requests version before running the crawler. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/rs-metadata-crawler) <br>
- [Publisher profile](https://clawhub.ai/user/ruiduobao) <br>
- [Copernicus Open Access Hub](https://scihub.copernicus.eu) <br>
- [USGS EarthExplorer](https://earthexplorer.usgs.gov) <br>
- [Microsoft Planetary Computer](https://planetarycomputer.microsoft.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash examples; runtime outputs JSON, CSV, and optional QA JSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Searches can write result files, cache files, and QA sidecar summaries containing bbox/date/source parameters and scene statistics.] <br>

## Skill Version(s): <br>
0.3.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
