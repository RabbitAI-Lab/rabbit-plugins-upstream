## Description: <br>
Searches and downloads public Landsat 8/9 Collection 2 Level 2 imagery from STAC sources, with filters for date, area, cloud cover, WRS-2 path/row, platform, and bands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT No Attribution (MIT-0) <br>


## Use Case: <br>
Developers, GIS analysts, and remote-sensing practitioners use this skill to find and download Landsat scenes for geospatial analysis workflows without relying on manual EarthExplorer, cloud-console, or GEE workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive place names may be sent to Open-Meteo or Nominatim and cached under ~/.geoskill_core_cache when --place is used. <br>
Mitigation: Prefer explicit --bbox for sensitive areas, disable Nominatim where appropriate, and clear or avoid the cache in sensitive environments. <br>
Risk: The security scan recommends review before installation because optional place-name lookup is broader than the main public data download flow. <br>
Mitigation: Review the permissions and network destinations before deployment, especially for workflows involving sensitive project locations. <br>
Risk: Dependency or test execution can introduce operational risk: requests should remain patched and e2e_test.py may reset artifact-local test output. <br>
Mitigation: Use a constraints file or environment policy to pin a current patched requests version, and run e2e tests only in disposable or clearly scoped workspaces. <br>


## Reference(s): <br>
- [Microsoft Planetary Computer Landsat Collection 2 Level 2](https://planetarycomputer.microsoft.com/dataset/landsat-c2-l2) <br>
- [Microsoft Planetary Computer STAC API](https://planetarycomputer.microsoft.com/api/stac/v1/) <br>
- [Element84 Earth Search STAC API](https://earth-search.aws.element84.com/v1/) <br>
- [ClawHub landsat-download release page](https://clawhub.ai/ruiduobao/skills/landsat-download) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Files, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands; CLI text or JSON results; GeoTIFF, metadata, and optional QA JSON files when download options are used.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Downloads write to the selected output directory using .part temporary files before final replacement; progress output can be suppressed for CI.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
