## Description: <br>
Compose multi-layer maps with cartographic decoration and high-resolution render to TIFF or PDF. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and cartographers use this skill to create print-ready shaded-relief basemaps from local DEM GeoTIFFs or synthetic test data. It supports optional RGB overlay compositing for publication maps, wall maps, and atlases. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled helper modules include credential, network, and home-directory cache behavior beyond the advertised offline map-printing path. <br>
Mitigation: Review the packaged code before deployment, run with local input or synthetic mode where possible, and remove or isolate unused credential, downloader, and geocoding helpers before treating the package as offline-only. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-map-print-composition) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Text] <br>
**Output Format:** [GeoTIFF, PDF, JSON metadata and manifest files, plus brief CLI status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Primary outputs are print_map.tif, print_map.pdf, print_meta.json, and output-manifest.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; CLI VERSION also reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
