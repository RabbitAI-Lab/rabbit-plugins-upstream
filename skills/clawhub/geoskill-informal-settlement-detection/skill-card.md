## Description: <br>
Detect informal settlements by fusing texture irregularity, building morphology and spectral mixing into a classification score. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External geospatial analysts, urban planning teams, and developers use this skill to score likely informal settlement areas from local multispectral rasters, optional building footprints, or synthetic test scenes. Outputs should support survey triage and human review rather than direct enforcement or decisions affecting communities. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled helper modules include network geocoding, download, local credential-store, and hardcoded Earthdata-default behavior. <br>
Mitigation: Review those helper modules before installation and remove or disable network and credential paths that are not needed for the intended workflow. <br>
Risk: Informal-settlement classifications can be incomplete, biased by local data quality, or misleading when used outside their analytical context. <br>
Mitigation: Use outputs only as a rough analytical signal, require domain-expert review, and avoid using the results as the sole basis for enforcement or decisions affecting communities. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-informal-settlement-detection) <br>
- [Publisher profile](https://clawhub.ai/user/ruiduobao) <br>
- [README](README.md) <br>
- [Skill definition](SKILL.md) <br>
- [License](LICENSE) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Code, Files, Analysis, JSON, Configuration guidance] <br>
**Output Format:** [CLI-generated GeoTIFF, JSON statistics, JSON manifest, and console status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The primary raster contains an informal score band and a classification mask; JSON sidecars report summary statistics and run metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and script VERSION; artifact openai.yaml and CHANGELOG list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
