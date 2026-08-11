## Description:

Simulates watershed runoff hydrographs and peak flows from land use, DEM, and design rainfall using the SCS-CN runoff method and a triangular unit hydrograph.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT

## Use Case:

Developers, hydrology analysts, and geospatial practitioners use this skill to run local small-watershed runoff simulations for urban drainage, flood estimation, and sponge-city assessment workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Server security evidence marks the release suspicious because bundled credential and network helper code is present beyond the advertised local runoff simulator.

Mitigation: Run the skill in an isolated environment, avoid exposing sensitive credential files or API keys, and ask the publisher to remove or clearly document unused helper code before broad deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-stream-flow-simulation)
- [README](artifact/README.md)
- [SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Files, JSON, GeoTIFF, Text]

**Output Format:** [GeoTIFF runoff raster, hydrograph JSON, output manifest JSON, and command-line status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally by default and writes outputs to the requested output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata and target metadata; artifact CHANGELOG.md and openai.yaml list 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
