## Description:

基于 D8 流向汇流、洼地识别与不透水面径流系数的城市内涝风险评估

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and geospatial analysts use this skill to run urban waterlogging risk analysis from a local DEM or synthetic test area, producing raster risk/depth outputs, runoff paths, and run metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled support code includes under-disclosed credential handling and a hardcoded Earthdata fallback password.

Mitigation: Audit or remove the bundled credential module before deployment, and require credentials to come from managed environment variables or a controlled secrets store.

Risk: Bundled support code includes remote geocoding and downloader utilities even though the documented drainage workflow is mostly local.

Mitigation: Run the skill in a contained environment, disable unexpected network access unless explicitly needed, and document any allowed outbound endpoints.

Risk: Home-directory caching and credential discovery may persist or read user-specific state.

Mitigation: Use an isolated runtime home directory and review cache and secrets paths before production use.

Risk: Dependencies are listed without pinned versions.

Mitigation: Pin and review dependencies before production installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-urban-drainage-analysis)
- [README](README.md)
- [Skill instructions](SKILL.md)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands; generated runs produce GeoTIFF, GeoJSON, JSON summaries, and a JSON manifest.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI writes waterlogging_risk.tif, waterlogging_depth_mm.tif, runoff_paths.geojson, drainage_summary.json, and output-manifest.json.]

## Skill Version(s):

1.0.0 (source: server release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
