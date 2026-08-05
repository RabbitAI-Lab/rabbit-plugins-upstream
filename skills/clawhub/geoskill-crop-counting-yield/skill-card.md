## Description: <br>
Counts plants via canopy peak detection plus watershed segmentation and estimates yield with an empirical model. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers can use this skill to run local crop canopy analysis, count plants from CHM or NDVI-like rasters, and estimate yield from empirical model parameters. It also supports synthetic offline scenes for testing the workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bundled package includes geospatial helper modules whose network, credential, and cache behavior is broader than the crop-counting entrypoint describes. <br>
Mitigation: Audit or remove the unrelated helper modules before deployment, and run the skill in an isolated environment with network access disabled when offline processing is required. <br>
Risk: Helper code may read local credential stores or fall back to embedded Earthdata credentials. <br>
Mitigation: Inspect credential handling before installation, avoid running with sensitive home-directory secrets mounted, and provide only explicit environment credentials needed for the approved workflow. <br>
Risk: Dependencies and geospatial I/O libraries can affect local files and generated raster outputs. <br>
Mitigation: Pin dependencies, scan the resolved environment, and review generated GeoTIFF and JSON outputs before using them for decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-crop-counting-yield) <br>
- [Publisher profile](https://clawhub.ai/user/ruiduobao) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples; the executable skill writes GeoTIFF and JSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Primary generated files include canopy.tif, plant_labels.tif, count_yield_stats.json, and output-manifest.json when the manifest helper is available.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and entrypoint VERSION; artifact CHANGELOG.md and openai.yaml list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
