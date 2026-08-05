## Description: <br>
Evaluate band math expressions like NDVI on rasters with a safe expression parser. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and GIS or remote-sensing analysts use this skill to run local raster band math and vegetation or water index calculations on GeoTIFF inputs or synthetic rasters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Under-disclosed network, download, cache, and credential-handling code is present alongside the local raster calculator. <br>
Mitigation: Review or isolate the vendored geoskill core modules before deployment; allow only the calculator path and network behavior that is explicitly needed. <br>
Risk: Credential helpers can access configured API keys or fallback credential stores. <br>
Mitigation: Run with least-privilege environment variables, avoid shared credential stores, and remove credential helper modules if they are not required. <br>
Risk: External geocoding and download helpers may contact network services and cache lookups in the home directory. <br>
Mitigation: Use synthetic or local inputs for offline workflows, or disable and isolate helper modules that perform network or cache writes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-map-algebra-calculator) <br>
- [README](README.md) <br>
- [Skill definition](SKILL.md) <br>
- [Changelog](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [files, json, shell commands, guidance] <br>
**Output Format:** [GeoTIFF files, JSON metadata, run manifests, and text guidance with shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Typical runs write result.tif, expression_meta.json, and output-manifest.json to the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
