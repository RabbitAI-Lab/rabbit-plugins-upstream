## Description: <br>
Detects suspected pest and disease stress areas from red-edge anomaly, thermal, texture, and multi-temporal remote-sensing signals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and agricultural remote-sensing users can run this skill to identify suspected crop pest or disease stress from local or synthetic multispectral and thermal raster inputs. It produces probability and risk rasters plus a run manifest for downstream inspection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes helper code that can read credential stores, retain secrets, contact third-party geocoding services, and use embedded Earthdata credentials. <br>
Mitigation: Audit or remove the helper modules before installation, rotate any exposed credentials, and run the skill with network access restricted when only local or synthetic processing is needed. <br>
Risk: The stated offline purpose does not fully match the bundled credential and network helper behavior. <br>
Mitigation: Review the installed files against the intended offline workflow and pin dependencies before using the release in a shared or production environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-pest-disease-detection) <br>
- [README](README.md) <br>
- [Server-resolved publisher profile](https://clawhub.ai/user/ruiduobao) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Text] <br>
**Output Format:** [GeoTIFF raster files, JSON run manifest, and brief console summary text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes pest_probability.tif, pest_risk.tif, stress_signals.tif, and output-manifest.json to the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and entrypoint VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
