## Description: <br>
Searches STAC catalogs for Sentinel-1 SAR GRD imagery by area, date, polarization, and orbit direction, and can download selected assets with progress and .part temporary-file writes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and geospatial analysts use this skill to find and download Sentinel-1 SAR imagery from public STAC endpoints for remote-sensing workflows such as flood, vegetation, soil, surface-change, vessel, and sea-ice analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled credential handling includes an unnecessary hardcoded Earthdata password and code paths that can read local credential files. <br>
Mitigation: Review or remove the credential module before installation, do not rely on bundled credentials, and provide any required credentials through user-controlled secure storage. <br>
Risk: --place lookups may send place names to third-party geocoding services and cache resolved locations locally. <br>
Mitigation: Use explicit --bbox values for sensitive locations, disable optional lookup paths where available, and review or clear the local geocoding cache. <br>
Risk: Download mode writes remote Sentinel-1 assets to a user-selected output directory. <br>
Mitigation: Run downloads in a controlled workspace, review output paths before execution, and inspect downloaded files before downstream processing. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/sentinel1-download) <br>
- [Microsoft Planetary Computer STAC API](https://planetarycomputer.microsoft.com/api/stac/v1/) <br>
- [Element84 Earth Search STAC API](https://earth-search.aws.element84.com/v1/) <br>
- [Artifact README](README.md) <br>
- [Artifact LICENSE](LICENSE) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, files, guidance] <br>
**Output Format:** [CLI text or JSON results, with optional downloaded Sentinel-1 asset files and progress output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search-only mode returns matching scenes; download mode writes selected assets to the configured output directory.] <br>

## Skill Version(s): <br>
0.3.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
