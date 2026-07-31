## Description: <br>
Downloads and searches global land-cover datasets including ESA WorldCover, FROM-GLC, and GlobeLand30 by bounding box or resolved place. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, GIS analysts, and research teams use this skill to find and download land-cover raster tiles for a selected region and year. It supports search-only workflows and local downloads for downstream environmental, urban planning, and climate analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bundled credential helper includes embedded Earthdata credentials and broader local credential lookup behavior. <br>
Mitigation: Remove the embedded credentials, rotate any exposed account, and rely on user-provided environment variables, netrc, or documented secret storage before deployment. <br>
Risk: Place and bounding-box queries are sent to external geospatial services during search, download, or place resolution. <br>
Mitigation: Use explicit --bbox values for sensitive locations, disable Nominatim with --no-nominatim when appropriate, and review network destinations before use. <br>
Risk: Downloads write remote raster data and statistics files to the local filesystem. <br>
Mitigation: Run in a controlled output directory, review requested datasets and years, and scan downloaded files before downstream processing. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/landcover-download) <br>
- [README](README.md) <br>
- [Planetary Computer STAC API](https://planetarycomputer.microsoft.com/api/stac/v1) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, code, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text or JSON search results, with optional downloaded GeoTIFF files and CSV or GeoJSON category statistics.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Downloads are user-directed and written to a local output directory; search requests send bbox or place-derived region data to external services.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
