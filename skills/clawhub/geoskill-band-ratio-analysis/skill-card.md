## Description: <br>
Batch computation of NDVI, NDWI, MNDWI, NDBI, EVI, and SAVI spectral indices with per-index GeoTIFF outputs and value-range statistics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and remote-sensing practitioners use this skill to calculate common spectral indices from local multispectral GeoTIFF inputs or synthetic offline scenes, then inspect per-index raster products and summary statistics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes credential, geocoding, download, and home-directory cache code beyond the advertised local raster-analysis workflow. <br>
Mitigation: Review the package before installation, install only from a trusted publisher, and prefer a narrowed package that removes unused credential, geocoding, and download modules. <br>
Risk: Network-capable helper code may contact geocoding services or download files if invoked by future workflows or modifications. <br>
Mitigation: Use synthetic or local-input workflows when network access is not required, restrict network permissions in the execution environment, and review commands before running them. <br>
Risk: Bundled dependency declarations are broad and may resolve to different package versions over time. <br>
Mitigation: Pin and review dependencies in a controlled environment before deploying the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-band-ratio-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands; generated agent workflows may produce GeoTIFF rasters and JSON manifests when executed.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill execution writes one single-band GeoTIFF per requested index plus index_stats.json and output-manifest.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence, target metadata, and script VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
