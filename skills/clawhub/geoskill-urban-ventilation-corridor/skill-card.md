## Description:

Derive aerodynamic roughness and ventilation potential from building morphology and extract least-resistance ventilation corridors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT

## Use Case:

Developers, urban analytics teams, and GIS practitioners use this skill to compute roughness and ventilation-potential rasters from building morphology and extract a least-resistance corridor for urban ventilation planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security review marks the package suspicious because it includes under-disclosed network, downloader, credential, and provenance-mismatched modules outside the advertised local ventilation workflow.

Mitigation: Review the package before installation, run it in a constrained environment, and prefer a cleaned release that removes unused credential and download helpers.

Risk: The package may access user credential and cache locations such as ~/.netrc, ~/.geoskill/secrets.json, and home-directory cache files.

Mitigation: Install and run only where access to those local files is acceptable, or isolate the process from sensitive home-directory state.

Risk: The artifact advertises offline processing, while the authoritative security guidance notes under-documented network geocoding behavior.

Mitigation: Document any network geocoding behavior before deployment and disable or remove unrelated network-capable modules when they are not required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-urban-ventilation-corridor)
- [Publisher profile](https://clawhub.ai/user/ruiduobao)

## Skill Output:

**Output Type(s):** [Files, Configuration, Shell commands, Guidance]

**Output Format:** [GeoTIFF, GeoJSON, JSON, and Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces ventilation.tif, corridor.geojson, ventilation_stats.json, and output-manifest.json in the selected output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata and script constant; artifact changelog lists 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
