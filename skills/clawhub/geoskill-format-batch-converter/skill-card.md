## Description: <br>
Batch converts raster and vector geospatial files, including GeoTIFF, Shapefile, GeoPackage, and GeoJSON, through GDAL/OGR-based Python tooling with structured logging. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to batch convert local raster and vector GIS datasets, optionally generating a small synthetic dataset for offline testing. The workflow records conversion status, output byte counts, and run metadata for later review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The authoritative security summary says the advertised converter is local, but the package includes bundled modules for network geocoding, arbitrary URL downloads, credential handling, and hardcoded credentials. <br>
Mitigation: Review the package before installation, remove or clearly gate unused network and credential modules, and run in an environment with restricted network and credential access unless those capabilities are explicitly needed. <br>
Risk: The authoritative security guidance marks the release as suspicious because bundled behavior does not fully match the advertised local conversion purpose. <br>
Mitigation: Treat the release as requiring security review before deployment and verify that only the intended converter entrypoint and dependencies are exposed to agents. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-format-batch-converter) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [README](artifact/README.md) <br>
- [Sample output manifest](artifact/_test_cli_run/output-manifest.json) <br>


## Skill Output: <br>
**Output Type(s):** [files, JSON, shell commands, guidance] <br>
**Output Format:** [Converted geospatial files plus JSON conversion logs and run manifests] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs on local files or locally generated synthetic data; unsupported files and conversion errors are recorded in the log without stopping the full batch.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and runtime output manifest) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
