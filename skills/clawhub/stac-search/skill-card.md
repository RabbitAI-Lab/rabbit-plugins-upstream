## Description: <br>
STAC Universal Search Tool for searching geospatial data across any STAC endpoint. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to search STAC catalogs, inspect collections and assets, and return remote-sensing results filtered by collection, bounding box, date range, cloud cover, place, or preset endpoint. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Geospatial searches can reveal sensitive areas of interest through bbox, place, collection, date, and filter values sent to STAC endpoints. <br>
Mitigation: Prefer explicit bounding boxes over sensitive place names, use trusted HTTPS endpoints, and avoid submitting sensitive search parameters when possible. <br>
Risk: Custom endpoints and broad dependency ranges can change the operational or supply-chain risk profile of a deployment. <br>
Mitigation: Limit use to trusted STAC endpoints and pin or tighten the requests dependency range during deployment review. <br>
Risk: User-directed output and QA sidecar paths can create local files containing query metadata. <br>
Mitigation: Write outputs only to intended paths and review generated JSON files before sharing them outside the deployment environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/stac-search) <br>
- [Microsoft Planetary Computer STAC API](https://planetarycomputer.microsoft.com/api/stac/v1/) <br>
- [Element84 Earth Search STAC API](https://earth-search.aws.element84.com/v1/) <br>
- [Google Earth Engine STAC catalog](https://earthengine-stac.storage.googleapis.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text tables, raw STAC JSON, GeoJSON FeatureCollections, asset listings, collection summaries, and optional JSON QA sidecar files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write user-directed JSON output or QA summary files when output paths are supplied.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
