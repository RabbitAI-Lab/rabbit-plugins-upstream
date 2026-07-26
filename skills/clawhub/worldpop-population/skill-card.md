## Description: <br>
Search and download WorldPop population grid datasets as GeoTIFF files by country, year, dataset type, or place, with optional JSON output and clipping. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and planners use this skill to find WorldPop demographic datasets, download population GeoTIFFs, and optionally subset outputs by bounding box or place for spatial analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/ruiduobao/skills/worldpop-population) <br>
- [WorldPop](https://www.worldpop.org/) <br>
- [WorldPop REST API](https://www.worldpop.org/rest/data) <br>
- [Open-Meteo Geocoding API endpoint](https://geocoding-api.open-meteo.com/v1/search) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, files] <br>
**Output Format:** [CLI text or JSON, with downloaded GeoTIFF files and optional .qa.json sidecar files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Makes internet requests to WorldPop and optional geocoding services, can write large GeoTIFF files to user-selected paths, and should be run with reviewed output paths and pinned dependencies in stricter environments.] <br>

## Skill Version(s): <br>
0.3.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
