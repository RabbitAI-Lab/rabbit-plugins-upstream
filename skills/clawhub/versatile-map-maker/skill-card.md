## Description:

Creates editable SVG maps for choropleths, categorical region maps, point and label overlays, and custom or historical boundary overlays from public map data or user-provided geometry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stanestane](https://clawhub.ai/user/stanestane)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to create editable SVG maps that visualize regional data, overlay boundaries or features, and document source precision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may download public map data and install pip or npm dependencies.

Mitigation: Review commands before execution and allow network or package installation only in an approved environment.

Risk: User-provided geodata or tabular data may contain proprietary or sensitive information.

Mitigation: Use an appropriate scratch area, preserve originals, and avoid sharing sensitive source data in generated notes or public outputs.

Risk: Generated maps can mislead if coarse, generalized, unmatched, or schematic geometry is presented as precise.

Mitigation: Label source granularity and precision, report unmatched regions or missing data, and visually inspect previews before delivery.

## Reference(s):

- [Data Sources](references/data-sources.md)
- [Geometry Inputs](references/geometry-inputs.md)
- [Styling And Accessibility](references/styling.md)
- [Technique Notes](references/technique.md)
- [Natural Earth rivers and lake centerlines GeoJSON](https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_10m_rivers_lake_centerlines.geojson)
- [Natural Earth Europe rivers GeoJSON](https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_10m_rivers_europe.geojson)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands plus generated SVG, PNG preview, JSON, and source-data files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Final notes should name the map source, data source, geometry precision, and any unmatched regions or missing data.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
