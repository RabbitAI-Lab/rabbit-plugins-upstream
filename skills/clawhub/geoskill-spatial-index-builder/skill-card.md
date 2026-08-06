## Description: <br>
Builds R-tree, Quadtree, and GeoHash spatial indexes, benchmarks query performance, and validates results against brute-force search. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial engineers use this skill to compare spatial indexing strategies on local vector data or synthetic point sets and generate benchmark reports for query latency, hit counts, and result consistency. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release security summary flags unrelated credential, geocoding, caching, and download helper modules bundled with an otherwise local spatial-index benchmark. <br>
Mitigation: Review or remove the bundled _geoskill_core helper modules before installing in environments with real credentials or sensitive geospatial queries. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-spatial-index-builder) <br>
- [Publisher profile](https://clawhub.ai/user/ruiduobao) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces spatial_index_report.json with per-index benchmark metrics and output-manifest.json with run metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
