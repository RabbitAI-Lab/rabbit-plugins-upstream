## Description: <br>
Search, browse, and download 52K+ NASA Earth science datasets using the opengeos/NASA-Earth-Data offline catalog plus live NASA CMR, LP DAAC Earthdata Cloud, and GES DISC endpoints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to search NASA Earth science dataset metadata, inspect dataset details, find granules for a time and bounding box, and download selected Earthdata granules with appropriate credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The CLI reads local credential sources for NASA Earthdata access. <br>
Mitigation: Use a dedicated NASA Earthdata token with the minimum access needed and review local credential files before running the skill. <br>
Risk: Direct URL downloads can retrieve data from an unintended host if the URL is not trusted. <br>
Mitigation: Use direct download URLs only from trusted NASA Earthdata hosts and prefer dataset-driven search parameters when possible. <br>
Risk: QA sidecar files may reveal credential source and availability metadata. <br>
Mitigation: Store QA sidecars in controlled locations and review them before sharing logs or artifacts. <br>
Risk: Example credentials in the artifact are not appropriate for reuse. <br>
Mitigation: Create and store your own Earthdata token instead of reusing sample username, password, or token values. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/nasa-dataset-catalog) <br>
- [opengeos/NASA-Earth-Data](https://github.com/opengeos/NASA-Earth-Data) <br>
- [NASA Earthdata token profile](https://urs.earthdata.nasa.gov/profile) <br>
- [CMR collection search endpoint](https://cmr.earthdata.nasa.gov/search/collections.json) <br>
- [CMR granule search endpoint](https://cmr.earthdata.nasa.gov/search/granules.json) <br>
- [LP DAAC Earthdata Cloud](https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/...) <br>
- [GES DISC data endpoint](https://data.gesdisc.earthdata.nasa.gov/data/...) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Files, Configuration guidance] <br>
**Output Format:** [CLI text or JSON responses, downloaded data files, and optional QA JSON sidecar files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use NASA Earthdata credentials and network access for live CMR lookup and authenticated granule downloads.] <br>

## Skill Version(s): <br>
3.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
