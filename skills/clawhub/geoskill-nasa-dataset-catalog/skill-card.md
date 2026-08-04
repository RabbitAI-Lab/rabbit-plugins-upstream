## Description: <br>
Search, browse, and download 52K+ NASA Earth science datasets using an offline catalog plus live CMR, LP DAAC Earthdata Cloud, and GES DISC endpoints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, data engineers, and Earth science practitioners use this skill to search NASA Earth science datasets, inspect dataset metadata, find granules for a space-time window, and download selected granules with NASA Earthdata credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Real-looking embedded Earthdata username and password defaults may be used accidentally or copied into local workflows. <br>
Mitigation: Remove or rotate embedded defaults before use, and provide a user-owned NASA Earthdata token through environment variables, .netrc, or a scoped ~/.geoskill/secrets.json file. <br>
Risk: QA sidecar files include credential-source metadata and may reveal how credentials are configured. <br>
Mitigation: Treat QA sidecars as operational metadata, avoid sharing them publicly, and review or redact credential-source fields before storing logs or reports. <br>
Risk: The credential helper recognizes more credential variables than the NASA catalog workflow needs. <br>
Mitigation: Install and run the skill in a minimal environment that exposes only the Earthdata credentials required for the selected command. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-nasa-dataset-catalog) <br>
- [opengeos NASA Earth Data catalog source](https://github.com/opengeos/NASA-Earth-Data) <br>
- [NASA CMR collection search endpoint](https://cmr.earthdata.nasa.gov/search/collections.json) <br>
- [NASA CMR granule search endpoint](https://cmr.earthdata.nasa.gov/search/granules.json) <br>
- [NASA Earthdata token profile](https://urs.earthdata.nasa.gov/profile) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, configuration, files, guidance] <br>
**Output Format:** [CLI text or JSON, downloaded granule files, URL-list JSON files, and optional QA JSON sidecars] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports offline catalog search, optional live network queries, bearer-token downloads, and --qa run summaries.] <br>

## Skill Version(s): <br>
5.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
