## Description: <br>
Download NASA Earth observation datasets by using the earthaccess library to authenticate with NASA Earthdata Login, search granules by dataset, time window, and bounding box, and download or list files with optional QA sidecars. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and geospatial analysts use this skill to search NASA Earth observation collections and bulk-download granules for a selected dataset, date range, and WGS84 bounding box. It also supports offline catalog lookup, URL export, dry-run previews, and JSON QA sidecars for download workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The server security verdict is suspicious because the release ships real-looking default Earthdata credentials and handles more secrets than the NASA download workflow needs. <br>
Mitigation: Use only user-owned Earthdata credentials, remove or rotate shipped defaults before deployment, and prefer environment variables, a private secrets file, or netrc over embedded fallback values. <br>
Risk: QA sidecars include credential source metadata, which can reveal where secrets are configured when written to shared locations. <br>
Mitigation: Write QA sidecars only to private paths, review them before sharing, and minimize or remove credential metadata in shared reports. <br>
Risk: Networked search, URL, login, and download commands authenticate to NASA Earthdata services and can download large datasets. <br>
Mitigation: Run dry-run or URL listing first, constrain bounding boxes and counts, and review output directories before bulk download. <br>


## Reference(s): <br>
- [earthaccess](https://github.com/nsidc/earthaccess) <br>
- [NASA Earth Data catalog source](https://github.com/opengeos/NASA-Earth-Data) <br>
- [NASA Earthdata token profile](https://urs.earthdata.nasa.gov/profile) <br>
- [NASA CMR Search](https://cmr.earthdata.nasa.gov/search/) <br>
- [LP DAAC Earthdata Cloud](https://data.lpdaac.earthdatacloud.nasa.gov/) <br>
- [GES DISC Data](https://data.gesdisc.earthdata.nasa.gov/data/) <br>
- [LAADS Archive](https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [CLI text output, optional JSON output files, QA JSON sidecars, and downloaded NASA data files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write downloaded HDF, NetCDF, GeoTIFF, or related granule files to a local output directory; networked commands require NASA Earthdata access.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence; artifact CLI reports 0.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
