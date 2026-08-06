## Description:

Maps tsunami inundation from DEM or synthetic terrain using bathtub hydrological connectivity, producing inundation extent, water depth, arrival time, evacuation zone, parameter, and manifest outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, GIS analysts, and disaster-risk teams use this skill to run local tsunami inundation scenarios from a DEM or synthetic coastal terrain and generate flood extent, depth, arrival-time, evacuation-zone, and run-manifest outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The main tsunami mapping workflow appears local, but security evidence reports undisclosed geocoding, persistent location caching, downloader, and plaintext fallback credential behavior outside the advertised workflow.

Mitigation: Review before installing, install only if the publisher is trusted, and remove or isolate unrelated vendored modules before deployment.

Risk: Security evidence reports a plaintext fallback password and recommends treating the package as suspicious.

Mitigation: Rotate the exposed credential if it is real, run the skill in an isolated environment, and pin dependencies for reproducible installs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-tsunami-inundation-mapping)
- [README](artifact/README.md)
- [Skill documentation](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Files, JSON, Shell commands, Configuration instructions]

**Output Format:** [GeoTIFF rasters, JSON files, and Markdown or shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces inundation.tif, water_depth.tif, arrival_time.tif, evacuation_zone.tif, tsunami_params.json, and output-manifest.json.]

## Skill Version(s):

1.0.0 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
