## Description: <br>
Geoskill: NASA Dataset Download helps agents search NASA Earth observation datasets by dataset name, bounding box, and time window, then return granule listings, download URLs, JSON summaries, or downloaded data files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to find NASA Earth observation granules, inspect available products, collect download URLs, and download selected HDF, NetCDF, or GeoTIFF files for a geographic area and date range. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence reports that this downloader ships with and can silently use hardcoded Earthdata credentials. <br>
Mitigation: Install only after review; configure a personal Earthdata token through environment variables or a protected secret store, avoid the bundled fallback account, and do not copy sample passwords or tokens from the artifact. <br>
Risk: QA sidecars can preserve query details and credential-state metadata. <br>
Mitigation: Write QA outputs only to protected locations and review or redact them before sharing outside the deployment boundary. <br>


## Reference(s): <br>
- [ClawHub skill release](https://clawhub.ai/ruiduobao/skills/geoskill-nasa-dataset-download) <br>
- [earthaccess Python SDK](https://github.com/nsidc/earthaccess) <br>
- [NASA Earthdata token profile](https://urs.earthdata.nasa.gov/profile) <br>
- [NASA CMR Search](https://cmr.earthdata.nasa.gov/search/) <br>
- [NASA-Earth-Data catalog](https://github.com/opengeos/NASA-Earth-Data) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, JSON, files, guidance] <br>
**Output Format:** [Text or Markdown guidance with CLI commands, optional JSON output or QA sidecars, URL lists, and downloaded dataset files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access and NASA Earthdata credentials for live search, URL retrieval, and downloads; dry-run mode can preview download targets without writing data files.] <br>

## Skill Version(s): <br>
5.0.1 (source: server release evidence; artifact CLI reports 0.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
