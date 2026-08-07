## Description:

Maps water yield, water retention, and nitrogen retention using a simplified InVEST-style Budyko water balance and NDVI-modulated retention coefficients.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT

## Use Case:

Developers, GIS analysts, and environmental teams use this skill to generate local raster estimates for watershed water-retention assessment, water-purification service accounting, and ecological conservation planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Server security evidence reports bundled helper modules with unrelated network, credential, and hardcoded-account behavior that does not fit the advertised offline mapping skill.

Mitigation: Review, remove, or isolate the bundled _geoskill_core helpers before execution, and run only in an environment without sensitive credentials until that code is clearly scoped.

Risk: The generated GeoTIFF and JSON outputs are model estimates from simplified Budyko and NDVI-based calculations.

Mitigation: Treat outputs as planning or screening evidence and validate assumptions, input rasters, and parameter choices before operational decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-water-purification-mapping)
- [Publisher profile](https://clawhub.ai/user/ruiduobao)
- [README](artifact/README.md)
- [License](artifact/LICENSE)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files]

**Output Format:** [Markdown guidance with shell commands; generated artifacts include GeoTIFF rasters and JSON manifests.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI writes water_yield.tif, water_retention.tif, nutrient_retention.tif, water_purification_params.json, and output-manifest.json.]

## Skill Version(s):

1.0.0 (source: server release metadata and target metadata; script VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
