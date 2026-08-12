## Description:

Extracts remote-sensing image features, trains a lightweight classifier, evaluates accuracy, and writes classification maps and reports using an offline numpy/sklearn workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT

## Use Case:

Developers and geospatial analysts use this skill to run local transfer-learning-style classification or clustering on remote-sensing imagery, including synthetic supervised evaluation and unsupervised processing of local GeoTIFF scenes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security summary reports that the main classifier appears local, but the artifact also bundles credential-reading, geocoding, and download code that is not disclosed in the offline skill description.

Mitigation: Review the package before installing, remove or document the extra helper modules, and require explicit user opt-in before enabling network or credential-related behavior.

Risk: The server security guidance says bundled Earthdata credentials should be treated as exposed.

Mitigation: Avoid using the bundled credential helpers unless that access is intended, and replace any exposed credentials with user-provided secrets from a controlled environment.

## Reference(s):

- [Artifact README](artifact/README.md)
- [Skill Definition](artifact/SKILL.md)
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/geoskill-transfer-learning-rs)

## Skill Output:

**Output Type(s):** [Files, JSON, Geospatial raster, Text]

**Output Format:** [GeoTIFF and JSON files with optional console status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes classification.tif, accuracy_report.json, and output-manifest.json to the selected output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata and entrypoint VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
