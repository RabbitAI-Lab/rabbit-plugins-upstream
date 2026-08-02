## Description: <br>
Search and download WorldPop high-resolution population and demographic GeoTIFF datasets by country, year, and type without an API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and data engineers use this skill to discover, download, and optionally clip WorldPop population and demographic GeoTIFF datasets for spatial analysis workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Large WorldPop downloads may consume significant disk space. <br>
Mitigation: Choose an output directory with enough free space and prefer lower-resolution or clipped datasets when appropriate. <br>
Risk: The downloader writes files to user-selected paths and may overwrite existing outputs. <br>
Mitigation: Review output filenames before execution and use dedicated data directories for downloads and QA sidecars. <br>
Risk: The skill depends on network requests and Python packages such as requests and tqdm. <br>
Mitigation: Install in an isolated Python environment and prefer maintained dependency versions. <br>


## Reference(s): <br>
- [WorldPop](https://www.worldpop.org/) <br>
- [WorldPop REST API](https://www.worldpop.org/rest/data) <br>
- [Open-Meteo Geocoding API](https://geocoding-api.open-meteo.com/v1/search) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, Python command examples, and optional JSON output examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide users to create GeoTIFF downloads and optional QA JSON sidecars when running the packaged script.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
