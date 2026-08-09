## Description: <br>
Build spatial dashboards combining map layers and statistical charts into HTML. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and GIS practitioners use this skill to turn local GeoTIFF data or offline synthetic spatial data into a self-contained dashboard with maps, KPI cards, SVG charts, zonal statistics, and reproducible output files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes under-disclosed credential, download, caching, and network-capable helper behavior beyond the main dashboard command. <br>
Mitigation: Review before installing, remove or justify credential and downloader helpers, and avoid sensitive environments until the behavior is documented and approved. <br>
Risk: Generated dashboards load Leaflet assets and OpenStreetMap tiles in the browser when opened. <br>
Mitigation: Document browser-side network requests and use local Leaflet assets or offline tile sources where network isolation is required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-spatial-data-dashboard) <br>
- [Publisher profile](https://clawhub.ai/user/ruiduobao) <br>


## Skill Output: <br>
**Output Type(s):** [files, text, code, shell commands, configuration, guidance] <br>
**Output Format:** [HTML dashboard, JSON statistics, GeoTIFF raster, JSON run manifest, and console text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local processing with offline synthetic mode; generated dashboards load Leaflet assets and OpenStreetMap tiles in the browser unless adapted for offline tiles.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and entrypoint VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
