## Description: <br>
Estimates multi-look complex coherence and interferometric phase from registered master/slave SLC images, identifying stable scatterers and decorrelated change areas and producing coherence/phase GeoTIFFs plus statistics JSON. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and remote-sensing engineers use this skill to run local D-InSAR coherence and interferometric phase analysis on registered master/slave SLC imagery or synthetic test data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package security summary reports that the stated local raster-processing workflow is bundled with unused credential discovery, hardcoded Earthdata credentials, network geocoding/download helpers, and a provenance mismatch. <br>
Mitigation: Review the package before installing it in environments with credentials or sensitive location data, and prefer a cleaned release that removes unused helpers and hardcoded credentials. <br>
Risk: The security guidance reports unpinned dependencies. <br>
Mitigation: Pin and review dependencies before deployment. <br>
Risk: Server-resolved provenance is unavailable for this version. <br>
Mitigation: Treat provenance as unavailable and verify the publisher and package contents before relying on the release. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-dinsar-coherence-analysis) <br>
- [README](artifact/README.md) <br>
- [SKILL](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, JSON, Guidance] <br>
**Output Format:** [GeoTIFF files, JSON statistics and manifest files, and concise CLI guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces coherence.tif, phase.tif, coherence_statistics.json, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
