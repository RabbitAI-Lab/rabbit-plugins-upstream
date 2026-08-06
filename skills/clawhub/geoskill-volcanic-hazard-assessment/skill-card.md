## Description:

Assesses volcanic activity levels by fusing thermal infrared anomalies, InSAR deformation, SO2 column concentration, and eruption recency into GeoTIFF activity scores and five-level classifications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and geospatial workflows can use this skill to run local volcanic activity assessment from a multi-band GeoTIFF or synthetic scenario data. The outputs support review of activity score rasters, classified hazard levels, and run metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package bundles credential, geocoding, and download helpers that are not part of the documented volcanic hazard workflow.

Mitigation: Review the package before installation and remove or clearly disclose unrelated helpers before deployment.

Risk: The security evidence reports a hardcoded Earthdata password in the bundled helpers.

Mitigation: Remove the hardcoded credential and rotate the affected password before use.

Risk: Dependencies are not pinned in requirements.txt.

Mitigation: Pin and review dependencies in a controlled environment before production use.

Risk: Volcanic activity outputs can be mistaken for operational hazard decisions.

Mitigation: Require domain expert review and documented input data provenance before using outputs in safety-relevant decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-volcanic-hazard-assessment)
- [Publisher profile](https://clawhub.ai/user/ruiduobao)
- [Artifact README](artifact/README.md)
- [Artifact skill instructions](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [files, json, shell commands, guidance]

**Output Format:** [GeoTIFF rasters, JSON metadata, and concise CLI text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes activity_score.tif, activity_level.tif, volcano_params.json, and output-manifest.json to the selected output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata and CLI VERSION; openai.yaml and CHANGELOG list 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
