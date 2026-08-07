## Description:

Generates groundwater level and depth-to-water rasters from discrete well observations using IDW or simplified kriging interpolation with leave-one-out cross-validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, GIS analysts, and hydrology practitioners use this skill to generate groundwater table and depth-to-water raster products from well observations or synthetic samples for contour mapping, depth zoning, and well network assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is flagged suspicious because it bundles remote-service, downloader, and credential helpers that are not explained by the visible mapping workflow.

Mitigation: Review the package before installing, remove or disable bundled helpers that are not needed for groundwater mapping, and deploy in a controlled environment.

Risk: Credential-related helper code and exposed Earthdata credentials create unnecessary secret-handling risk for a workflow documented as local-first.

Mitigation: Rotate any exposed credentials, avoid storing secrets in the skill directory, and provide credentials only through managed environment variables when required.

Risk: Real well observations and geospatial coordinates may be sensitive even when processing is local.

Mitigation: Keep input data local, restrict output sharing, and review generated rasters and reports for sensitive location information before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-water-table-mapping)
- [Artifact README](artifact/README.md)
- [Artifact SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Files, JSON, Shell commands, Guidance]

**Output Format:** [GeoTIFF rasters, JSON reports, and Markdown/CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces water_table.tif, depth_to_water.tif, interpolation_report.json, and output-manifest.json in the selected output directory.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
