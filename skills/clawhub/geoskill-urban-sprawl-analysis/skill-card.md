## Description:

Quantifies urban sprawl morphology and change metrics from multi-epoch built-up area rasters, including compactness, fractal dimension, centroid movement, and expansion rate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT

## Use Case:

Developers, GIS analysts, and planning teams use this skill to run local urban expansion analysis over multi-date binary urban rasters or synthetic test data. It produces sprawl metrics, centroid trajectories, and vectorized urban footprints for mapping and downstream spatial review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package is advertised as an offline urban-sprawl analyzer but evidence.security reports bundled credential, web lookup, and generic download helpers outside that description.

Mitigation: Review the package before installation, test it in an isolated environment, and remove or clearly disclose helpers that are not needed for the urban-sprawl workflow.

Risk: evidence.security guidance reports an exposed Earthdata credential.

Mitigation: Rotate the exposed credential before use and verify no shipped files contain live secrets.

Risk: Dependencies are not pinned in requirements.txt.

Mitigation: Pin dependency versions and scan the resolved environment before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/geoskill-urban-sprawl-analysis)
- [Publisher Profile](https://clawhub.ai/user/ruiduobao)
- [Artifact README](artifact/README.md)
- [Artifact SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, files]

**Output Format:** [Console text plus JSON, GeoJSON, and manifest files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include sprawl_metrics.json, centroid_trajectory.json, urban_footprint.geojson, and output-manifest.json.]

## Skill Version(s):

1.0.0 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
