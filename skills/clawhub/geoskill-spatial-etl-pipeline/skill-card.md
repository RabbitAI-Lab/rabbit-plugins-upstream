## Description: <br>
Config-driven spatial extract-transform-load pipeline with per-step logging and a quality report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to run configurable local spatial ETL jobs over synthetic or local vector data, apply composable transforms, and generate output datasets with step logs and quality reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Server security evidence reports undisclosed credential handling and a hardcoded Earthdata password in the package. <br>
Mitigation: Remove hardcoded credentials, rotate the exposed Earthdata password, and document all credential paths before using the skill in sensitive environments. <br>
Risk: Server security evidence reports optional network geocoding that conflicts with the skill's offline privacy claims. <br>
Mitigation: Use synthetic or local-file mode when offline operation is required, and disable or clearly document geocoding and download helpers before deployment. <br>
Risk: Server security guidance says dependencies are not pinned. <br>
Mitigation: Pin and review runtime dependencies before installation in controlled or production environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-spatial-etl-pipeline) <br>
- [README](README.md) <br>
- [Skill definition](SKILL.md) <br>
- [Changelog](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Files, JSON] <br>
**Output Format:** [Markdown guidance with CLI commands and JSON configuration examples; runtime artifacts include GeoJSON, GeoPackage, JSON reports, and run manifests.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally by default for synthetic and local-file ETL; optional bundled helpers include credential, geocoding, and download behavior that should be reviewed before sensitive use.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and script VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
