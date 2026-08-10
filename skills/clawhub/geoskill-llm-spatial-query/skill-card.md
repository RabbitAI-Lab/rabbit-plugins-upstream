## Description: <br>
Parses natural-language spatial and attribute queries and executes them with geopandas and shapely to produce GeoJSON results and an auditable JSON query plan. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and GIS or remote-sensing practitioners use this skill to run local vector spatial queries from natural-language commands, including synthetic tests and queries over GeoJSON or Shapefile inputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes network, downloader, and credential-handling modules beyond the advertised offline spatial-query workflow. <br>
Mitigation: Review before installing and remove or clearly gate geocoding, downloader, and credential modules when they are not required. <br>
Risk: The credential module includes hardcoded Earthdata fallback credentials. <br>
Mitigation: Remove and rotate exposed credentials before use; rely on environment variables, .netrc, or user secrets instead of packaged defaults. <br>
Risk: AOI geocoding code can use home-directory caching. <br>
Mitigation: Disable home-directory caching by default or document and control the cache path for deployments. <br>
Risk: Dependencies are not version-pinned. <br>
Mitigation: Pin dependencies and review transitive packages before deploying the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-llm-spatial-query) <br>
- [README](README.md) <br>
- [Skill instructions](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Text] <br>
**Output Format:** [GeoJSON FeatureCollection, JSON query plan, JSON run manifest, and concise console status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are written to a local output directory and may include WGS84 bounding-box metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and geoskill-llm-spatial-query.py) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
