## Description:

Export data to KML or CZML with time attributes and popup info for virtual globes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT

## Use Case:

Developers and GIS engineers use this skill to convert local spatiotemporal point or track data into virtual-globe formats for Google Earth and Cesium. It can also generate synthetic timestamped track data for local testing and demonstrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The advertised exporter is mostly local, but the package includes unrelated credential and network helper code that is not disclosed to users.

Mitigation: Review or remove the bundled credential and network helper modules before deployment; install only when the publisher is trusted.

Risk: Bundled credential helpers include hardcoded fallback credentials and automatic reads from common secret stores.

Mitigation: Audit credential handling, clear hardcoded defaults, and run the skill in a scoped environment with only the secrets required for the intended workflow.

Risk: Network-capable helper modules are present even though the exporter is documented as local and offline by default.

Mitigation: Block outbound network access for offline export workflows, or explicitly review and approve any network-enabled helper behavior before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-virtual-globe-export)
- [README](README.md)
- [Skill definition](SKILL.md)
- [Changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Files, JSON, Shell commands]

**Output Format:** [KML, CZML, JSON, GeoTIFF, and terminal guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes export.kml, export.czml, export.json, track_density.tif, and output-manifest.json.]

## Skill Version(s):

1.0.0 (source: server release metadata; code VERSION agrees)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
