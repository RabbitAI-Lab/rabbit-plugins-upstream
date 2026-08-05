## Description:

Simplify vector geometries with Douglas-Peucker or Visvalingam-Whyatt algorithms and report vertex reduction and area retention.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT

## Use Case:

Developers and GIS practitioners use this skill to simplify local vector datasets for cartographic generalization, data-size reduction, and lighter tile rendering. It can process local vector inputs or generate synthetic test geometries, then summarize geometry reduction and area-retention results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package includes unrelated credential, network lookup, download, and cache modules that are not disclosed in the skill instructions.

Mitigation: Review the package before installing and remove the unrelated _geoskill_core credential, AOI, downloader, and cache modules before routine use if they are not required.

Risk: Credential-related code and a hardcoded credential create unnecessary exposure when run in a normal user environment.

Mitigation: Run only in an isolated environment without real ~/.netrc or ~/.geoskill/secrets.json files until the credential issue is remediated.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-vector-simplification)
- [README.md](README.md)
- [SKILL.md](SKILL.md)
- [CHANGELOG.md](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files, JSON]

**Output Format:** [Markdown guidance with shell commands; runtime outputs include GeoJSON, JSON statistics, and a JSON manifest.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are written locally as simplified.geojson, simplification_stats.json, and output-manifest.json.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact script VERSION also reports 1.0.0; artifact CHANGELOG reports 0.1.0 on 2026-08-04)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
