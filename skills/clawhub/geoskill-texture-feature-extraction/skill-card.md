## Description:

Extracts GLCM texture features such as contrast, homogeneity, and energy from raster imagery and outputs multi-direction averaged texture rasters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT

## Use Case:

Developers and geospatial analysts use this skill to compute texture features from local or synthetic raster data for remote-sensing analysis, land-cover feature engineering, and offline validation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled shared modules include network, download, cache, and credential-handling capabilities beyond the core texture extraction workflow.

Mitigation: Review the package before installation and prefer a release that removes unused network and credential modules if those capabilities are not needed.

Risk: External endpoint access may occur if geocoding or download helper code is invoked.

Mitigation: Run synthetic or local-input workflows for offline processing, and restrict network access unless external lookup or download behavior is explicitly required.

Risk: Credential helper code can read environment variables, user credential files, and local credential stores.

Mitigation: Install only from a trusted publisher, avoid exposing unnecessary secrets in the runtime environment, and inspect credential-related modules before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-texture-feature-extraction)
- [README](artifact/README.md)
- [Skill definition](artifact/SKILL.md)
- [Runtime metadata](artifact/openai.yaml)
- [Example output manifest](artifact/_test_tex_basic/output-manifest.json)
- [Example texture statistics](artifact/_test_tex_basic/texture_stats.json)

## Skill Output:

**Output Type(s):** [Files, JSON, Configuration, Shell commands, Guidance]

**Output Format:** [GeoTIFF raster files, JSON manifests and statistics, plus concise CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default output includes texture_features.tif, texture_stats.json, and output-manifest.json; synthetic mode can run offline.]

## Skill Version(s):

1.0.0 (source: server release metadata and script VERSION; artifact openai.yaml and CHANGELOG list 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
