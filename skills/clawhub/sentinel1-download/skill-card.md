## Description: <br>
STAC-based Sentinel-1 SAR C-band downloader for searching by bounding box, dates, polarization, and orbit direction, with optional large-file downloads and visual progress. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT No Attribution (MIT-0) <br>


## Use Case: <br>
Developers, geospatial analysts, and remote-sensing workflows use this skill to search public Sentinel-1 GRD scenes and optionally download selected VV/VH assets from STAC providers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Place-name queries may reveal sensitive research areas through Open-Meteo or Nominatim geocoding when --place is used. <br>
Mitigation: Use --bbox instead of --place for privacy-sensitive work; if --place is necessary, review expected network egress and consider disabling Nominatim fallback. <br>
Risk: AOI query results may persist in a home-directory geoskill cache after use. <br>
Mitigation: Clear or isolate ~/.geoskill_core_cache after sensitive use. <br>
Risk: Dependency behavior can vary across controlled environments if dependencies are not pinned. <br>
Mitigation: Pin and review dependencies before installation in controlled or production environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/sentinel1-download) <br>
- [README](README.md) <br>
- [Skill instructions](SKILL.md) <br>
- [Microsoft Planetary Computer STAC API](https://planetarycomputer.microsoft.com/api/stac/v1/) <br>
- [Element84 Earth Search STAC API](https://earth-search.aws.element84.com/v1/) <br>
- [Landsat Downloader reference](https://clawhub.ai/skills/landsat-download) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, CSV, shell commands, files] <br>
**Output Format:** [Markdown guidance plus CLI text or JSON output, optional CSV or JSON metadata side files, QA summaries, and downloaded imagery files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search output can be text or JSON; --format can write CSV or JSON metadata; --qa can write a JSON QA summary; --download writes Sentinel-1 asset files using .part temporary files before final replacement.] <br>

## Skill Version(s): <br>
0.3.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
