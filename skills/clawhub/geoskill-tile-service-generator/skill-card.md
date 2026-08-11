## Description:

Slices local or synthetic rasters into multi-zoom XYZ Web Mercator PNG tiles with tile metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT

## Use Case:

Developers and GIS engineers use this skill to generate static XYZ tile directories from local GeoTIFFs or synthetic rasters for web map clients such as Leaflet, OpenLayers, and MapLibre.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security evidence flags the release as suspicious because bundled geospatial core modules include credential, geocoding, download, cache, and vendored-code behavior beyond the stated offline tile workflow.

Mitigation: Review the package before installing; remove or split unused credential and network modules if only local tiling is needed.

Risk: Credential-related bundled components can access local secrets and hardcoded fallback credentials.

Mitigation: Run in an isolated environment, avoid supplying unnecessary secrets, and inspect credential-related code before use.

Risk: Bundled network and cache components may contact external geocoding or download services and write cache files in the home directory.

Mitigation: Restrict network access when offline operation is required and review filesystem permissions before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-tile-service-generator)
- [README.md](README.md)
- [SKILL.md](SKILL.md)

## Skill Output:

**Output Type(s):** [Files, JSON, Shell commands, Configuration instructions, Guidance]

**Output Format:** [PNG tile files, JSON manifests, and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes XYZ {z}/{x}/{y}.png tiles, tiles.json, and output-manifest.json to a local output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
