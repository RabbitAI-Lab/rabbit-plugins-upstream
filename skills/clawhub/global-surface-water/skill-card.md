## Description: <br>
Downloads JRC Global Surface Water raster layers such as occurrence, change, seasonality, recurrence, transition, and extent for a supplied bounding box or resolved place. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, analysts, and GIS practitioners use this skill to download public JRC Global Surface Water GeoTIFF layers for an area of interest and prepare them for local geospatial analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review flags bundled credential defaults that need attention before installation. <br>
Mitigation: Remove or neutralize bundled credential defaults and rely on user-provided environment variables, .netrc, or a local secrets file. <br>
Risk: Place-name lookup can send sensitive location queries to third-party geocoding services and keep local cache data. <br>
Mitigation: Use explicit --bbox for sensitive areas, use --no-nominatim when appropriate, and clear ~/.geoskill_core_cache when place queries should not persist. <br>
Risk: Dependencies are not pinned, which can make installs less reproducible. <br>
Mitigation: Pin dependency versions before production use and review updates during maintenance. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/global-surface-water) <br>
- [JRC Global Surface Water Explorer](https://global-surface-water.appspot.com/) <br>
- [Google Earth Engine dataset catalog: JRC/GSW1_4/GlobalSurfaceWater](https://developers.google.com/earth-engine/datasets/catalog/JRC_GSW1_4_GlobalSurfaceWater) <br>
- [Pekel et al. 2016 Nature article](https://doi.org/10.1038/nature20584) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, code, configuration, guidance] <br>
**Output Format:** [Markdown instructions with command-line examples and generated GeoTIFF or JSON QA files when the bundled script is run] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports layer selection, bounding boxes, place lookup, output paths, dataset version, and optional QA summary output.] <br>

## Skill Version(s): <br>
0.3.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
