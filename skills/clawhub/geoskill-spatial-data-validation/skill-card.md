## Description: <br>
Validates vector data for geometry validity, topology issues, attribute completeness, and CRS consistency, then emits a graded quality report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
GIS developers, data engineers, and geospatial QA reviewers use this skill to check local vector datasets before ingestion, delivery acceptance, or submission. It can also generate synthetic defective datasets for offline validation of the quality-check workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled helper modules include network, downloader, geocoding, credential-reading, and hardcoded-credential behavior that is broader than the advertised local validation command. <br>
Mitigation: Review the package before installation and remove or disable unrelated helper modules when only local vector validation is required. <br>
Risk: Credential-reading and location-cache behavior could expose local environment data if invoked outside the intended CLI path. <br>
Mitigation: Run the skill in an isolated environment with limited home-directory and credential-store access. <br>
Risk: Network-capable helpers could send place queries to third-party services or download arbitrary URLs if an agent invokes those code paths. <br>
Mitigation: Restrict network access by default and require explicit human approval before using geocoding, downloader, or URL-based helper behavior. <br>


## Reference(s): <br>
- [Skill README](README.md) <br>
- [Skill Definition](SKILL.md) <br>
- [License](LICENSE) <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/geoskill-spatial-data-validation) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, JSON, GeoJSON] <br>
**Output Format:** [CLI guidance plus JSON reports, GeoJSON invalid-geometry exports, and run manifests] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces validation_report.json, invalid_geometries.geojson, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
