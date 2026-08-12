## Description:

Estimate traffic flow and speed from multi-temporal vehicle detection, counting and cross-correlation displacement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT

## Use Case:

Developers and geospatial analysts use this skill to estimate traffic flow and vehicle speed from local or synthetic two-epoch imagery for traffic monitoring and road-network performance assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package includes helper code for geocoding, downloads, and credential management beyond the documented local traffic-estimation workflow.

Mitigation: Review the package before installation and prefer a release with unused helper modules removed when those capabilities are not needed.

Risk: Security evidence reports embedded Earthdata credential behavior.

Mitigation: Do not rely on embedded credentials; use managed secrets or environment variables and rotate any exposed credentials before deployment.

Risk: Place-name workflows may contact remote geocoding services.

Mitigation: Use explicit bounding boxes, local GeoTIFF inputs, or synthetic mode when remote geocoding is not acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-traffic-flow-estimation)
- [README](README.md)
- [SKILL.md](SKILL.md)

## Skill Output:

**Output Type(s):** [Files, JSON, Configuration]

**Output Format:** [GeoTIFF traffic-flow raster, JSON traffic statistics, and JSON run manifest]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes outputs to a local output directory; synthetic mode requires no network.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
