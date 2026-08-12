## Description: <br>
Maps traffic noise levels using FHWA-style source estimates, geometric distance attenuation, building shielding, and ground absorption, producing a noise-level GeoTIFF and parameters JSON. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External developers, geospatial analysts, and environmental planning teams use this skill to estimate and map road traffic noise for environmental impact review, acoustic zoning, and noise-barrier siting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release security evidence reports shared geospatial helper code beyond the advertised offline mapper, including network, download, and credential-handling functionality. <br>
Mitigation: Review the package before deployment, remove or disable credential, geocoding, and download helpers that are not needed, and run the skill with network access restricted when offline behavior is required. <br>
Risk: Users could over-rely on the offline privacy claim for every file in the package. <br>
Mitigation: Treat the offline claim as applying to the main noise-mapping workflow only after local review, and verify which modules are imported or executed in the intended deployment path. <br>


## Reference(s): <br>
- [Skill README](artifact/README.md) <br>
- [Skill Definition](artifact/SKILL.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/geoskill-noise-pollution-mapping) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Shell commands, Configuration instructions] <br>
**Output Format:** [GeoTIFF, JSON, run manifest, and Markdown usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces noise_level.tif, noise_params.json, and output-manifest.json for a single mapping run.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata; artifact CHANGELOG lists 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
