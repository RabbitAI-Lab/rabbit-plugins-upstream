## Description:

Delineate urban growth boundaries from historical expansion rate and direction plus terrain, cropland and ecological constraints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT

## Use Case:

Developers, GIS analysts, and planning teams use this skill to run local urban growth boundary analysis from two-epoch built-up area rasters, terrain, cropland, and ecological constraints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package security summary flags undisclosed credential-handling and network geocoding helpers that do not fit the documented offline UGB workflow.

Mitigation: Review the package before sensitive deployment and remove or clearly document unrelated credential and geocoding helpers.

Risk: The security guidance notes that bundled helpers can read local credential files, contact external geocoding services, and write a home-directory cache.

Mitigation: Run in a restricted environment when privacy matters, disable network access unless needed, and inspect cache behavior before use.

Risk: The security guidance recommends dependency review because the package dependencies are not pinned.

Mitigation: Pin and review dependencies before installing in controlled or production environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-urban-growth-boundary)
- [README](artifact/README.md)
- [Skill documentation](artifact/SKILL.md)
- [License](artifact/LICENSE)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance plus local CLI commands; runtime outputs include GeoTIFF and JSON files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces growth_suitability.tif, growth_stats.json, and output-manifest.json in the selected output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
