## Description:

Extracts phenological features from NDVI time series and uses a RandomForest classifier for crop or land-cover classification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT

## Use Case:

Developers, geospatial analysts, and agriculture teams can use this skill to classify NDVI time-series rasters or synthetic phenology scenes and inspect feature importance, class curves, and run manifests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawHub security review reports that the main classifier appears local, but the package includes credential and network helper code that does not fit the stated offline crop-classification purpose.

Mitigation: Review the package before installing, and avoid running it in an environment with sensitive ~/.netrc or ~/.geoskill/secrets.json credentials unless those helpers are removed or clearly gated.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-time-series-classification)
- [README](artifact/README.md)
- [SKILL.md](artifact/SKILL.md)
- [VENDORED geoskill-core manifest](artifact/_geoskill_core/VENDORED.txt)

## Skill Output:

**Output Type(s):** [Files, GeoTIFF raster, JSON, Shell commands]

**Output Format:** [GeoTIFF classification raster, JSON feature and curve summaries, JSON run manifest, and console status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes outputs to the selected output directory; synthetic mode runs offline by default.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
