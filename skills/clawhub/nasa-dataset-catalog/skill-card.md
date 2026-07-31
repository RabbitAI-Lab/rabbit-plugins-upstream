## Description: <br>
Search, browse, and download 52K+ NASA Earth science datasets with offline catalog search, live NASA CMR and DAAC endpoint lookup, token-based single-granule download, and QA sidecar support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and earth science data users use this skill to search NASA Earth science collections, inspect dataset metadata, locate granules for a time and bounding box, and download selected granules through NASA Earthdata-backed services. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Embedded real-looking Earthdata username and password may expose or normalize unsafe credential handling. <br>
Mitigation: Remove the embedded credentials, rotate any affected account secrets, and replace examples with placeholders that direct users to environment variables or a secure secret manager. <br>
Risk: A bearer token can be sent to an arbitrary download URL when users provide untrusted direct URLs. <br>
Mitigation: Restrict authenticated downloads to NASA and Earthdata hosts, and avoid using direct URL downloads from untrusted sources. <br>
Risk: QA sidecars may capture operational details that should not be shared broadly. <br>
Mitigation: Treat QA sidecars as potentially sensitive logs and review them before storage or distribution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/nasa-dataset-catalog) <br>
- [opengeos NASA Earth Data catalog](https://github.com/opengeos/NASA-Earth-Data) <br>
- [NASA Earthdata token profile](https://urs.earthdata.nasa.gov/profile) <br>
- [NASA CMR collection search API](https://cmr.earthdata.nasa.gov/search/collections.json) <br>
- [NASA CMR granule search API](https://cmr.earthdata.nasa.gov/search/granules.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with shell commands, text or JSON command output, downloaded data files, and optional QA JSON sidecars] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Live search and download operations require network access and NASA Earthdata credentials; full downloads may create large local data files.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
