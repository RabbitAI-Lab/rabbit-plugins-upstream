## Description: <br>
Download NASA Earth observation datasets by using the earthaccess library to authenticate with NASA Earthdata Login, search granules by dataset, bounding box, and temporal window, and retrieve files or URLs with optional QA sidecars. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and geospatial practitioners use this skill to locate, preview, and download NASA Earth observation granules such as MODIS, VIIRS, GPM, Sentinel, SMAP, and ASTER data for analysis workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The documentation shows realistic plaintext NASA Earthdata credentials and the skill can read credentials from environment variables, ~/.geoskill/secrets.json, or ~/.netrc. <br>
Mitigation: Use a bearer token or secure secret manager, avoid copying plaintext password examples, and rotate any real credential that matches the documented example. <br>
Risk: Optional QA sidecar files can disclose credential-state metadata and download context. <br>
Mitigation: Store QA sidecars only in controlled locations and avoid sharing them outside the intended workflow. <br>


## Reference(s): <br>
- [earthaccess](https://github.com/nsidc/earthaccess) <br>
- [NASA Earthdata Login Profile](https://urs.earthdata.nasa.gov/profile) <br>
- [NASA CMR Granule Search](https://cmr.earthdata.nasa.gov/search/) <br>
- [NASA-Earth-Data catalog](https://github.com/opengeos/NASA-Earth-Data) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Files, Guidance] <br>
**Output Format:** [CLI text output, JSON result data or QA sidecars, and downloaded HDF, NetCDF, GeoTIFF, or related NASA dataset files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports optional dry-run previews, URL-only output, bounded result counts, local output directories, and nonzero exit codes for no-match and error cases.] <br>

## Skill Version(s): <br>
3.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
